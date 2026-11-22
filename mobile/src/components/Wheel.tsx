import { Animated, View } from 'react-native';
import Svg, { Circle, G, Path, Polygon, Text as SvgText } from 'react-native-svg';
import { SLIVER_COLORS, type Sliver } from '../game/rules.ts';
import { colors, fonts } from '../theme.ts';

function point(cx: number, cy: number, r: number, deg: number): [number, number] {
  const a = (deg * Math.PI) / 180;
  return [cx + r * Math.sin(a), cy - r * Math.cos(a)];
}

function slicePath(cx: number, cy: number, r: number, from: number, to: number): string {
  if (to - from >= 359.99) return `M${cx - r} ${cy} A${r} ${r} 0 1 1 ${cx + r} ${cy} A${r} ${r} 0 1 1 ${cx - r} ${cy} Z`;
  const [x1, y1] = point(cx, cy, r, from);
  const [x2, y2] = point(cx, cy, r, to);
  const large = to - from > 180 ? 1 : 0;
  return `M${cx} ${cy} L${x1} ${y1} A${r} ${r} 0 ${large} 1 ${x2} ${y2} Z`;
}

function short(name: string, n: number): string {
  return name.length > n ? `${name.slice(0, n - 1)}…` : name;
}

/** Slice colors: the same prize keeps one color, so duplicates are easy to spot. */
export function sliverColor(wheel: Sliver[], i: number): string {
  const order: string[] = [];
  for (const s of wheel) if (!order.includes(s.prizeId)) order.push(s.prizeId);
  let c = order.indexOf(wheel[i].prizeId) % SLIVER_COLORS.length;
  // Neighbours with the same color blur together; nudge to the next color when that happens.
  if (wheel.length > 1 && i > 0 && wheel[i - 1].prizeId !== wheel[i].prizeId) {
    const prev = order.indexOf(wheel[i - 1].prizeId) % SLIVER_COLORS.length;
    if (prev === c) c = (c + 1) % SLIVER_COLORS.length;
  }
  return SLIVER_COLORS[c];
}

/**
 * The prize wheel. Slice 0 starts at the top and slices go clockwise. Pass `rotation`
 * (degrees) to spin it; the pointer stays fixed at the top.
 */
export function Wheel({ wheel, size, rotation, empty = 4 }: { wheel: Sliver[]; size: number; rotation?: Animated.Value; empty?: number }) {
  const c = size / 2;
  const r = c - 8;
  const count = Math.max(wheel.length, 1);
  const slice = 360 / count;
  const labelSize = Math.max(11, Math.min(15, size / (count > 8 ? 26 : 24)));
  const arc = 2 * r * 0.84 * Math.sin(((Math.min(slice, 180) / 2) * Math.PI) / 180);
  const iconSize = Math.max(14, Math.min(30, arc * 0.55, size / 12));
  const maxChars = Math.max(4, Math.floor((r * 0.5) / (labelSize * 0.56)));
  const showLabels = size >= 200;
  const rotate = rotation?.interpolate({ inputRange: [0, 360], outputRange: ['0deg', '360deg'] });

  return (
    <View style={{ width: size, height: size + 14 }} accessibilityLabel={`Prize wheel with ${wheel.length} slices`}>
      <Animated.View style={{ position: 'absolute', top: 14, width: size, height: size, transform: rotate ? [{ rotate }] : [] }}>
        <Svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
          <Circle cx={c} cy={c} r={r + 6} fill={colors.ink} />
          {wheel.length === 0
            ? Array.from({ length: empty }, (_, i) => (
                <Path key={i} d={slicePath(c, c, r, (i * 360) / empty, ((i + 1) * 360) / empty)} fill={i % 2 ? '#3A3253' : '#2F2846'} stroke={colors.ink} strokeWidth={3} />
              ))
            : wheel.map((s, i) => {
                const from = i * slice;
                const mid = from + slice / 2;
                const [ix, iy] = point(c, c, r * 0.84, mid);
                const name = short(s.name, maxChars);
                const flip = mid > 180;
                return (
                  <G key={s.id}>
                    <Path d={slicePath(c, c, r, from, from + slice)} fill={sliverColor(wheel, i)} stroke={colors.ink} strokeWidth={3} strokeLinejoin="round" />
                    <SvgText x={ix} y={iy + iconSize * 0.35} fontSize={iconSize} textAnchor="middle">{s.icon}</SvgText>
                    {showLabels && name ? (
                      // Text reads outward on the right half and inward on the left half, so it is never upside down.
                      <G transform={flip ? `rotate(${mid + 90} ${c} ${c})` : `rotate(${mid - 90} ${c} ${c})`}>
                        {[true, false].map((outline) => (
                          <SvgText
                            key={String(outline)}
                            x={flip ? c - r * 0.2 : c + r * 0.2}
                            y={c + labelSize * 0.35}
                            fontSize={labelSize}
                            fontFamily={fonts.bodyBold}
                            fontWeight="800"
                            fill="#FFFFFF"
                            stroke={outline ? colors.ink : undefined}
                            strokeWidth={outline ? 3 : 0}
                            strokeLinejoin="round"
                            textAnchor={flip ? 'end' : 'start'}
                          >
                            {name}
                          </SvgText>
                        ))}
                      </G>
                    ) : null}
                  </G>
                );
              })}
          <Circle cx={c} cy={c} r={size * 0.09} fill="#FFFFFF" stroke={colors.ink} strokeWidth={4} />
          <Circle cx={c} cy={c} r={size * 0.035} fill={colors.accent} />
        </Svg>
      </Animated.View>
      <Svg width={size} height={size * 0.16} style={{ position: 'absolute', top: 0 }} viewBox={`0 0 ${size} ${size * 0.16}`}>
        <Polygon
          points={`${c - size * 0.055},2 ${c + size * 0.055},2 ${c},${size * 0.14}`}
          fill={colors.accent}
          stroke={colors.ink}
          strokeWidth={4}
          strokeLinejoin="round"
        />
      </Svg>
    </View>
  );
}

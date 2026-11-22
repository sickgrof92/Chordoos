import { useRef, type ReactNode } from 'react';
import { Animated, Pressable, StyleSheet, Text, View, type StyleProp, type TextStyle, type ViewStyle } from 'react-native';
import { haptic } from '../feedback.ts';
import { colors, fonts, shadow } from '../theme.ts';

/** A pressable that squishes slightly and gives a light haptic tick. */
export function Squish({
  onPress,
  disabled,
  style,
  children,
  label,
  silent,
}: {
  onPress?: () => void;
  disabled?: boolean;
  style?: StyleProp<ViewStyle>;
  children: ReactNode;
  label?: string;
  silent?: boolean;
}) {
  const scale = useRef(new Animated.Value(1)).current;
  const to = (v: number) => Animated.spring(scale, { toValue: v, useNativeDriver: true, speed: 40, bounciness: 8 }).start();
  return (
    <Pressable
      accessibilityRole="button"
      accessibilityLabel={label}
      accessibilityState={{ disabled: !!disabled }}
      disabled={disabled}
      onPressIn={() => to(0.95)}
      onPressOut={() => to(1)}
      onPress={() => {
        if (!silent) haptic.tap();
        onPress?.();
      }}
    >
      <Animated.View style={[style, { transform: [{ scale }] }, disabled && { opacity: 0.5 }]}>{children}</Animated.View>
    </Pressable>
  );
}

export function Button({
  title,
  onPress,
  kind = 'plain',
  big,
  disabled,
  style,
}: {
  title: string;
  onPress: () => void;
  kind?: 'plain' | 'primary' | 'danger';
  big?: boolean;
  disabled?: boolean;
  style?: StyleProp<ViewStyle>;
}) {
  return (
    <Squish
      onPress={onPress}
      disabled={disabled}
      label={title}
      style={[s.btn, big && s.btnBig, kind === 'primary' && s.btnPrimary, style]}
    >
      <Text
        style={[
          s.btnText,
          big && s.btnTextBig,
          kind === 'primary' && { color: colors.accentInk },
          kind === 'danger' && { color: colors.danger },
        ]}
      >
        {title}
      </Text>
    </Squish>
  );
}

export function Panel({ children, style }: { children: ReactNode; style?: StyleProp<ViewStyle> }) {
  return <View style={[s.panel, style]}>{children}</View>;
}

export function H1({ children, style }: { children: ReactNode; style?: StyleProp<TextStyle> }) {
  return <Text style={[s.h1, style]}>{children}</Text>;
}
export function H2({ children, style }: { children: ReactNode; style?: StyleProp<TextStyle> }) {
  return <Text style={[s.h2, style]}>{children}</Text>;
}
export function Body({ children, style, muted }: { children: ReactNode; style?: StyleProp<TextStyle>; muted?: boolean }) {
  return <Text style={[s.body, muted && { color: colors.muted }, style]}>{children}</Text>;
}

export function Points({ value, scale, small }: { value: number; scale?: Animated.Value; small?: boolean }) {
  return (
    <Animated.View style={[s.stars, small && { paddingHorizontal: 9 }, scale && { transform: [{ scale }] }]} accessibilityLabel={`${value} points`}>
      <Text style={[s.starIcon, small && { fontSize: 17 }]}>★</Text>
      <Text style={[s.starText, small && { fontSize: 17 }]}>{value}</Text>
    </Animated.View>
  );
}

export function Avatar({ color, name, size = 84, children }: { color: string; name: string; size?: number; children?: ReactNode }) {
  return (
    <View
      style={{
        width: size,
        height: size,
        borderRadius: size / 2,
        backgroundColor: children ? colors.tile : color,
        alignItems: 'center',
        justifyContent: 'center',
        overflow: 'hidden',
      }}
    >
      {children ?? <Text style={{ fontFamily: fonts.display, fontSize: size * 0.45, color: '#fff' }}>{name.charAt(0).toUpperCase()}</Text>}
    </View>
  );
}

export const s = StyleSheet.create({
  btn: {
    minHeight: 48,
    paddingHorizontal: 18,
    borderRadius: 999,
    backgroundColor: colors.surface,
    borderWidth: 2,
    borderColor: colors.line,
    alignItems: 'center',
    justifyContent: 'center',
    ...shadow,
  },
  btnBig: { minHeight: 60, paddingHorizontal: 26 },
  btnPrimary: { backgroundColor: colors.accent, borderColor: colors.accent },
  btnText: { fontFamily: fonts.bodyBold, fontSize: 16, color: colors.ink },
  btnTextBig: { fontFamily: fonts.display, fontSize: 21 },
  panel: {
    backgroundColor: colors.surface,
    borderRadius: 26,
    borderWidth: 2,
    borderColor: colors.line,
    padding: 18,
    gap: 12,
  },
  h1: { fontFamily: fonts.display, fontSize: 34, lineHeight: 38, color: colors.ink },
  h2: { fontFamily: fonts.display, fontSize: 24, lineHeight: 28, color: colors.ink },
  body: { fontFamily: fonts.body, fontSize: 16, lineHeight: 22, color: colors.ink },
  stars: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: colors.surface,
    borderWidth: 2,
    borderColor: colors.line,
    borderRadius: 999,
    paddingHorizontal: 12,
    paddingVertical: 2,
  },
  starIcon: { color: colors.star, fontSize: 22 },
  starText: { fontFamily: fonts.display, fontSize: 22, color: colors.ink, fontVariant: ['tabular-nums'] },
});

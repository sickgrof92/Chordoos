import { memo, useId, useMemo } from 'react';
import { SvgXml } from 'react-native-svg';
import { colors } from '../theme.ts';
import { ART } from './artData.ts';

/** Shown for any character whose art hasn't been drawn yet. */
const PLACEHOLDER = `<svg viewBox="0 0 200 200"><path d="M100 50 C142 50 162 86 162 122 C162 158 136 178 100 178 C64 178 38 158 38 122 C38 86 58 50 100 50 Z" fill="#E4DEFA" stroke="#B9B0E0" stroke-width="4"/><text x="100" y="138" text-anchor="middle" font-size="56" font-weight="800" fill="#9A90C8">?</text></svg>`;

/** Turns art into a flat mystery shape for characters a kid hasn't found yet. */
function silhouette(xml: string, color: string): string {
  return xml
    .replace(/<defs>[\s\S]*?<\/defs>/g, '')
    // Glows and sparkles (class="fx") would turn into blobs, so mystery shapes leave them out.
    .replace(/<(circle|path|ellipse|g)[^>]*class="fx"[^>]*\/>/g, '')
    .replace(/<g[^>]*class="fx"[^>]*>[\s\S]*?<\/g>/g, '')
    .replace(/fill="(?!none)[^"]*"/g, `fill="${color}"`)
    .replace(/stroke="(?!none)[^"]*"/g, `stroke="${color}"`)
    .replace(/opacity="[^"]*"/g, '');
}

const silCache: Record<string, string> = {};

interface Props {
  id: string;
  size: number;
  locked?: boolean;
}

/** Gives each drawing's gradient ids a per-instance suffix so two copies on screen never clash. */
function scopeIds(xml: string, suffix: string): string {
  return xml.replace(/id="([^"]+)"/g, `id="$1-${suffix}"`).replace(/url\(#([^)]+)\)/g, `url(#$1-${suffix})`);
}

function CharacterImpl({ id, size, locked }: Props) {
  const suffix = useId().replace(/[^a-zA-Z0-9]/g, '');
  const xml = useMemo(() => {
    const art = ART[id] ?? PLACEHOLDER;
    return locked ? (silCache[id] ??= silhouette(art, colors.silhouette)) : scopeIds(art, suffix);
  }, [id, locked, suffix]);
  return <SvgXml xml={xml} width={size} height={size} />;
}

export const Character = memo(CharacterImpl);

import { useId } from 'react';
import { SvgXml } from 'react-native-svg';

/** The surprise pod. `cracks` 0-2 shows how far it has been tapped open. */
export function Pod({ size, color = '#FF6B4A', cracks = 0 }: { size: number; color?: string; cracks?: number }) {
  const gid = `pod${useId().replace(/[^a-zA-Z0-9]/g, '')}`;
  const crack = (d: string, show: boolean) =>
    show ? `<path d="${d}" fill="none" stroke="#2B2340" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>` : '';
  const xml = `<svg viewBox="0 0 100 120">
  <ellipse cx="50" cy="113" rx="28" ry="5" fill="#2B2340" opacity=".18"/>
  <defs><radialGradient id="${gid}" cx="0.35" cy="0.3" r="0.9"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#E7E2FA"/></radialGradient></defs>
  <path d="M50 8C78 8 88 44 88 70C88 96 72 108 50 108C28 108 12 96 12 70C12 44 22 8 50 8Z" fill="url(#${gid})" stroke="#2B2340" stroke-width="3"/>
  <path d="M12.5 62C14 40 25 8 50 8C75 8 86 40 87.5 62L76 56L64 66L50 56L36 66L24 56Z" fill="${color}" stroke="#2B2340" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="30" cy="34" r="5" fill="#fff" opacity=".55"/><circle cx="66" cy="26" r="3.5" fill="#fff" opacity=".55"/>
  <path d="M50 74l4.4 9 9.9 1.4-7.2 7 1.7 9.8-8.8-4.6-8.8 4.6 1.7-9.8-7.2-7 9.9-1.4z" fill="#FFC23D" stroke="#2B2340" stroke-width="2.5" stroke-linejoin="round"/>
  ${crack('M40 66L46 76L40 84', cracks >= 1)}
  ${crack('M66 64L60 74L68 80L62 90', cracks >= 2)}
  ${crack('M24 72L30 80L24 88', cracks >= 2)}
</svg>`;
  return <SvgXml xml={xml} width={size} height={size * 1.2} />;
}

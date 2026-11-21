import { createAudioPlayer, setAudioModeAsync, type AudioPlayer } from 'expo-audio';
import * as Haptics from 'expo-haptics';

const SOURCES = {
  ding: require('../assets/sounds/ding.wav'),
  tap: require('../assets/sounds/tap.wav'),
  crack: require('../assets/sounds/crack.wav'),
  reveal: require('../assets/sounds/reveal.wav'),
  revealBig: require('../assets/sounds/reveal-big.wav'),
} as const;

export type Sound = keyof typeof SOURCES;

const players: Partial<Record<Sound, AudioPlayer>> = {};
let configured = false;

/** Plays a short effect. Respects the silent switch and mixes with other apps' audio. */
export function play(sound: Sound, enabled: boolean): void {
  if (!enabled) return;
  try {
    if (!configured) {
      configured = true;
      setAudioModeAsync({ playsInSilentMode: false, interruptionMode: 'mixWithOthers' }).catch(() => {});
    }
    const p = (players[sound] ??= createAudioPlayer(SOURCES[sound]));
    p.seekTo(0).catch(() => {});
    p.play();
  } catch {
    // Sound is a nice-to-have; never let it break a tap.
  }
}

export const haptic = {
  tap: () => Haptics.selectionAsync().catch(() => {}),
  bump: () => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium).catch(() => {}),
  crack: () => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy).catch(() => {}),
  success: () => Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success).catch(() => {}),
  warn: () => Haptics.notificationAsync(Haptics.NotificationFeedbackType.Warning).catch(() => {}),
};

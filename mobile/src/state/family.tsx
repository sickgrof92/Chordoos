import AsyncStorage from '@react-native-async-storage/async-storage';
import { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState, type ReactNode } from 'react';
import { AppState } from 'react-native';
import { localDate, type FamilyState, type Kid, type Settings } from '../game/rules.ts';

const KEY = 'chordoos.family.v2';
const EMPTY: FamilyState = { version: 2, settings: null, kids: [] };

interface FamilyApi {
  ready: boolean;
  state: FamilyState;
  today: string;
  saveSettings: (s: Settings) => void;
  saveKid: (k: Kid) => void;
  removeKid: (id: string) => void;
  kid: (id: string | undefined) => Kid | undefined;
}

const Ctx = createContext<FamilyApi | null>(null);

export function FamilyProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<FamilyState>(EMPTY);
  const [ready, setReady] = useState(false);
  const [today, setToday] = useState(localDate());
  const writing = useRef<Promise<void>>(Promise.resolve());

  useEffect(() => {
    AsyncStorage.getItem(KEY)
      .then((raw) => {
        if (raw) {
          const parsed = JSON.parse(raw) as FamilyState;
          if (parsed && parsed.version === 2) setState(parsed);
        }
      })
      .catch(() => {})
      .finally(() => setReady(true));
  }, []);

  // Daily tasks reset when a new day starts, including when the app comes back from the background.
  useEffect(() => {
    const sub = AppState.addEventListener('change', (s) => {
      if (s === 'active') setToday(localDate());
    });
    const timer = setInterval(() => setToday(localDate()), 60_000);
    return () => {
      sub.remove();
      clearInterval(timer);
    };
  }, []);

  const commit = useCallback((fn: (s: FamilyState) => FamilyState) => {
    setState((prev) => {
      const next = fn(prev);
      const body = JSON.stringify(next);
      writing.current = writing.current.then(() => AsyncStorage.setItem(KEY, body)).catch(() => {});
      return next;
    });
  }, []);

  const api = useMemo<FamilyApi>(
    () => ({
      ready,
      state,
      today,
      saveSettings: (settings) => commit((s) => ({ ...s, settings })),
      saveKid: (k) =>
        commit((s) => {
          const exists = s.kids.some((x) => x.id === k.id);
          return { ...s, kids: exists ? s.kids.map((x) => (x.id === k.id ? k : x)) : [...s.kids, k] };
        }),
      removeKid: (id) => commit((s) => ({ ...s, kids: s.kids.filter((x) => x.id !== id) })),
      kid: (id) => state.kids.find((k) => k.id === id),
    }),
    [ready, state, today, commit],
  );

  return <Ctx.Provider value={api}>{children}</Ctx.Provider>;
}

export function useFamily(): FamilyApi {
  const v = useContext(Ctx);
  if (!v) throw new Error('useFamily must be used inside FamilyProvider');
  return v;
}

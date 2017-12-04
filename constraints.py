from itertools import combinations, izip
from prelims import fix_num, voices

def crossvoice(satb):
    # check to make sure voices never cross
    soprano, alto, tenor, bass = satb
    return all(i > j for i, j in izip(satb[:-1], satb[1:]))

def spacing(satb):
    # check to make sure spacing never exceeds an octave between upper 3 voices
    return all(i - j < 8 for i, j in izip(satb[:-2], satb[1:-1]))

def parallel(n):
    return lambda first, second: not all(fix_num(f - s) == n
                                         for f, s in izip(first, second))

def jump(n):
    def jumper(first, second):
        if first < second:
            first, second = second, first
        return first - second <= n
    return jumper


class ConstraintsAgg:

    def __init__(self, basics, voice_pairs, voice_singles):
        self.basics = basics
        self.voice_pairs = voice_pairs
        self.voice_singles = voice_singles
        self.ns = frozenset({1} | set(voice_pairs.iterkeys()) |
                            set(voice_singles.iterkeys()))

    def test(self, satbs):
        n = len(satbs)
        if n in self.voice_pairs:
            for first, second in combinations(izip(*satbs), 2):
                if not all(f(first, second) for f in self.voice_pairs[n]):
                    return False
        if n in self.voice_singles:
            for voice in zip(*satbs)[:-1]:
                if not all(f(*voice) for f in self.voice_singles[n]):
                    return False
        if n == 1:
            if not all(f(*satbs) for f in self.basics):
                return False
        return True


bach = ConstraintsAgg([crossvoice, spacing], {2: [parallel(5), parallel(8)]},
                      {2: [jump(5)]})

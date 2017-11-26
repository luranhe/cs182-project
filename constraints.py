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


class ConstraintsAgg:

    def __init__(self, basics, voice_pairs):
        self.basics = basics
        self.voice_pairs = voice_pairs
        self.ns = [1]
        self.ns.extend(voice_pairs.iterkeys())

    def test(self, satbs):
        n = len(satbs)
        return (all(f(*satbs) for f in self.basics if n == 1) and
                all(f(first, second) for f in self.voice_pairs[n]
                    for first, second in combinations(izip(*satbs), 2)
                    if n in self.voice_pairs))


bach = ConstraintsAgg([crossvoice, spacing], {2: [parallel(5), parallel(8)]})

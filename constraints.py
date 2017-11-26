from itertools import combinations, izip
from prelims import fix_num, voices

def crossvoice(satb):
    # check to make sure voices never cross
    soprano, alto, tenor, bass = satb
    return soprano > alto > tenor > bass

def spacing(satb):
    # check to make sure spacing never exceeds an octave between upper 3 voices
    treble_voices = satb[:-1]
    return all(i - j < 8 for i, j in zip(treble_voices[:-1], treble_voices[1:]))

def parallel(n):
    return lambda first, second: not all(fix_num(f - s) == n
                                         for f, s in zip(first, second))


class ConstraintsAgg:

    def __init__(self, basics, voice_pairs):
        self.basics = basics
        self.voice_pairs = voice_pairs
        self.ns = voice_pairs.keys()
        self.ns.append(1)

    def test(self, *satbs):
        n = len(satbs)
        if n == 1:
            if not all(f(*satbs) for f in self.basics):
                return False
        if n in self.voice_pairs:
            for first, second in combinations(izip(*satbs), 2):
                if not all(f(first, second) for f in self.voice_pairs[n]):
                    return False
        return True


bach = ConstraintsAgg([crossvoice, spacing], {2: [parallel(5), parallel(8)]})

from itertools import combinations
from prelims import fix_num

constraints_dict = {}

def cross_tester(satb):
    soprano, alto, tenor, bass = satb
    # check to make sure voices never cross
    if not soprano > alto > tenor > bass:
        return False
    return True

def spacing_tester(satb):
    treble_voices = satb[:-1]
    treble_names = voices[:-1]
    # check to make sure spacing never exceeds an octave between upper 3 voices
    for i, j in zip(treble_voices[:-1], treble_voices[1:]):
        if i - j >= 8:
            return False
    # if all goes well, return True
    return True

constraints_dict[1] = [cross_tester, spacing_tester]

def horizontal_tester(satb1, satb2):
    paired_voices = zip(satb1, satb2)
    for first, second in combinations(paired_voices, 2):
        # parallel octaves
        if all(f.name == s.name for f, s in zip(first, second)):
            return False
        # parallel fifths
        if all(fix_num(f - s) == 5 for f, s in zip(first, second)):
            return False
    return True

    # if all goes well, return True
    return True

constraints_dict[2] = [horizontal_tester]

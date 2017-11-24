from itertools import combinations
from prelims import *

def vertical_tester(satb):
    soprano, alto, tenor, bass = satb
    treble_voices = satb[:-1]
    treble_names = voices[:-1]
    # check ranges to make sure we haven't given unsingable notes
    for voice, name in zip(treble_voices, treble_names):
        if not lims[name][0] <= voice <= lims[name][1]:
            return False

    # check to make sure voices never cross
    if not soprano <= alto <= tenor <= bass:
        return False

    # check to make sure spacing never exceeds an octave between upper 3 voices
    for i, j in zip(treble_voices[:-1], treble_voices[1:]):
        if i - j > 7:
            return False

    # if all goes well, return True
    return True

# first chord has voices b_x through s_x, second chord here has b_y through s_y
def horizontal_tester(satb1, satb2):
    paired_voices = zip(satb1, satb2)
    for first, second in combinations(paired_voices, 2):
        # check for parallel octaves
        if all(f.name == s.name for f, s in zip(first, second)):
            return False
        # check for parallel fifths (assuming we've already tested crossing)
        if all(fix_num(f.data[0] - s.data[0]) == 4
               for f, s in zip(first, second)):
            return False
    return True

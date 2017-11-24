from prelims import *

def vertical_tester(bass, tenor, alto, soprano):
    treble_voices = [tenor, alto, soprano]
    treble_names = ['tenor', 'alto', 'soprano']
    # check ranges to make sure we haven't given unsingable notes
    for voice, name in zip(treble_voices, treble_names):
        if voice < lims[name][0] or lims[name][1] < voice:
            return False

    # check to make sure voices never cross
    if not soprano <= alto <= tenor <= bass:
        return False

    # check to make sure spacing never exceeds an octave between upper 3 voices
    note_num = [to_num[voice.name] + 7 * voice.octave for voice in treble_voices]
    if note_num[1] - note_num[0] > 7 or note_num[2] - note_num[1] > 7:
        return False

    # if all goes well, return True
    return True

# first chord has voices b_x through s_x, second chord here has b_y through s_y
def horizontal_tester(b_x, t_x, a_x, s_x, b_y, t_y, a_y, s_y):
    paired_voices = [(b_x, b_y), (t_x, t_y), (a_x, a_y), (s_x, s_y)]
    for first in paired_voices:
        paired_voices.remove(first)
        for second in paired_voices:
            # check for parallel octaves
            if first[0].name == second[0].name and first[1].name == second[1].name:
                return False
            # check for parallel fifths (assuming we've already tested crossing)
            if to_num[second[0].name] - to_num[first[0].name] == 4 and to_num[second[1].name] - to_num[first[1].name] == 4:
                return False
    return True

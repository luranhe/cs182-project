from collections import defaultdict
from itertools import product

class ComparableMixin:

    def __eq__(self, other):
        return not self < other and not other < self

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return not other < self


notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
to_let = dict(enumerate(notes, start=1))
to_num = {v: k for k, v in to_let.iteritems()}

def fix_num(n):
    n = n % 7
    return n + (not n) * 7


class Note(ComparableMixin):
    # Encoding musical notes (diatonic C major)

    def __init__(self, name, octave):
        if type(name) is str:
            self.data = (octave, to_num[name])
            self.name = name
        else:
            self.data = (octave, name)
            self.name = to_let[fix_num(name)]
        self.octave = self.data[0]

    def __lt__(self, other):
        return self.data < other.data

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return self.name + str(self.data[0])


lims = {'tenor': (Note('A', 2), Note('F', 4)),
        'alto': (Note('G', 3), Note('C', 5)),
        'soprano': (Note('C', 4), Note('A', 5))}


def all_about_that_bass(name, inversion):
    root = fix_num(name - inversion * 2)
    third = fix_num(root + 2)
    fifth = fix_num(third + 2)
    if root == 7:
        if inversion == 0:
            return [[third, third, fifth]]
        if inversion == 1:
            return [[root, third, fifth]]
        else:
            return [[root, third, third]]
    if inversion == 2:
        return [[root, third, fifth]]
    if root in (2, 3, 6):
        if inversion == 0:
            return [[third, third, fifth], [root, third, fifth]]
        else:
            return [[root, third, fifth], [root, root, fifth]]
    if root in (1, 4):
        if inversion == 0:
            return [[root, third, fifth], [third, fifth, fifth], [third, third, fifth]]
        else:
            return [[root, root, fifth], [root, fifth, fifth], [root, third, fifth]]
    else:
        if inversion == 0:
            return [[root, third, fifth], [root, fifth, fifth]]
        else:
            return [[root, root, fifth], [root, fifth, fifth]]

def voice_generator(note_ingredients):
    for i in note_ingredients:
        voice = defaultdict(list)
        #all possible notes for soprano, alto, and tenor
        for name in i:
            for octave in xrange(lims['tenor'][0].octave,
                                 lims['soprano'][1].octave):
                n = Note(name, octave)
                for v, lim in lims.iteritems():
                    lower, upper = lim
                    if lower <= n <= upper:
                        voice[v].append(n)

        #generates all possible chords in voice range as tuples of (soprano, alto, tenor)
        for el in product(voice['soprano'], voice['alto'], voice['tenor']):
            yield el

def vertical_tester(bass, tenor, alto, soprano):
    treble_voices = [tenor, alto, soprano]
    treble_names = ['tenor', 'alto', 'soprano']
    # check ranges to make sure we haven't given unsingable notes
    for voice, name in zip(treble_voices, treble_names):
        if voice < lims[name][0] or lims[name][1] < voice:
            return False
    
    # check to make sure voices never cross
    if tenor <= bass:
        return False
    if alto <= tenor:
        return False
    if soprano <= alto:
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
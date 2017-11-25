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

    def __sub__(self, other):
        assert self >= other
        d = self.octave * 7 + self.data[0] - other.octave * 7 - other.data[0]
        return d + 1

    def __str__(self):
        return self.name + str(self.data[0])


lims = {'tenor': (Note('A', 2), Note('F', 4)),
        'alto': (Note('G', 3), Note('C', 5)),
        'soprano': (Note('C', 4), Note('A', 5))}

voices = ['soprano', 'alto', 'tenor', 'bass']


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
            return [[root, third, fifth], [third, fifth, fifth],
                    [third, third, fifth]]
        else:
            return [[root, root, fifth], [root, fifth, fifth],
                    [root, third, fifth]]
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
        # generates all possible chords in voice range as SAT tuples
        for el in product(*(voice[v] for v in voices[:-1])):
            yield el

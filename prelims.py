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
            self.name = to_let(fix_num(name))

    def __lt__(self, other):
        return self.data < other.data

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return self.name + str(self.data[0])


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

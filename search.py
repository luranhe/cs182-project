import random
from itertools import ifilter
from prelims import fix_num

class NoSatisfaction(Exception):
    pass

successors = {1: range(1, 8),
              2: [5, 7],
              3: [6],
              4: [2, 5, 7],
              5: [1, 6],
              6: [2, 4, 5, 7],
              7: [1, 5, 6]}

predecessors = {i: [j for j in range(1, 8) if i in successors[j]]
                for i in range(1, 8)}

def find_chords(bassline):
    bassline = bassline[::-1]
    chords = []

    # acceptable cadences
    possibilities = [iter([1]), iter([5, 4])]
    i = 0
    n = len(bassline)

    # Bach voice leading rules don't make sense for n < 2
    if n < 2:
        raise NoSatisfaction('No possible chord sequence')
    while i < n:

        # get the possible previous chords
        try:
            it = possibilities[i]
        except IndexError:
            try:
                next_chord = chords[i - 1]

            # if i < 0, that means all possibilities have been exhausted
            except IndexError:
                raise NoSatisfaction('No possible chord sequence')
            poss = predecessors[next_chord][:]

            # shuffling gives nondeterministic behavior
            random.shuffle(poss)
            it = iter(poss)
            possibilities.append(it)

        # try to assign a value to the previous chord, backtracking if failing
        try:
            curr_note = bassline[i].data[1]
            prev_chord = ifilter(lambda n: curr_note
                                 in [fix_num(n + 2 * i)
                                     for i in xrange(3)], it).next()
            try:
                chords[i] = prev_chord
            except IndexError:
                chords.append(prev_chord)
            i += 1
        except StopIteration:
            possibilities.pop()
            i -= 1
    return chords[::-1]

def voice_leading(bassline, chords):
    pass

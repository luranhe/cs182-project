from random import shuffle
from itertools import ifilter, izip
from prelims import fix_num, all_about_that_bass, voice_generator

class NoSatisfaction(Exception):
    pass

successors = {1: range(1, 8),
              2: [5, 7],
              3: [6],
              4: [2, 5, 7],
              5: [1, 6],
              6: [2, 4, 5, 7],
              7: [1, 5, 6]}

predecessors = {i: [j for j in xrange(1, 8) if i in successors[j]]
                for i in xrange(1, 8)}

notes_in_chord = {c: frozenset(fix_num(c + 2 * i) for i in xrange(3))
                  for c in xrange(1, 8)}

def find_chords(bassline):
    bass = [b.num for b in bassline[::-1]]
    chords = []
    # acceptable cadences
    possibilities = [iter([1]), iter([5, 4])]
    i = 0
    n = len(bass)
    ex = NoSatisfaction('No possible chord sequence')
    # Bach voice leading rules don't make sense for n < 2
    if n < 2:
        raise ex
    while i < n:
        # get the possible previous chords
        try:
            gen = possibilities[i]
        except IndexError:
            next_chord = chords[i - 1]
            poss = predecessors[next_chord][:]
            # shuffling gives nondeterministic behavior
            shuffle(poss)
            gen = iter(poss)
            possibilities.append(gen)
        # try to assign a value to the previous chord, backtracking if failing
        try:
            b = bass[i]
            prev_chord = next(n for n in gen if b in notes_in_chord[n])
            chords.append(prev_chord)
            i += 1
        except StopIteration:
            try:
                chords.pop()
            # if all possibilities have been exhausted
            except IndexError:
                raise ex
            possibilities.pop()
            i -= 1
    return chords[::-1]

def voice_leading(bassline, chords, constraints):
    n = len(bassline)
    assert n == len(chords)
    recipes = [all_about_that_bass(b.num, fix_num(b.num - chord) / 2)
               for b, chord in izip(bassline, chords)]
    possibilities = []
    music = []
    i = 0
    while i < n:
        # get possible combos
        try:
            gen = possibilities[i]
        except IndexError:
            gen = voice_generator(recipes[i])
            possibilities.append(gen)
        # find a combo that satisfies the constraints, backtracking if failing
        b = bassline[i]
        try:
            while True:
                music.append(gen.next() + (b,))
                if all(constraints.test(music[i - num + 1:i + 1])
                       for num in constraints.ns if i + 1 >= num):
                    i += 1
                    break
                else:
                    music.pop()
        except StopIteration:
            music.pop()
            possibilities.pop()
            i -= 1
            # if all possibilities have been exhausted
            if i < 0:
                raise NoSatisfaction('No valid voice leading')
    return music

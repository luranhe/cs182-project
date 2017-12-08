from random import shuffle
from itertools import imap, izip
from abc import ABCMeta, abstractmethod, abstractproperty
from prelims import fix_num, all_about_that_bass, voice_generator
from constraints import bach


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


class Problem:
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        pass

    @abstractproperty
    def depth(self):
        pass

    @abstractmethod
    def succ_gen(self):
        pass

    @abstractmethod
    def constraints(self):
        pass

    @abstractmethod
    def to_output(self):
        pass

    @abstractproperty
    def fail(self):
        pass


class FindChords(Problem):
    fail = NoSatisfaction('No possible chord sequence')
    depth = None

    def __init__(self, bassline):
        self.bassline = [b.num for b in bassline[::-1]]
        self.depth = len(self.bassline)

    def start(self):
        return [iter([1]), iter([5, 4])]

    def succ_gen(self, _, next_chord):
        try:
            poss = predecessors[next_chord][:]
            shuffle(poss)
            return iter(poss)
        except KeyError:
            assert next_chord is None
            raise self.fail

    def constraints(self, res):
        i = len(res) - 1
        return self.bassline[i] in notes_in_chord[res[i]]

    def to_output(self, res):
        return res[::-1]


class VoiceLeading(Problem):
    fail = NoSatisfaction('No valid voice leading')
    depth = None

    def __init__(self, bassline, chords, consts):
        self.depth = len(bassline)
        assert self.depth == len(chords)
        self.bassline = bassline
        self.recipes = [all_about_that_bass(b.num, ((b.num - chord) % 7) / 2)
                        for b, chord in izip(bassline, chords)]
        self.consts = consts

    def start(self):
        return []

    def succ_gen(self, i, _):
        gen = voice_generator(self.recipes[i])
        return imap(lambda g: g + (self.bassline[i],), gen)

    def constraints(self, res):
        i = len(res)
        return all(self.consts.test(res[i - num:])
                   for num in self.consts.ns if i >= num)

    def to_output(self, res):
        return res


def DFSSolve(problem):
    i = 0
    res = []
    possibilities = problem.start()
    if len(possibilities) > problem.depth:
        raise problem.fail
    while i < problem.depth:
        try:
            gen = possibilities[i]
        except IndexError:
            try:
                gen = problem.succ_gen(i, res[i - 1])
            except IndexError:
                gen = problem.succ_gen(i, None)
            possibilities.append(gen)
        try:
            while True:
                res.append(gen.next())
                if problem.constraints(res):
                    i += 1
                    break
                else:
                    res.pop()
        except StopIteration:
            if i <= 0 or i + 1 != len(possibilities):
                raise problem.fail
            i -= 1
            possibilities.pop()
            res.pop()
    return problem.to_output(res)


def bring_AI_bach(bassline):
    find = FindChords(bassline)
    chords = DFSSolve(find)
    voice = VoiceLeading(bassline, chords, bach)
    return DFSSolve(voice)

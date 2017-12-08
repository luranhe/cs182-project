from random import choice, randint
from itertools import izip, islice, cycle
from prelims import voice_generator
from constraints import bach
from search import *

def heuristic_dist(chord_list):
    total_dist = 0
    for chord_1, chord_2 in izip(chord_list[:-1], chord_list[1:]):
        for (first, second) in izip(chord_1[:-1], chord_2[:-1]):
            if first < second:
                first, second = second, first
            total_dist += (first - second) ** 2
    return total_dist

class ConstraintsViolated(Exception):
    pass

def hill_climb(bassline, reps):
    find = FindChords(bassline)
    chords_set = DFSSolve(find)
    voice = VoiceLeading(bassline, chords_set, bach)
    possibilities = [list(voice_generator(r)) for r in voice.recipes]
    voicing = DFSSolve(voice)
    current_voicing = voicing[:]
    current_dist = heuristic_dist(current_voicing)
    bass_len = len(bassline)
    print('Initial Distance: ' + str(current_dist))
    print('Climbing...')
    for i in islice(cycle(xrange(bass_len)), reps):
        bass = bassline[i]
        chord = chords_set[i]
        possibles = possibilities[i]
        new_v = current_voicing[:]
        new_v[i] = choice(possibles) + (bass,)
        new_dist = heuristic_dist(new_v)
        if new_dist < current_dist:
            try:
                for n in voice.consts.ns:
                    for inc in xrange(n):
                        start = i - inc
                        end = start + n
                        if start >= 0 and end < bass_len:
                            if not voice.consts.test(new_v[start:end]):
                                raise ConstraintsViolated
                current_voicing = new_v
                current_dist = new_dist
            except ConstraintsViolated:
                pass
    print('Final Distance: ' + str(current_dist))
    return voicing, current_voicing

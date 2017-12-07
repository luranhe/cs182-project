from prelims import *
from constraints import bach
from search import *
from random import *
from itertools import izip

def heuristic_dist(chord_list):
    total_dist = 0
    for chord_1, chord_2 in izip(chord_list[:-1], chord_list[1:]):
        for (first, second) in izip(chord_1[:-1], chord_2[:-1]):
            if first < second:
                first, second = second, first
            total_dist += first - second
    return total_dist

class ConstraintsViolated(Exception):
    pass

def hill_climb(bassline, reps):
    find = FindChords(bassline)
    chords_set = DFSSolve(find)
    voice = VoiceLeading(bassline, chords_set, bach)
    current_voicing = DFSSolve(voice)
    current_dist = heuristic_dist(current_voicing)
    bass_len = len(bassline)
    print('Initial Distance: ' + str(current_dist))
    print('Climbing...')
    for x in range(0, reps):
        rand_num = randint(0, bass_len - 1)
        bass = bassline[rand_num]
        chord = chords_set[rand_num]
        recipe = all_about_that_bass(bass.num, ((bass.num - chord) % 7) / 2)
        
        new_v = current_voicing[:rand_num]
        possibles = list(voice_generator(recipe))
        shuffle(possibles)
        new_v.append(possibles[0] + (bass,))
        new_v += current_voicing[rand_num + 1:]
        new_dist = heuristic_dist(new_v)
        
        if new_dist < current_dist:
            try:
                for n in voice.consts.ns:
                    for i in range(n):
                        start_index = rand_num - i
                        end_index = start_index + n
                        if start_index >= 0 and end_index < bass_len:
                            if not voice.consts.test(new_v[start_index:end_index]):
                                raise ConstraintsViolated
                current_voicing = new_v
                current_dist = new_dist
            except ConstraintsViolated:
                pass
    print('Final Distance: ' + str(current_dist))
    return current_voicing
        


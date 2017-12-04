from prelims import Note
from constraints import bach
from search import *

print('Running Bach tests...')

import time
start_time = time.time()

bass_1 = [Note('C', 3), Note('D', 3), Note('E', 3), Note('G', 2), Note('C', 3)]
find_1 = FindChords(bass_1)
chords_1 = DFSSolve(find_1)
v_1 = VoiceLeading(bass_1, chords_1, bach)
voiced_1 = DFSSolve(v_1)

# from BWV 43: Ermuntre dich, mein schwacher Geist
bass_2 = [Note('C', 3), Note('A', 2), Note('G', 2), Note('C', 3), Note('D', 3),
	  Note('C', 3), Note('D', 3), Note('D', 2), Note('G', 2), Note('C', 3),
	  Note('F', 2), Note('C', 2), Note('G', 2), Note('A', 2), Note('G', 2),
	  Note('C', 2)]
find_2 = FindChords(bass_2)
chords_2 = DFSSolve(find_2)
v_2 = VoiceLeading(bass_2, chords_2, bach)
voiced_2 = DFSSolve(v_2)

# from BWV 318: Gottes Sohn ist Kommen
bass_3 = [Note('A', 2), Note('B', 2), Note('C', 3), Note('A', 2), Note('G', 2),
	  Note('C', 3)]
find_3 = FindChords(bass_3)
chords_3 = DFSSolve(find_3)
v_3 = VoiceLeading(bass_3, chords_3, bach)
voiced_3 = DFSSolve(v_3)

# from BWV 376: Lobt Gott, ihr Christen allzugleich
bass_4 = [Note('C', 3), Note('B', 2), Note('G', 2), Note('C', 3), Note('E', 3),
	  Note('F', 2), Note('G', 2), Note('C', 2)]
find_4 = FindChords(bass_4)
chords_4 = DFSSolve(find_4)
v_4 = VoiceLeading(bass_4, chords_4, bach)
voiced_4 = DFSSolve(v_4)

# from BWV 248: Von Himmel hoch da komm ich her
bass_5 = [Note('C', 2), Note('G', 2), Note('A', 2), Note('D', 2), Note('E', 2),
	  Note('F', 2), Note('D', 2), Note('C', 2)]
find_5 = FindChords(bass_5)
chords_5 = DFSSolve(find_5)
v_5 = VoiceLeading(bass_5, chords_5, bach)
voiced_5 = DFSSolve(v_5)

# from BWV 414: Uns ist ein Kindlein heut geborn
bass_6 = [Note('C', 2), Note('G', 2), Note('A', 2), Note('F', 2), Note('G', 2),
	  Note('E', 2), Note('G', 2), Note('G', 2), Note('C', 2)]
find_6 = FindChords(bass_6)
chords_6 = DFSSolve(find_6)
v_6 = VoiceLeading(bass_6, chords_6, bach)
voiced_6 = DFSSolve(v_6)   

'''
# from BWV 178: Wo Gott der Herr nicht bei uns halt
bass_7 = [Note('A', 3), Note('E', 3), Note('F', 3), Note('E', 3), Note('C', 3),
	  Note('F', 3), Note('G', 3), Note('C', 3)]
find_7 = FindChords(bass_6)
chords_7 = DFSSolve(find_6)
v_7 = VoiceLeading(bass_6, chords_6, bach)
voiced_7 = DFSSolve(v_6)
'''

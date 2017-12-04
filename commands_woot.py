from prelims import Note
from constraints import bach
from search import *
bass_1 = [Note('C', 3), Note('D', 3), Note('E', 3), Note('G', 2), Note('C', 3)]
find_1 = FindChords(bass_1)
chords_1 = DFSSolve(find_1)
v_1 = VoiceLeading(bass_1, chords_1, bach)
voiced_1 = DFSSolve(v_1)

# BWV 43: Ermuntre dich, mein schwacher Geist (adapted and transposed)
bass_2 = [Note('C', 3), Note('A', 2), Note('G', 2), Note('C', 3), Note('D', 3),
	  Note('C', 3), Note('D', 3), Note('D', 2), Note('G', 2), Note('C', 3),
	  Note('F', 2), Note('C', 2), Note('G', 2), Note('A', 2), Note('G', 2),
	  Note('C', 2)]
find_2 = FindChords(bass_2)
chords_2 = DFSSolve(find_2)
v_2 = VoiceLeading(bass_2, chords_2, bach)
voiced_2 = DFSSolve(v_2)

from prelims import Note
from constraints import bach
from search import *

def bring_AI_bach(bassline):
    find = FindChords(bassline)
    chords = DFSSolve(find)
    voice = VoiceLeading(bassline, chords, bach)
    return DFSSolve(voice)

basslines = []

bass = [Note('C', 3), Note('D', 3), Note('E', 3), Note('G', 2), Note('C', 3)]
basslines.append(bass)

# from BWV 43: Ermuntre dich, mein schwacher Geist
bass = [Note('C', 3), Note('A', 2), Note('G', 2), Note('C', 3), Note('D', 3),
        Note('C', 3), Note('D', 3), Note('D', 2), Note('G', 2), Note('C', 3),
        Note('F', 2), Note('C', 2), Note('G', 2), Note('A', 2), Note('G', 2),
        Note('C', 2)]
basslines.append(bass)

# from BWV 318: Gottes Sohn ist Kommen
bass = [Note('A', 2), Note('B', 2), Note('C', 3), Note('A', 2), Note('G', 2),
        Note('C', 3)]
basslines.append(bass)

# from BWV 376: Lobt Gott, ihr Christen allzugleich
bass = [Note('C', 3), Note('B', 2), Note('G', 2), Note('C', 3), Note('E', 3),
        Note('F', 2), Note('G', 2), Note('C', 2)]
basslines.append(bass)

# from BWV 248: Von Himmel hoch da komm ich her
bass = [Note('C', 2), Note('G', 2), Note('A', 2), Note('D', 2), Note('E', 2),
        Note('F', 2), Note('D', 2), Note('C', 2)]
basslines.append(bass)

# from BWV 414: Uns ist ein Kindlein heut geborn
bass = [Note('C', 2), Note('G', 2), Note('A', 2), Note('F', 2), Note('G', 2),
        Note('E', 2), Note('G', 2), Note('G', 2), Note('C', 2)]
basslines.append(bass)

'''
# from BWV 178: Wo Gott der Herr nicht bei uns halt
bass = [Note('A', 3), Note('E', 3), Note('F', 3), Note('E', 3), Note('C', 3),
        Note('F', 3), Note('G', 3), Note('C', 3)]
basslines.append(bass)
'''

voiced = [bring_AI_bach(b) for b in basslines]

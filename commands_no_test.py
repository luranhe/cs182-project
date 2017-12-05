from prelims import Note
from constraints import bach
from search import *

def bring_AI_bach(bassline):
    find = FindChords(bassline)
    chords = DFSSolve(find)
    voice = VoiceLeading(bassline, chords, bach)
    return DFSSolve(voice)

voiced = []

bass_1 = [Note('C', 3), Note('D', 3), Note('E', 3), Note('G', 2), Note('C', 3)]
voiced.append(bring_AI_bach(bass_1))

# from BWV 43: Ermuntre dich, mein schwacher Geist
bass_2 = [Note('C', 3), Note('A', 2), Note('G', 2), Note('C', 3), Note('D', 3),
          Note('C', 3), Note('D', 3), Note('D', 2), Note('G', 2), Note('C', 3),
          Note('F', 2), Note('C', 2), Note('G', 2), Note('A', 2), Note('G', 2),
          Note('C', 2)]
voiced.append(bring_AI_bach(bass_2))

# from BWV 318: Gottes Sohn ist Kommen
bass_3 = [Note('A', 2), Note('B', 2), Note('C', 3), Note('A', 2), Note('G', 2),
          Note('C', 3)]
voiced.append(bring_AI_bach(bass_3))

# from BWV 376: Lobt Gott, ihr Christen allzugleich
bass_4 = [Note('C', 3), Note('B', 2), Note('G', 2), Note('C', 3), Note('E', 3),
          Note('F', 2), Note('G', 2), Note('C', 2)]
voiced.append(bring_AI_bach(bass_4))

# from BWV 248: Von Himmel hoch da komm ich her
bass_5 = [Note('C', 2), Note('G', 2), Note('A', 2), Note('D', 2), Note('E', 2),
          Note('F', 2), Note('D', 2), Note('C', 2)]
voiced.append(bring_AI_bach(bass_5))

# from BWV 414: Uns ist ein Kindlein heut geborn
bass_6 = [Note('C', 2), Note('G', 2), Note('A', 2), Note('F', 2), Note('G', 2),
          Note('E', 2), Note('G', 2), Note('G', 2), Note('C', 2)]
voiced.append(bring_AI_bach(bass_6))

'''
# from BWV 178: Wo Gott der Herr nicht bei uns halt
bass_7 = [Note('A', 3), Note('E', 3), Note('F', 3), Note('E', 3), Note('C', 3),
          Note('F', 3), Note('G', 3), Note('C', 3)]
voiced_7 = bring_AI_bach(bass_7)
'''

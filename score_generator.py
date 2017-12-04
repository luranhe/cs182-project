from abjad import *
import abjad
from prelims import Note
from constraints import bach
from search import *

#chords generated
from prelims import Note
from constraints import bach
from search import *

print('Running Bach tests...')

bass_6 = [Note('C', 2), Note('G', 2), Note('A', 2), Note('F', 2), Note('G', 2),
          Note('E', 2), Note('G', 2), Note('G', 2), Note('C', 2)]
find_6 = FindChords(bass_6)
chords_6 = DFSSolve(find_6)
v_6 = VoiceLeading(bass_6, chords_6, bach)
voiced_6 = DFSSolve(v_6)   


#right format
notes = []
soprano = ""
alto = ""
tenor = ""
bass = ""
for chord in voiced_1:
    voice_counter = 1
    for note in chord:
        (octave,note_num) = note.data
        name = str.lower(note.name)
        if octave >= 4:
            for j in range(octave-3):
                name = name+"'"
        if octave == 2:
            name = name+","
        if octave == 1:
            name = name+",,"
        name = name+"4"
        
        #builds the voices
        if voice_counter == 1:
            soprano = soprano+name+" "
        if voice_counter == 2:
            alto = alto+name+" "
        if voice_counter == 3:
            tenor = tenor+name+" "
        if voice_counter == 4:
            bass = bass+name+" "
        voice_counter = voice_counter+1
print soprano

#build the score
container = abjad.Container()
l = len(voiced_1)-1

clef = abjad.Clef('soprano')
container.append(abjad.Voice(soprano))

container.append(abjad.Voice(alto))

container.append(abjad.Voice(tenor))
clef = abjad.Clef('bass')
abjad.attach(clef, container[2])

container.append(abjad.Voice(bass))
clef = abjad.Clef('bass')
abjad.attach(clef, container[3])
container.is_simultaneous = True
show(container) 

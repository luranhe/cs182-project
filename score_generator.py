import abjad

def show_score(voiced_chords):

    def add2staff(voice1, voice2, staff):
        voice1 = abjad.Voice(voice1)
        command = abjad.indicatortools.LilyPondCommand('voiceOne')
        abjad.attach(command, voice1)
        voice2 = abjad.Voice(voice2)
        command = abjad.indicatortools.LilyPondCommand('voiceTwo')
        abjad.attach(command, voice2)
        staff.extend([voice1, voice2])
        staff.is_simultaneous = True

    #right format
    notes = []
    satb = [""] * 4
    for chord in voiced_chords:
        for i, note in enumerate(chord):
            octave = note.octave
            name = str.lower(note.name)
            name += ("'" * (octave - 3) * (octave > 3) +
                     "," * (3 - octave) * (octave < 3) + "4 ")

            #builds the voices
            satb[i] += name

    soprano, alto, tenor, bass = satb

    #build the score

    upper_staff = abjad.Staff()
    lower_staff = abjad.Staff()
    satb_staff = abjad.StaffGroup([upper_staff, lower_staff])

    add2staff(soprano, alto, upper_staff)
    add2staff(tenor, bass, lower_staff)
    abjad.attach(abjad.Clef('bass'), lower_staff[0])

    abjad.show(satb_staff)

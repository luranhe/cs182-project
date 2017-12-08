import abjad
from examples import basslines
from search import bring_AI_bach
from hill import hill_climb

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
    # abjad.play(satb_staff)

def main():
    print 'Choose your bassline:'
    print '0: Sample'
    print '1: excerpt from BWV 43: Ermuntre dich, mein schwacher Geist'
    print '2: excerpt from BWV 318: Gottes Sohn ist Kommen'
    print '3: excerpt from BWV 376: Lobt Gott, ihr Christen allzugleich'
    print '4: excerpt from BWV 248: Von Himmel hoch da komm ich her'
    print '5: excerpt from BWV 414: Uns ist ein Kindlein heut geborn'
    i = raw_input(' >>  ')
    try:
        return basslines[int(i)]
    except (ValueError, IndexError) as _:
        print 'Invalid input, please try again. :('
        return main()

def ishill():
    print 'Hill climbing?'
    i = raw_input('y/[n]: ')
    b = i == 'y'
    if b:
        print 'Proceeding with Hill Climbing (1000 steps)'
    else:
        print 'Proceeding with Backtracking Search'
    return b

loading = 'Loading the result...'
wait = ('(This may take a few seconds. ' +
        'Once open, you may need to close the windows to continue)')

bass = main()
if ishill():
    pre, post = hill_climb(bass, 1000)
    print 'Before hill climbing:'
    print loading
    print wait
    show_score(pre)
    print 'After hill climbing:'
    print loading
    print wait
    show_score(post)
else:
    print loading
    print wait
    show_score(bring_AI_bach(bass))

from scamp import *
playback_settings.recording_file_path = "miamidada_terryogara_120723.wav"

# ----------------------------------------------------------------------------
# SECTION 0: PROJECT INFORMATION
# ----------------------------------------------------------------------------

# TITLE: 'Miami Dada' 
# COMPOSER: Terry O'Gara
# DATE: 12/07/2023
# COPYRIGHT: (c) 2023 Terry O'Gara. All rights reserved.
# ABOUT THIS PROJECT: Cinematic computer music composition scored using Python

# ----------------------------------------------------------------------------

s = Session()
s.tempo = 80

# ----------------------------------------------------------------------------
# SECTION A: INSTRUMENTS AND SFX
# ----------------------------------------------------------------------------

#SFX
fx=s.new_part("Goblin")
heli=s.new_part("Helicopter")
gunshots=s.new_part("Gun Shot")
phone=s.new_part("Telephone")
synthbeep = s.new_part("SCP-Beeper", soundfont="Synths.sf2")
synthwobble = s.new_part("SupSawA", soundfont="Synths.sf2")
scratch_hit = s.new_part("Scratch 2", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
scratch_trans = s.new_part("Scratch 5", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")

#RHYTHM
bass = s.new_part("DY-Synthe", soundfont="Synths.sf2")
drumkit=s.new_part("Kit 10", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
percussion1=s.new_part("Shakers", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
percussion2=s.new_part("CongasBngos", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
percussion3=s.new_part("Timbales", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
orch_hit=s.new_part("Orchestra Hit")
heavydrum=s.new_part("Taiko Drum")

#HARMONY
harmony_strings = s.new_part("PlasticStrings", soundfont="Synths.sf2")
harmony_chorus = s.new_part("Poly Synth")
harmony_breakdown = s.new_part("Synth Strings")
harmony_brasspad=s.new_part("Brass")
brasshit=s.new_part("Brass Hit 3", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
end_chord=s.new_part("Orchestra")

#EARCANDY
gtr1_drivepad=s.new_part("Overdrive Guitar")
gtr2_riffs=s.new_part("Gtr gtr2_riffs", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")

#VOCALS
vox1 = s.new_part("Vox Hit 1", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
vox2 = s.new_part("Vox Hit 2", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
vox3 = s.new_part("Vox Hit 3", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
vox4 = s.new_part("Vox Hit 4", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")
vox5 = s.new_part("Soul Oohs", soundfont="Emu_Planet_Phatt_Hip_Hop.sf2")

#BREAKDOWN ENSEMBLE
pit_player1 = s.new_part("Baritone Sax")
pit_player2 = s.new_part("Accordion")
pit_player3 = s.new_part("Mute Tpt")
pit_player4 = s.new_part("Vibraphone")
pit_player5 = s.new_part("Trumpet 2")
pit_player6 = s.new_part("UprightBass")
pit_player7 = s.new_part("Ocarina")
synthx = s.new_part("CandyBee", soundfont="Synths.sf2")

# ----------------------------------------------------------------------------
# SECTION B: SAMPLE TRIGGERS AND MUSIC PROGRAMMING
# ----------------------------------------------------------------------------
 

# ------------------------------------------------------------------
# SFX
# ------------------------------------------------------------------

def streetnoise():
    heavydrum.play_note(40, 1, 3.0, blocking=False)
    fx.play_note(57, 1, 8)
    wait(0.25)
    gunshots.play_note(50, 1, .75)
    wait(0.25)
    gunshots.play_note(51, 1, .75)
    wait(2.25)
    gunshots.play_note(52, 1, .75)
    wait(3)
    heli.play_note(60, 1, 16)
 
def phonecall():
    wait(16)
    
    wait(1.0)
    phone.play_note(60, 1, 3.0)

    wait(1.0)
    phone.play_note(60, 1, 3.0)

    wait(1.0)
    phone.play_note(60, 1, 3.0)


def scratchout():
    wait(21)
    scratch_trans.play_note(71, 0.7, 3.0)
    

def bighit():
    heavydrum.play_note(40, 1, 2.0, blocking=False)
    drumkit.play_note(87, 3.0, .9, blocking=False)
    orch_hit.play_note(69, 3.0, 3.0, blocking=False)
    scratch_hit.play_note(71, 3.0, .9, blocking=False)
    vox5.play_note(69, 0.7, 1, blocking=False) #a
    end_chord.play_note(45, 1, 2.0, blocking=False)
    end_chord.play_note(48, 1, 2.0, blocking=False)
    end_chord.play_note(52, 1, 2.0)
    wait(1.0)
    
# ------------------------------------------------------------------
# MELODIES
# ------------------------------------------------------------------

def melody(): #mallets
    wait(1.0)
    pit_player4.play_note(69, 0.7, 1.0) #a
    wait(2.0)
    
    pit_player4.play_note(62, 0.7, .5) #d
    pit_player4.play_note(65, 0.7, .5) #f
    pit_player4.play_note(62, 0.7, .5) #d
    pit_player4.play_note(69, 0.7, 1.5) #a
    wait(1.0)
    
    wait(.5)
    pit_player4.play_note(72, 0.7, 1.0) #b
    pit_player4.play_note(67, 0.7, .5) #g
    pit_player4.play_note(64, 0.7, 1.5) #e
    wait(.5)
    
    wait(.5)
    pit_player4.play_note(60, 0.7, .5) #c
    pit_player4.play_note(64, 0.7, .5) #e
    pit_player4.play_note(60, 0.7, .5) #c
    pit_player4.play_note(69, 0.7, 1.0) #a
    wait(1.0)
    
    pit_player4.play_note(57, 0.7, 1.0) #a
    pit_player4.play_note(69, 0.7, 1.0) #a
    wait(2)
    
    pit_player4.play_note(62, 0.7, .5) #d
    pit_player4.play_note(65, 0.7, .5) #f
    pit_player4.play_note(62, 0.7, .5) #d
    pit_player4.play_note(69, 0.7, 1.5) #a
    wait(1.0)
    
    pit_player4.play_note(72, 0.7, 1.0) #b
    pit_player4.play_note(67, 0.7, .5) #g
    pit_player4.play_note(64, 0.7, 1.5) #e
    wait(1)
    
    wait(.5)
    pit_player4.play_note(60, 0.7, .5) #c
    pit_player4.play_note(64, 0.7, .5) #e
    pit_player4.play_note(60, 0.7, .5) #c
    pit_player4.play_note(57, 0.7, 1.0) #a
    wait(1.0)


def melody2(): #Trumpet
    wait(4)

    pit_player5.play_note(74, 0.7, .75) #d
    pit_player5.play_note(77, 0.7, .25) #f
    pit_player5.play_note(74, 0.7, .75) #d
    pit_player5.play_note(81, 0.7, .25) #a
    pit_player5.play_note(81, 0.7, 1.0) #a
    
    wait(.5)
    pit_player5.play_note(71, 0.7, .5) #b
    pit_player5.play_note(79, 0.7, .5) #g
    pit_player5.play_note(76, 0.7, 1.0) #e
    wait(1.5)
    
    wait(.5)
    pit_player5.play_note(72, 0.7, 1/3) #c
    pit_player5.play_note(76, 0.7, 1/3) #e
    pit_player5.play_note(72, 0.7, 1/3) #c
    pit_player5.play_note(81, 0.7, 1.0) #a
    wait(1.5)
    
    wait(.5)
    pit_player5.play_note(81, 0.7, .5) #a
    pit_player5.play_note(81, 0.7, 1.0) #a
    wait(2.0)
    
    pit_player5.play_note(74, 0.7, .75) #d
    pit_player5.play_note(77, 0.7, .25) #f
    pit_player5.play_note(74, 0.7, .75) #d
    pit_player5.play_note(81, 0.7, .25) #a
    pit_player5.play_note(81, 0.7, 1.0) #a
    
    wait(.5)
    pit_player5.play_note(71, 0.7, .5) #b
    pit_player5.play_note(79, 0.7, .5) #g
    pit_player5.play_note(76, 0.7, 1.0) #e
    wait(1.5)
    
    wait(.5)
    pit_player5.play_note(72, 0.7, 1/3) #c
    pit_player5.play_note(76, 0.7, 1/3) #e
    pit_player5.play_note(72, 0.7, 1/3) #c
    pit_player5.play_note(81, 0.7, 1.5) #a
    wait(1.0)
    
    
def melody3(): #Ocarina
    wait(4)
    
    pit_player7.play_note(74+12, 0.7, .75) #d
    pit_player7.play_note(77+12, 0.7, .25) #f
    pit_player7.play_note(74+12, 0.7, .75) #d
    pit_player7.play_note(81+12, 0.7, .25) #a
    pit_player7.play_note(81+12, 0.7, 1.0) #a
    
    wait(.5)
    pit_player7.play_note(71+12, 0.7, .5) #b
    pit_player7.play_note(79+12, 0.7, .5) #g
    pit_player7.play_note(76+12, 0.7, 1.0) #e
    wait(1.5)
    
    wait(.5)
    pit_player7.play_note(72+12, 0.7, 1/3) #c
    pit_player7.play_note(76+12, 0.7, 1/3) #e
    pit_player7.play_note(72+12, 0.7, 1/3) #c
    pit_player7.play_note(81+12, 0.7, 1.0) #a
    wait(1.5)
    
    wait(.5)
    pit_player7.play_note(81+12, 0.7, .5) #a
    pit_player7.play_note(81+12, 0.7, 1.0) #a
    wait(2.0)
    
    pit_player7.play_note(74+12, 0.7, .75) #d
    pit_player7.play_note(77+12, 0.7, .25) #f
    pit_player7.play_note(74+12, 0.7, .75) #d
    pit_player7.play_note(81+12, 0.7, .25) #a
    pit_player7.play_note(81+12, 0.7, 1.0) #a
    
    wait(.5)
    pit_player7.play_note(71+12, 0.7, .5) #b
    pit_player7.play_note(79+12, 0.7, .5) #g
    pit_player7.play_note(76+12, 0.7, 1.0) #e
    wait(1.5)
    
    wait(.5)
    pit_player7.play_note(72+12, 0.7, 1/3) #c
    pit_player7.play_note(76+12, 0.7, 1/3) #e
    pit_player7.play_note(72+12, 0.7, 1/3) #c
    pit_player7.play_note(81+12, 0.7, 1.5) #a
    wait(1.0)
    
# ------------------------------------------------------------------
# PERCUSSION
# ------------------------------------------------------------------

def transhits():
    wait(28)
    drumkit.play_note(92, .25, .25) #transhit
    drumkit.play_note(92, .25, .25)
    wait(.25)
    drumkit.play_note(92, .25, .25)

    wait(.25)
    drumkit.play_note(92, .25, .25)
    drumkit.play_note(92, .25, .25) 
    wait(.25)
    
    drumkit.play_note(92, .25, .25)
    drumkit.play_note(92, .25, .25)
    wait(.25)
    drumkit.play_note(92, .25, .25)

    wait(.25)
    drumkit.play_note(92, .25, .25)
    drumkit.play_note(92, .25, .25) 
    wait(.25)
  
  
def timbalehits():
    wait(28)
    percussion3.play_note(60, .25, .5) #timbales
    percussion3.play_note(60, .25, .5)
    wait(.5)
    percussion3.play_note(60, .25, .5)
    percussion3.play_note(60, .25, .5)
    percussion3.play_note(60, .25, .5)
    percussion3.play_note(60, .25, .5)
    percussion3.play_note(60, .25, .5)
    
    
def hihat():
    counter2=0
    while counter2<2:
        drumkit.play_note(66, .25, .75) #hihat
        drumkit.play_note(66, .25, .25)
        drumkit.play_note(66, .25, .75)
        wait(.25)
        wait(2.0)
        
        drumkit.play_note(66, .25, .75)
        drumkit.play_note(66, .25, .25)
        drumkit.play_note(66, .25, .125)
        wait(.125)
        wait(2.75)
        
        counter2=counter2+1
    
    wait(16)
                      

def shakerz():
    wait(16)
    counter3=0
    while counter3<4:
        percussion1.play_note(65, .25, .75) #shakers
        percussion1.play_note(65, .25, .25)
        percussion1.play_note(65, .25, .75) 
        percussion1.play_note(65, .25, .25)
        percussion1.play_note(65, .25, .75) 
        percussion1.play_note(65, .25, .25)
        percussion1.play_note(65, .25, .75)
        percussion1.play_note(65, .25, .25)
        
        counter3=counter3+1


def shakerz2():
    counter4=0
    while counter4<8:
        percussion1.play_note(32, .25, .75) #shaker2
        percussion1.play_note(32, .25, .25)
        percussion1.play_note(32, .25, .75) 
        percussion1.play_note(32, .25, .25)
        percussion1.play_note(32, .25, .75) 
        percussion1.play_note(32, .25, .25)
        percussion1.play_note(32, .25, .75)
        percussion1.play_note(32, .25, .25)
        
        counter4=counter4+1    

def handdrums():
    counter10=0
    while counter10<4:
        percussion2.play_note(59, 0.25, .5)
        percussion2.play_note(60, 0.25, .5)
        percussion2.play_note(59, 0.25, .5)
        percussion2.play_note(59, 0.25, .5)
        
        percussion2.play_note(61, 0.25, 1.0)
        percussion2.play_note(60, 0.25, 1.0)
        
        wait(.5)
        percussion2.play_note(59, 0.25, .5)
        
        wait(.5)
        percussion2.play_note(63, 0.25, .5)
        
        wait(.5)
        percussion2.play_note(59, 0.25, .5)
        percussion2.play_note(60, 0.25, .5)
        percussion2.play_note(64, 0.25, .5)

        counter10=counter10+1
        
# ------------------------------------------------------------------
# RHTYHM SECTION
# ------------------------------------------------------------------

def kicksnare():
    counter5=0
    while counter5<4:
        
        drumkit.play_note(72, 1, 1.0) #kick
        drumkit.play_note(62, 0.7, 1.0) #snare
        drumkit.play_note(72, 1, .5) #kick
        drumkit.play_note(72, 1, .5) #kick
        drumkit.play_note(62, 0.7, 1.0) #snare
        
        wait(.5)
        drumkit.play_note(72, 1, .5) #kick
        drumkit.play_note(62, 0.7, 1.0) #snare
        wait(.5)
        drumkit.play_note(72, 1, .5) #kick
        drumkit.play_note(62, 0.7, .5) #snare
        drumkit.play_note(62, 0.7, .5) #snare
        
        counter5=counter5+1

 
def bassline():
    for pitch in [45, 50, 52, 45, 45, 50, 52, 45]: #a(45), d(50), e(52)
        bass.play_note(pitch, 0.25, 0.5)
        bass.play_note(pitch, 0.25, 0.5)
        
        wait(0.5)
        bass.play_note(pitch, 0.25, 0.5)
        
        wait(0.5)
        bass.play_note(pitch, 0.25, 0.5)
        
        wait(0.5)
        bass.play_note(pitch, 0.25, 0.5)
        
# ------------------------------------------------------------------
# VERSE: PADS
# ------------------------------------------------------------------

def openharmony():
    counter1=0
    while counter1<2:

        #measure 1, beat 1 (am)
        harmony_strings.play_note(45, 1, 2.0, blocking=False)
        harmony_strings.play_note(48, 1, 2.0, blocking=False)
        harmony_strings.play_note(52, 1, 2.0)
        wait(2.0)
        
        #measure 1, beat 3 (dm)
        harmony_strings.play_note(45, 1, 3.0, blocking=False)
        harmony_strings.play_note(50, 1, 3.0, blocking=False)
        harmony_strings.play_note(53, 1, 3.0)
        wait(1.0)
        
        #measure 1, beat 2 (em)
        harmony_strings.play_note(55, 1, 2.0, blocking=False)
        harmony_strings.play_note(59, 1, 2.0, blocking=False)
        harmony_strings.play_note(52, 1, 2.0)
        wait(2.0)

        #measure 1, beat 4 (am)
        harmony_strings.play_note(45, 1, 3.0, blocking=False)
        harmony_strings.play_note(48, 1, 3.0, blocking=False)
        harmony_strings.play_note(52, 1, 3.0)
        wait(1.0)
          
        counter1=counter1+1
        
def pad_verse():
    counter6=0
    while counter6<2:
        #measure 1, beat 1 (am)
        harmony_strings.play_note(57, 1, 3.0, blocking=False)
        harmony_strings.play_note(60, 1, 3.0, blocking=False)
        harmony_strings.play_note(64, 1, 3.0)
        wait(1.0)
        
        #measure 1, beat 3 (dm)
        harmony_strings.play_note(57, 1, 3.0, blocking=False)
        harmony_strings.play_note(62, 1, 3.0, blocking=False)
        harmony_strings.play_note(65, 1, 3.0)
        wait(1.0)
        
        #measure 1, beat 2 (em)
        harmony_strings.play_note(55, 1, 3.0, blocking=False)
        harmony_strings.play_note(59, 1, 3.0, blocking=False)
        harmony_strings.play_note(64, 1, 3.0)
        wait(1.0)

        #measure 1, beat 4 (am)
        harmony_strings.play_note(57, 1, 3.0, blocking=False)
        harmony_strings.play_note(60, 1, 3.0, blocking=False)
        harmony_strings.play_note(64, 1, 3.0)
        wait(1.0)
        
        counter6=counter6+1

    
def pad_chorus():
    counter7=0
    while counter7<2:
        #measure 1, beat 1 (am)
        harmony_chorus.play_note(57, 1, 3.0, blocking=False)
        harmony_chorus.play_note(60, 1, 3.0, blocking=False)
        harmony_chorus.play_note(64, 1, 3.0)
        wait(1.0)
        
        #measure 1, beat 3 (dm)
        harmony_chorus.play_note(57, 1, 3.0, blocking=False)
        harmony_chorus.play_note(62, 1, 3.0, blocking=False)
        harmony_chorus.play_note(65, 1, 3.0)
        wait(1.0)
        
        #measure 1, beat 2 (em)
        harmony_chorus.play_note(55, 1, 3.0, blocking=False)
        harmony_chorus.play_note(59, 1, 3.0, blocking=False)
        harmony_chorus.play_note(64, 1, 3.0)
        wait(1.0)

        #measure 1, beat 4 (am)
        harmony_chorus.play_note(57, 1, 3.0, blocking=False)
        harmony_chorus.play_note(60, 1, 3.0, blocking=False)
        harmony_chorus.play_note(64, 1, 3.0)
        wait(1.0)
        
        counter7=counter7+1
    
    
def pad_break():
    counter8=0
    while counter8<2:
        #measure 1, beat 1 (am)
        heavydrum.play_note(40, 1, 3.0, blocking=False)
        harmony_breakdown.play_note(57, 1, 3.0, blocking=False)
        harmony_breakdown.play_note(60, 1, 3.0, blocking=False)
        harmony_breakdown.play_note(64, 1, 3.0)
        wait(1.0)
        
        #measure 1, beat 3 (dm)
        harmony_breakdown.play_note(57, 1, 3.0, blocking=False)
        harmony_breakdown.play_note(62, 1, 3.0, blocking=False)
        harmony_breakdown.play_note(65, 1, 3.0)
        wait(1.0)
        
        #measure 1, beat 2 (em)
        harmony_breakdown.play_note(55, 1, 3.0, blocking=False)
        harmony_breakdown.play_note(59, 1, 3.0, blocking=False)
        harmony_breakdown.play_note(64, 1, 3.0)
        wait(1.0)

        #measure 1, beat 4 (am)
        harmony_breakdown.play_note(57, 1, 3.0, blocking=False)
        harmony_breakdown.play_note(60, 1, 3.0, blocking=False)
        harmony_breakdown.play_note(64, 1, 3.0)
        wait(1.0)
        
        counter8=counter8+1
    

def overdrive():
    counter9=0
    while counter9<2:
        #measure 1, beat 1 (am)
        synthbeep.play_note(33, 1, 3.0, blocking=False)
        gtr2_riffs.play_note(63, .5, 3.0, blocking=False)
        synthwobble.play_note(57, .25, 1.5)
        wait(1.0)
        
        #measure 1, beat 3 (dm)
        gtr2_riffs.play_note(62, .5, 3.0, blocking=False)
        synthwobble.play_note(65, .25, 2.0)
        wait(1.0)
        
        #measure 1, beat 2 (em)
        gtr2_riffs.play_note(60, .5, 2.0, blocking=False)
        synthwobble.play_note(52, .25, 2.0)
        wait(2.0)

        #measure 1, beat 4 (am)
        gtr2_riffs.play_note(64, .5, 3.0, blocking=False)
        wait(1.0)
        
        counter9=counter9+1
    
    
def brassharmony():
    wait(16)
    #measure 1, beat 1 (am)
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(48, 1, .5, blocking=False)
    harmony_brasspad.play_note(52, 1, .5)
    
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(48, 1, .5, blocking=False)
    harmony_brasspad.play_note(52, 1, .5)
    
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(48, 1, .5, blocking=False)
    harmony_brasspad.play_note(52, 1, .5)
    
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(48, 1, .5, blocking=False)
    harmony_brasspad.play_note(52, 1, .5)
    
    wait(2.0)
    
    #measure 1, beat 3 (dm)
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(50, 1, .5, blocking=False)
    harmony_brasspad.play_note(53, 1, .5)
    
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(50, 1, .5, blocking=False)
    harmony_brasspad.play_note(53, 1, .5)
    
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(50, 1, .5, blocking=False)
    harmony_brasspad.play_note(53, 1, .5)
    
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45+12, 1, .5, blocking=False)
    harmony_brasspad.play_note(50+12, 1, .5, blocking=False)
    harmony_brasspad.play_note(53+12, 1, .5)
    
    wait(2.0)
    
    #measure 1, beat 2 (em)
    brasshit.play_note(55, 1, .5, blocking=False)
    harmony_brasspad.play_note(55, 1, .5, blocking=False)
    harmony_brasspad.play_note(59, 1, .5, blocking=False)
    harmony_brasspad.play_note(52, 1, .5)
    
    brasshit.play_note(55, 1, .5, blocking=False)
    harmony_brasspad.play_note(55, 1, .5, blocking=False)
    harmony_brasspad.play_note(59, 1, .5, blocking=False)
    harmony_brasspad.play_note(52, 1, .5)
    
    brasshit.play_note(55, 1, .5, blocking=False)
    harmony_brasspad.play_note(55, 1, .5, blocking=False)
    harmony_brasspad.play_note(59, 1, .5, blocking=False)
    harmony_brasspad.play_note(52, 1, .5)
    
    brasshit.play_note(55, 1, .5, blocking=False)
    harmony_brasspad.play_note(55+12, 1, .5, blocking=False)
    harmony_brasspad.play_note(59+12, 1, .5, blocking=False)
    harmony_brasspad.play_note(52+12, 1, .5)
                       
    wait(2.0)

    #measure 1, beat 4 (am)
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(48, 1, .5, blocking=False)
    harmony_brasspad.play_note(52, 1, .5)
    
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(48, 1, .5, blocking=False)
    harmony_brasspad.play_note(52, 1, .5)
    
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(48, 1, .5, blocking=False)
    harmony_brasspad.play_note(52, 1, .5)
    
    brasshit.play_note(45, 1, .5, blocking=False)
    harmony_brasspad.play_note(45+12, 1, .5, blocking=False)
    harmony_brasspad.play_note(48+12, 1, .5, blocking=False)
    harmony_brasspad.play_note(52+12, 1, .5)
    
    wait(1.0)
    
    brasshit.play_note(45, 1, 1/3, blocking=False)
    harmony_brasspad.play_note(45, 1, 1/3, blocking=False)
    harmony_brasspad.play_note(48, 1, 1/3, blocking=False)
    harmony_brasspad.play_note(52, 1, 1/3)
    
    brasshit.play_note(45, 1, 1/3, blocking=False)
    harmony_brasspad.play_note(45, 1, 1/3, blocking=False)
    harmony_brasspad.play_note(48, 1, 1/3, blocking=False)
    harmony_brasspad.play_note(52, 1, 1/3)
    
    brasshit.play_note(45, 1, 1/3, blocking=False)
    harmony_brasspad.play_note(45+12, 1, 1/3, blocking=False)
    harmony_brasspad.play_note(48+12, 1, 1/3, blocking=False)
    harmony_brasspad.play_note(52+12, 1, 1/3)

# ------------------------------------------------------------------
# VOCALS
# ------------------------------------------------------------------
 
def vocals():
    for pitch in [82, 75, 77, 69, 82, 75, 77, 69]: #a(69), d(73), e(77)
        wait(1)
        vox2.play_note(pitch, 0.25, 1.5)
        wait(1)
        vox3.play_note(pitch-1, 0.25, .5)
        
        synthx.play_note(pitch+11, 1, 1.0)
        wait(3)
        
        wait(0.5)
        vox1.play_note(pitch+5, 0.25, .75)
        wait(0.25)
        synthx.play_note(pitch+11, 0.25, 1.5)
        #wait(1.0)
        
        wait(4.0)


def risingline():
     
    wait(1.0)

    #rising line (1-8)
    synthx.play_note(69, 0.7, 1/3) #a
    vox5.play_note(71, 0.7, 1/3) #b
    synthx.play_note(69, 0.7, 1/3) #a
    
    synthx.play_note(71, 0.7, 1/3) #b
    vox5.play_note(72, 0.7, 1/3) #c
    synthx.play_note(71, 0.7, 1/3) #b
    
    synthx.play_note(72, 0.7, 1/3) #c
    vox5.play_note(74, 0.7, 1/3) #d
    synthx.play_note(72, 0.7, 1/3) #c
    
    synthx.play_note(74, 0.7, 1/3) #d
    vox5.play_note(76, 0.7, 1/3) #e
    synthx.play_note(74, 0.7, 1/3) #d
    
    synthx.play_note(76, 0.7, 1/3) #e
    vox5.play_note(77, 0.7, 1/3) #f
    synthx.play_note(76, 0.7, 1/3) #e
    
    synthx.play_note(77, 0.7, 1/3) #f
    vox5.play_note(79, 0.7, 1/3) #g
    synthx.play_note(77, 0.7, 1/3) #f
    
    synthx.play_note(79, 0.7, 1/3) #g
    vox5.play_note(81, 0.7, 1/3) #a
    synthx.play_note(79, 0.7, 1/3) #g
    
    #descending line (9-16)
    vox5.play_note(88, 0.7, 1/3) #e
    synthx.play_note(86, 0.7, 1/3) #d
    synthx.play_note(84, 0.7, 1/3) #c
    
    vox5.play_note(86, 0.7, 1/3) #d
    synthx.play_note(84, 0.7, 1/3) #c
    synthx.play_note(83, 0.7, 1/3) #b
    
    vox5.play_note(84, 0.7, 1/3) #c
    synthx.play_note(83, 0.7, 1/3) #b
    synthx.play_note(84, 0.7, 1/3) #c
    
    vox5.play_note(86, 0.7, 1/3) #d
    synthx.play_note(84, 0.7, 1/3) #c
    synthx.play_note(82, 0.7, 1/3) #b
    
    vox5.play_note(81, 0.7, 2.0) #a
    wait(2.0)
    
    #16-24
    wait(8.0)
    
    #descending line (25-32)
    synthx.play_note(88, 0.7, 1/3) #e
    vox5.play_note(86, 0.7, 1/3) #d
    synthx.play_note(84, 0.7, 1/3) #c
    
    synthx.play_note(86, 0.7, 1/3) #d
    vox5.play_note(84, 0.7, 1/3) #c
    synthx.play_note(83, 0.7, 1/3) #b
    
    synthx.play_note(84, 0.7, 1/3) #c
    vox5.play_note(83, 0.7, 1/3) #b
    synthx.play_note(84, 0.7, 1/3) #c
    
    synthx.play_note(86, 0.7, 1/3) #d
    vox5.play_note(84, 0.7, 1/3) #c
    synthx.play_note(82, 0.7, 1/3) #b
    
    vox5.play_note(81, 0.7, 4.0) #a   


def endline():
    wait(16)
    
    #am
    wait(1.0)
    
    synthx.play_note(76, 0.7, 1/3) #e
    vox5.play_note(69, 0.7, 1/3) #a
    synthx.play_note(72, 0.7, 1/3) #c
    
    synthx.play_note(72, 0.7, 1/3) #c
    vox5.play_note(76, 0.7, 1/3) #e
    synthx.play_note(69, 0.7, 1/3) #a
    
    synthx.play_note(69, 0.7, 1/3) #a
    vox5.play_note(72, 0.7, 1/3) #c
    synthx.play_note(76, 0.7, 1/3) #e
    
    #dm
    synthx.play_note(74, 0.7, 1/3) #d
    vox5.play_note(77, 0.7, 1/3) #f
    synthx.play_note(69, 0.7, 1/3) #a
    
    synthx.play_note(77, 0.7, 1/3) #f
    vox5.play_note(69, 0.7, 1/3) #a
    synthx.play_note(74, 0.7, 1/3) #d
    
    synthx.play_note(69, 0.7, 1/3) #a
    vox5.play_note(74, 0.7, 1/3) #d
    synthx.play_note(77, 0.7, 1/3) #f
    
    synthx.play_note(74, 0.7, 1/3) #d
    vox5.play_note(77, 0.7, 1/3) #f
    synthx.play_note(69, 0.7, 1/3) #a
    
    
#     #em - decided not to use these, but saving them if I decide to change back at a later date
#     synthx.play_note(76, 0.7, 1/3) #e
#     vox5.play_note(79, 0.7, 1/3) #g
#     synthx.play_note(72, 0.7, 1/3) #b
#     
#     synthx.play_note(79, 0.7, 1/3) #g
#     vox5.play_note(72, 0.7, 1/3) #b
#     synthx.play_note(76, 0.7, 1/3) #e
#     
#     synthx.play_note(72, 0.7, 1/3) #b
#     vox5.play_note(76, 0.7, 1/3) #e
#     synthx.play_note(79, 0.7, 1/3) #g
#     
#     synthx.play_note(76, 0.7, 1/3) #e
#     vox5.play_note(79, 0.7, 1/3) #g
#     synthx.play_note(72, 0.7, 1/3) #b
    
    
    #am
#     synthx.play_note(69, 0.7, 1/3) #a
#     vox5.play_note(72, 0.7, 1/3) #c
#     synthx.play_note(76, 0.7, 1/3) #e
#     
#     synthx.play_note(76, 0.7, 1/3) #e
#     vox5.play_note(69, 0.7, 1/3) #a
#     synthx.play_note(72, 0.7, 1/3) #c
#     
#     synthx.play_note(72, 0.7, 1/3) #c
#     vox5.play_note(76, 0.7, 1/3) #e
#     synthx.play_note(69, 0.7, 1/3) #a
#     
#     synthx.play_note(69, 0.7, 1/3) #a
#     vox5.play_note(72, 0.7, 1/3) #c
#     synthx.play_note(76, 0.7, 1/3) #e   
        
# ------------------------------------------------------------------
# BREAKDOWN: ASCENDING OCTAVES
# ------------------------------------------------------------------                     
                     
def breakdown_sax(): #Baritone Sax
    for pitch in range(45, 53): #loop through a range
         if pitch % 2 == 0: #if values are an even numbered pitch, execute the following-
            pit_player1.play_note(pitch+4, 0.5, 0.75)
            pit_player1.play_note(pitch+2, 0.5, 0.25)
             
            pit_player1.play_note(pitch+5, 0.5, 0.75)
            pit_player1.play_note(pitch+4, 0.5, 0.25)
             
            pit_player1.play_note(pitch+7, 0.5, 0.75)
            pit_player1.play_note(pitch+5, 0.5, 0.25)
             
            pit_player1.play_note(pitch+9, 0.5, 0.75)
            pit_player1.play_note(pitch+7, 0.5, 0.25)
                  
         else: #if values are an odd numbered pitch, execute the following-
            pit_player1.play_note(pitch-1, 0.7, 1/3)
            pit_player1.play_note(pitch-2, 0.7, 1/3)
            pit_player1.play_note(pitch-3, 0.7, 1/3)
             
            pit_player1.play_note(pitch, 0.7, 1.0)
            wait(2.0)


def breakdown_bellows(): #Accordion
    for pitch in range(45, 53): #loop through a range
         if pitch % 2 == 0: #if values are an even numbered pitch, execute the following-
            wait(.25)
            pit_player2.play_note(pitch+4, 0.5, 0.25)
            pit_player2.play_note(pitch+2, 0.5, 0.5)
             
            wait(.25)
            pit_player2.play_note(pitch+5, 0.5, 0.25)
            pit_player2.play_note(pitch+4, 0.5, 0.5)
             
            wait(.25)
            pit_player2.play_note(pitch+7, 0.5, 0.25)
            pit_player2.play_note(pitch+5, 0.5, 0.5)
             
            wait(.25)
            pit_player2.play_note(pitch+9, 0.5, 0.25)
            pit_player2.play_note(pitch+7, 0.5, 0.5)
                  
         else: #if values are an odd numbered pitch, execute the following-
            pit_player2.play_note(pitch-1, 0.7, 1/3)
            pit_player2.play_note(pitch-2, 0.7, 1/3)
            pit_player2.play_note(pitch-3, 0.7, 1/3)
             
            pit_player2.play_note(pitch, 0.7, 1.0)
            wait(1.0)

def breakdown_bass(): #Upright Bass
    for pitch in range(45, 53): #loop through a range
        if pitch % 2 == 0: #if values are an even numbered pitch, execute the following-
            pit_player6.play_note(pitch+4, 0.5, 0.75)
            pit_player6.play_note(pitch+2, 0.5, 0.25)
             
            pit_player6.play_note(pitch+5, 0.5, 0.75)
            pit_player6.play_note(pitch+4, 0.5, 0.25)
             
            pit_player6.play_note(pitch+7, 0.5, 0.75)
            pit_player6.play_note(pitch+5, 0.5, 0.25)
             
            pit_player6.play_note(pitch+9, 0.5, 0.75)
            pit_player6.play_note(pitch+7, 0.5, 0.25)
                  
        else: #if values are an odd numbered pitch, execute the following-
            pit_player6.play_note(pitch-1, 0.7, 1/3)
            pit_player6.play_note(pitch-2, 0.7, 1/3)
            pit_player6.play_note(pitch-3, 0.7, 1/3)
             
            pit_player6.play_note(pitch, 0.7, 1.0)
            wait(2.0)
        
# ------------------------------------------------------------------
# SECTION 3: MUSICAL SECTIONS
# ------------------------------------------------------------------
   
def melodyfx():
    fork(streetnoise)
    melody()


def pads():
    fork(pad_verse)
    overdrive()


def rhythmsection():
    fork(hihat)
    fork(shakerz)
    fork(bassline)
    kicksnare()
       

def moodyopen():
    fork(openharmony)
    fork(streetnoise)
    fork(shakerz)
    fork(transhits)
    melody()


def mainverse():
    fork(melodyfx)
    pad_verse()


def chorus():
    fork(melody2)
    fork(vocals)
    fork(overdrive)
    pad_chorus()
   
   
def breakdown():
    fork(breakdown_sax)
    fork(breakdown_bellows)
    fork(breakdown_bass)
    fork(pad_break)
    fork(brassharmony)
    fork(shakerz2)
    fork(melody3)
    fork(transhits)
    fork(timbalehits)
    handdrums()


def chorusout():
    fork(melody2)
    fork(vocals)
    fork(overdrive)
    fork(timbalehits)
    fork(phonecall)
    fork(scratchout)
    pad_chorus()

def endhit():
    bighit()
    
# ------------------------------------------------------------------
# SECTION 4: PLAY MUSIC COMMANDS
# ------------------------------------------------------------------

#intro
moodyopen()
 
#a section: verse
fork(mainverse)
rhythmsection()

#b  section: chorus
fork(chorus)
rhythmsection()

#c section: breakdown
fork(risingline)
breakdown()

#chorus and close
fork(chorus)
fork(endline)
fork(phonecall)
fork(timbalehits)
rhythmsection()

endhit()


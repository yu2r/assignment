from microbit import *

def midiNoteOn(chan, n, vel):
    MIDI_NOTE_ON = 0x90
    if chan > 15:
        return
    if n > 127:
        return
    if vel > 127:
        return
    msg = bytes([MIDI_NOTE_ON | chan, n, vel])
    uart.write(msg)
def midiNoteOff(chan, n, vel):
    MIDI_NOTE_OFF = 0x80
    if chan > 15:
        return
    if n > 127:
        return
    if vel > 127:
        return
    msg = bytes([MIDI_NOTE_OFF | chan, n, vel])
    uart.write(msg)

def Start():
    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)

Start()
lastA = False
lastB = False
lastC = False
BUTTON_A_NOTE = 36
BUTTON_B_NOTE = 86
last_ldr = 0
while True:
    # set up the photoresistance
    ldr= pin0.read_analog()
    if last_ldr != ldr:
        velocity = math.floor(ldr / 1024 * 127)
        midiControlChange(0, 127, velocity)
    last_ldr = ldr

    # Button a and b are used to check whether the MIDI signal is connected normally
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    if a is True and lastA is False:
        midiNoteOn(0, BUTTON_A_NOTE, 127)
    elif a is False and lastA is True:
        midiNoteOff(0, BUTTON_A_NOTE, 127)
    if b is True and lastB is False:
        midiNoteOn(0, BUTTON_B_NOTE, 127)
    elif b is False and lastB is True:
        midiNoteOff(0, BUTTON_B_NOTE, 127)

    ## "##" is the description and "#" is the pseudocode.

    ## Button c is used to change the type of waveform (Pseudocode)
    c = pin1.is_touched()
    # count = button_c.get_presses()
    # set counter = 0
    ## There are four waveform in the pd patch, each time you press the button_c the waveform would change.
    # if C is True and lastC is False:
    #    counter + 1
    #    output the counter message
    # elif c is False and lastC is True:
    #    Stop counting
    # if counter > 4
    #    then set counter to 1
    # elif counter++
    # lastC = c


    lastA = a
    lastB = b
    sleep(10)


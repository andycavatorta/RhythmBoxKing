
import time
import threading
import mido
import sys
import MRQ1
import duplexPort

# globals
MIDI_PORT = False
MIDI_mapping = [None] * 127
MIDI_mapping[97] = [MRQ1.setClockOscillator,[1,0]]
MIDI_mapping[98] = [MRQ1.setClockOscillator,[1,1]]
MIDI_mapping[99] = [MRQ1.setClockOscillator,[1,2]]
MIDI_mapping[93] = [MRQ1.setClockOscillator,[0,0]]
MIDI_mapping[94] = [MRQ1.setClockOscillator,[0,1]]
MIDI_mapping[95] = [MRQ1.setClockOscillator,[0,2]]
MIDI_mapping[36] = [MRQ1.triggerSnare,None]]
MIDI_mapping[37] = [MRQ1.triggerBongo,None]
MIDI_mapping[38] = [MRQ1.triggerBlock,None]
MIDI_mapping[39] = [MRQ1.triggerBass ,None]
MIDI_mapping[68] = [MRQ1.triggerBrush,None]
MIDI_mapping[96] = [MRQ1.setVolume, 1]
MIDI_mapping[92] = [MRQ1.setVolume, 0]
MIDI_mapping[67] = [MRQ1.setBalance,1]
MIDI_mapping[63] = [MRQ1.setBalance,0]
MIDI_mapping[65] = [MRQ1.toggleExternalClock,None]
MIDI_mapping[64] = [MRQ1.togglePower,None]

# init simurgh



# init duplex port
def testCallback(msg_l):
    print "testCallback:", msg_l

duplexPort.init(testCallback)


# init MIDI
def mido_init():
	midiOutputs_l = mido.get_output_names()
	if len(midiOutputs_l)  < 2:
	    print "MIDI Outputs not found.  Check USB connection."
	    sys.exit(0)
	else:
		global MIDI_PORT
	    MIDI_PORT = mido.open_output(midiOutputs_l[0])
		MIDI_PORT = mido.open_input(callback=mapMIDI)
		MIDI_PORT.callback = mapMIDI

# MIDI mappings
def mapMIDI(msg):
	print msg
	mapping_l = MIDI_mapping[msg.note]
	if not mapping_l:
		print "mapping for pitch not found:", msg.note
		return
	fpgaParams = mapping_l[0](msg, mapping_l[1])
	print "fpgaParams",fpgaParams
	duplexPort.send(fpgaParams[0],fpgaParams[1])

# signal functions

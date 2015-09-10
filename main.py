
import time
import threading
import mido
import sys
import MRQ1
#import duplexPort

# globals
MIDI_PORT = False
MIDI_note_mapping = [None] * 127

MIDI_note_mapping[91] = [MRQ1.droneSnare,16]
MIDI_note_mapping[93] = [MRQ1.droneBongo,16]
MIDI_note_mapping[95] = [MRQ1.droneBass, 16]
MIDI_note_mapping[96] = [MRQ1.droneBrush,16]
MIDI_note_mapping[98] = [MRQ1.droneBlock,16]

MIDI_note_mapping[100] = [MRQ1.triggerSnare,None]
MIDI_note_mapping[101] = [MRQ1.triggerBongo,None]
MIDI_note_mapping[105] = [MRQ1.triggerBlock,None]
MIDI_note_mapping[107] = [MRQ1.triggerBass ,None]
MIDI_note_mapping[103] = [MRQ1.triggerBrush,None]

MIDI_note_mapping[119] = [MRQ1.toggleExternalClock,None]
MIDI_note_mapping[120] = [MRQ1.togglePower,None]
MIDI_CC_mapping = [None] * 127
MIDI_CC_mapping[74] = [MRQ1.setClockOscillator,0]
MIDI_CC_mapping[71] = [MRQ1.setClockOscillator,1]
MIDI_CC_mapping[91] = [MRQ1.setClockOscillator,2]
MIDI_CC_mapping[93] = [MRQ1.setVolume,3]
MIDI_CC_mapping[73] = [MRQ1.setBalance,4]

# init simurgh
"""
# init duplex port
def TestCallback():
	while True:
		time.sleep(1)
#duplexPort.init(testcallback)
testcallback = threading.Thread(target=TestCallback)
testcallback.start()

duplexPort.init(testcallback)
"""

# init MIDI
def mido_init():
	midiInputs_l = mido.get_output_names()
	print ">> MIDI Inputs", midiInputs_l
	if len(midiInputs_l)  < 2:
	    print "MIDI inputs not found.  Check USB connection."
	    sys.exit(0)
	else:
		global MIDI_PORT
		#MIDI_PORT = mido.open_output(midiOutputs_l[0])
		MIDI_PORT = mido.open_input(midiInputs_l[1],callback=mapMIDI)
		#MIDI_PORT = mido.open_input(midiInputs_l[0],callback=mapMIDI)
		#MIDI_PORT.callback = mapMIDI
		print MIDI_PORT
 
# MIDI mappings
def mapMIDI(msg):
	print msg
	if msg.type == "note_on":
		mapping_l = MIDI_note_mapping[msg.note]	
		if mapping_l:
			mapping_l[0](msg, mapping_l[1])
			#fpgaParams = mapping_l[0](msg, mapping_l[1])
			#print "fpgaParams",fpgaParams
			#duplexPort.send(fpgaParams[0],fpgaParams[1])
	if msg.type == "control_change":
		mapping_l = MIDI_CC_mapping[msg.control]
		if mapping_l:
			mapping_l[0](msg, mapping_l[1])
			#fpgaParams = mapping_l[0](msg, mapping_l[1])
			#print "fpgaParams",fpgaParams
			#duplexPort.send(fpgaParams[0],fpgaParams[1])
	if msg.type == "note_off" and msg.note == 103:
		print "asdf"
		mapping_l = MIDI_note_mapping[msg.note]
		print mapping_l
		if mapping_l:	
			mapping_l[0](msg, mapping_l[1])
# signal functions
mido_init()

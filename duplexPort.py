"""
the job on the client side:

create duplex parallel ports
run test of i/o comms w/ Mojo

# deliver local IP and hostname to server via multicast
# listen for messages

"""

import time
import threading
import RPi.GPIO as GPIO

"""
Duplex Ports class handles communication with Mojo FPGA
There are two ports, in and out.

init() receives 
setModuleMap() connects module names in the Pi to module numbers in the Mojo
setCallback() sets callback function for incoming data
send(moduleName,Value) places name/value pairs in the send queue
"""

TIMING = 0.1
PINS_IN = [3,5,7,29,31,26,24,21,19,23,32,33]
PINS_OUT = [8,10,36,11,12,35,38,40,15,16,18,22]
moduleMap_d = False
recvCallback = False
inport = False
#outport = False

def init(mm_d, rc_f):
    global moduleMap_d
    global recvCallback_f
    GPIO.setmode(GPIO.BOARD)
    for pin in PINS_OUT:
        GPIO.setup(pin,GPIO.OUT)
    for pin in PINS_IN:
        GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    moduleMap_d = mm_d
    recvCallback_f = rc_f
    inport = InPort()
    inport.start()
    #outport = OutPort()
    #outport.start()

"""
outport_lock = threading.Event()
class OutPort(threading.thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
"""

inport_lock = threading.Event()
class InPort(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = []
    def run(self):
        last = 0
        while True:
            GPIO.wait_for_edge(3, GPIO.RISING)
            print "rising"
            print read()
            GPIO.wait_for_edge(3, GPIO.FALLING)
            print read()
            print "falling"
        pass

def read():
    pinValues = []
    for i in range(12):
        pin = PINS_IN[i]
        pinValue = GPIO.input(pin)
        pinValues.append(str(pinValue))
    return pinValues

def send(module, value):
    # to do : evaluate using bitwise operations to make this faster?
    if moduleMap_d == False:
        print "You must run init() before using this module"
        return False
    # make with the bit stuffing
    module_bin_str = dec2bin(module, 6)
    value_bin_str = dec2bin(value, 16)
    word1_str = value_bin_str[11:16] + module_bin_str + "0"
    word2_str = value_bin_str[0:11] + "1"
    for i in range(12):
        pin = PINS_OUT[i]
        val = int(word1_str[i])
        #print pin, val
        GPIO.output(pin,val)
    time.sleep(.001)
    for i in range(12):
        pin = PINS_OUT[i]
        val = int(word2_str[i])
        #print pin, val
        GPIO.output(pin,val)
        #print int(word2_str[11-i]), PINS_OUT[11-i]
    print module_bin_str, value_bin_str
    print word1_str, word2_str
    print
    time.sleep(.001)

def dec2bin(n, fill):
  bStr = ''
  while n > 0:
    bStr = str(n % 2) + bStr
    n = n >> 1
  return bStr.zfill(fill)

def testCallback(msg_l):
    print "testCallback:", msg_l

def testHarness():
    moduleMap = {"echo", 0}
    init(moduleMap, testCallback)
    for i in range(65534):
        send(0,i)
        #p = read()
        #print str(p)
        time.sleep(.1) 
    send(0,0)

testHarness()

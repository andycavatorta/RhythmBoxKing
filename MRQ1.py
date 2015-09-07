volume = 0 # range 0-127
externalClock0 = 0 # range 1-127
externalClock1 = 0 # range 1-127
externalClock2 = 0 # range 1-127
power = 0 # range 0-1

def setClockOscillator(msg,modifier):
	global externalClock0, externalClock1, externalClock2
	fpgaModuleId = 10
	if modifier == 0: # coarse
		v = msg.value / 4
		externalClock0 = v << 11
	if modifier == 1: # middle 
		v = msg.value / 4
		externalClock1 = v << 6
	if modifier == 2: # fine
		externalClock2 = msg.value / 2
	fpgaValue = externalClock0 + externalClock1 + externalClock2
	print fpgaValue
	return [fpgaModuleId,fpgaValue]

def triggerSnare(msg,modifier):
	fpgaModuleId = 20
	fpgaValue = 0 #msg.velocity * 255
	return [fpgaModuleId,fpgaValue]

def triggerBongo(msg,modifier):
	fpgaModuleId = 21
	fpgaValue = 0 #msg.velocity * 255
	return [fpgaModuleId,fpgaValue]

def triggerBlock(msg,modifier):
	fpgaModuleId = 22
	fpgaValue = 0 #msg.velocity * 255
	return [fpgaModuleId,fpgaValue]

def triggerBass(msg,modifier):
	fpgaModuleId = 23
	fpgaValue = 0 #msg.velocity * 255
	return [fpgaModuleId,fpgaValue]

def triggerBrush(msg,modifier):
	fpgaModuleId = 24
	fpgaValue = 0 #msg.velocity * 255
	return [fpgaModuleId,fpgaValue]

def setVolume(msg,modifier):
	global volume
	fpgaModuleId = 40
	fpgaValue = msg.value << 9
	return [fpgaModuleId,fpgaValue]

def setBalance(msg,modifier):
	global volume
	fpgaModuleId = 41
	fpgaValue = msg.value << 9
	return [fpgaModuleId,fpgaValue]

def toggleExternalClock(msg,modifier):
	if msg.type != "note_on":
		return None
	global externalClock
	externalClock = 0 if externalClock==1 else 1
	fpgaModuleId = 30
	return [fpgaModuleId,externalClock]

def togglePower(msg,modifier):
	if msg.type != "note_on":
		return None
	global power
	power = 0 if power==1 else 1
	fpgaModuleId = 31
	return [fpgaModuleId,power]


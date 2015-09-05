volume = 0 # range 0-127
externalClock = 0 # range 0-1
power = 0 # range 0-1

def setClockOscillator(msg,modifier):
	if msg.type == ""
	fpgaModuleId = 10

def triggerSnare(msg,modifier):
	if msg.type != "note_on":
		return None
	fpgaModuleId = 20
	fpgaValue = msg.velocity * 255
	return [fpgaModuleId,fpgaValue]

def triggerBongo(msg,modifier):
	if msg.type != "note_on":
		return None
	fpgaModuleId = 21
	fpgaValue = msg.velocity * 255
	return [fpgaModuleId,fpgaValue]

def triggerBlock(msg,modifier):
	if msg.type != "note_on":
		return None
	fpgaModuleId = 22
	fpgaValue = msg.velocity * 255
	return [fpgaModuleId,fpgaValue]

def triggerBass(msg,modifier):
	if msg.type != "note_on":
		return None
	fpgaModuleId = 23
	fpgaValue = msg.velocity * 255
	return [fpgaModuleId,fpgaValue]

def triggerBrush(msg,modifier):
	if msg.type != "note_on":
		return None
	fpgaModuleId = 24
	fpgaValue = msg.velocity * 255
	return [fpgaModuleId,fpgaValue]

def setVolume(msg,modifier):
	if msg.type != "note_on":
		return None
	global volume
	fpgaModuleId = 40
	if modifier == 0: # down
		if volume > 0:
			volume += volume
	else:
		if volume <= 127:
			volume -= volume
	fpgaValue = volume * 255
	return [fpgaModuleId,fpgaValue]

def setBalance(msg,modifier):
	if msg.type != "note_on":
		return None
	global volume
	fpgaModuleId = 41
	if modifier == 0: # down
		if volume > 0:
			volume += volume
	else:
		if volume <= 127:
			volume -= volume
	fpgaValue = volume * 255
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


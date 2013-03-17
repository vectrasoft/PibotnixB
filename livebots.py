import time
import urllib2
import os
import serial

ser = serial.Serial('/dev/ttyAMA0', 2400, timeout=1)

cfnt = 1

while True:
	try:
		req = urllib2.Request('http://livebots.cc/Robot/Message/30.html')
		response = urllib2.urlopen(req)
		html = response.read()
		html=html.strip()
		html=html.rstrip()
		html=html.lstrip()
		message = str(html).lower()
		if message != lastMessage:
			print message
			if "look left" in message:
				os.system('echo "5=0.2" > /dev/pi-blaster')
				cfnt = 0
			elif "look forward" in message:
				os.system('echo "5=0.15" > /dev/pi-blaster')
				cfnt = 1
			elif "look right" in message:
				os.system('echo "5=0.1" > /dev/pi-blaster')
				cfnt = 0
			elif "forward" in message:
				if cfnt == 1:
					os.system('echo "7=0.2" > /dev/pi-blaster')
					os.system('echo "6=0.1" > /dev/pi-blaster')
				else:
					os.system('echo "5=0.15" > /dev/pi-blaster')
					os.system('echo "7=0.2" > /dev/pi-blaster')
					os.system('echo "6=0.1" > /dev/pi-blaster')
			elif "backward" in message:
				if cfnt == 1:
					os.system('echo "7=0.1" > /dev/pi-blaster')
					os.system('echo "6=0.2" > /dev/pi-blaster')
				else:
					os.system('echo "5=0.15" > /dev/pi-blaster')
					os.system('echo "7=0.1" > /dev/pi-blaster')
					os.system('echo "6=0.1" > /dev/pi-blaster')
			elif "left" in message:
				os.system('echo "7=0.1" > /dev/pi-blaster')
				os.system('echo "6=0.1" > /dev/pi-blaster')
			elif "right" in message:
				os.system('echo "7=0.2" > /dev/pi-blaster')
				os.system('echo "6=0.2" > /dev/pi-blaster')
			lastMessage = message
	except:
		a = 1 + 1
	lastMessage = message
	time.sleep(0.25)
	os.system('echo "7=0" > /dev/pi-blaster')
	os.system('echo "6=0" > /dev/pi-blaster')
	string = ser.read(12)
	if len(string) == 0:
		if os.path.isfile("points"):
			os.system('rm points')
			print "Removed Points"
	else:
		print "Points Found"
		string = string[1:11]
		a = open("points","w")
		if string == "0F03037647":
			a.write("100")
		elif string == "360061AE83":
			a.write("50")
		elif string == "360074F230":
			a.write("150")
		elif string == "0F03041D8F":
			a.write("200")
		elif string == "46007177AA":
			a.write("150")
		elif string == "3B0032B8A5":
			a.write("50")
		a.close()
		ser.flush()

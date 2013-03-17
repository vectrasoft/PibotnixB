import curses
import os
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,0,"Up = Forward    Down = Backward    Left = Left    Right = Right")
stdscr.addstr(1,0,"Backspace = Stop and q to Quit")
stdscr.refresh()

key = ''
front = 1

while key != ord('q'):
    key = stdscr.getch()
#    stdscr.addch(20,25,key)
    stdscr.refresh()

    ### FORWARD CODE ###
    if key == curses.KEY_UP:
	if front == 1:
        	stdscr.addstr(2, 2, "Forward       ")
		os.system('echo "7=0.2" > /dev/pi-blaster')
		os.system('echo "6=0.1" > /dev/pi-blaster')
	else:
		stdscr.addstr(2, 2, "CAM FORWARD!")
    ### BACKWARD CODE ###
    elif key == curses.KEY_DOWN:
	if front == 1:
        	stdscr.addstr(2, 2, "Backward      ")
		os.system('echo "7=0.1" > /dev/pi-blaster')
		os.system('echo "6=0.2" > /dev/pi-blaster')
	else:
		stdscr.addstr(2, 2, "CAM FORWARD!")
    ### LEFT CODE ####
    elif key == curses.KEY_LEFT:
	if front == 1:
		stdscr.addstr(2, 2, "Left          ")
		os.system('echo "7=0.1" > /dev/pi-blaster')
		os.system('echo "6=0.1" > /dev/pi-blaster')
	else:
		stdscr.addstr(2, 2, "CAM FORWARD!")
    ### RIGHT CODE ###
    elif key == curses.KEY_RIGHT:
	if front == 1:
		stdscr.addstr(2, 2, "Right         ")
		os.system('echo "7=0.2" > /dev/pi-blaster')
		os.system('echo "6=0.2" > /dev/pi-blaster')
	else:
		stdscr.addstr(2, 2, "CAM FORWARD!")
    ### STOP CODE ###
    elif key == curses.KEY_BACKSPACE:
	stdscr.addstr(2, 2, "Stop          ")
	os.system('echo "7=0" > /dev/pi-blaster')
	os.system('echo "6=0" > /dev/pi-blaster')
    ### CAMERA LEFT ###
    elif key == curses.KEY_F1:
	stdscr.addstr(2, 2, "Look Left     ")
	os.system('echo "5=0.2" > /dev/pi-blaster')
	front = 0
    ### CAMERA FORWARD ###
    elif key == curses.KEY_F2:
	stdscr.addstr(2, 2, "Look Forward  ")
	os.system('echo "5=0.15" > /dev/pi-blaster')
	front = 1
    ### CAMERA RIGHT ###
    elif key == curses.KEY_F3:
	stdscr.addstr(2, 2, "Look Right    ")
	os.system('echo "5=0.1" > /dev/pi-blaster')
	front = 0

curses.endwin()


import curses
import os
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,0,"Up = Forward    Down = Backward    Left = Left    Right = Right")
stdscr.addstr(1,0,"Backspace = Stop and q to Quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
#    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP: 
        stdscr.addstr(2, 2, "Forward ")
	os.system('echo "7=0.2" > /dev/pi-blaster')
	os.system('echo "6=0.1" > /dev/pi-blaster')
    elif key == curses.KEY_DOWN: 
        stdscr.addstr(2, 2, "Backward")
	os.system('echo "7=0.1" > /dev/pi-blaster')
	os.system('echo "6=0.2" > /dev/pi-blaster')
    elif key == curses.KEY_LEFT:
	stdscr.addstr(2, 2, "Left    ")
	os.system('echo "7=0.1" > /dev/pi-blaster')
	os.system('echo "6=0.1" > /dev/pi-blaster')
    elif key == curses.KEY_RIGHT:
	stdscr.addstr(2, 2, "Right   ")
	os.system('echo "7=0.2" > /dev/pi-blaster')
	os.system('echo "6=0.2" > /dev/pi-blaster')
    elif key == curses.KEY_BACKSPACE:
	stdscr.addstr(2, 2, "Stop    ")
	os.system('echo "7=0" > /dev/pi-blaster')
	os.system('echo "6=0" > /dev/pi-blaster')

curses.endwin()


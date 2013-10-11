#!/usr/bin/env python

from os import system
import curses

def get_param(prompt_string):
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input

def execute_cmd(cmd_string):
    system("clear")
    a = system(cmd_string)
    print ""
    if a == 0:
        print "Command executed correctly"
    else:
        print "Command terminated with error"
    raw_input("Press enter")
    print ""

x = 0

while x != ord('5'):
    screen = curses.initscr()

    screen.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    screen.border(0)
    screen.addstr(2, 2, "Chose an option:")
    screen.addstr(4, 4, "1 - Start Security Service")
    screen.addstr(5, 4, "2 - Show Security Log")
    screen.addstr(6, 4, "3 - Show disk space")
    screen.addstr(7, 4, "4 - Run top")
    screen.addstr(8, 4, "5 - Exit")
    screen.refresh()

    x = screen.getch()

    if x == ord('1'):
        curses.endwin()
        execute_cmd("python security.py &")
    if x == ord('2'):
        curses.endwin()
        execute_cmd("less /var/log/security.log")
    if x == ord('3'):
        curses.endwin()
        execute_cmd("df -h")
    if x == ord('4'):
        curses.endwin()
        execute_cmd("top")

curses.endwin()

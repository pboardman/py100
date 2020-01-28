import sys
import os
import re
import termios
import tty
import time
from io import StringIO

escape = chr(27)

########
# Screen clearing
########


def clear_screen():
    """Clear entire screen"""
    print(escape + '[2J', end='')


########
# Cursor movement/position
########


def move_cursor_up(nb_line):
    """Move cursor up n lines"""
    print(escape + f'[{nb_line}A', end='')


def move_cursor_down(nb_line):
    """Move cursor down n lines"""
    print(escape + f'[{nb_line}B', end='')


def move_cursor_right(nb_line):
    """Move cursor right n lines"""
    print(escape + f'[{nb_line}C', end='')


def move_cursor_left(nb_line):
    """Move cursor left n lines"""
    print(escape + f'[{nb_line}D', end='')


def move_cursor_upper_left():
    """Move cursor to upper left corner"""
    print(escape + '[H', end='')


def move_cursor_to_location(hpos, vpos):
    """Move cursor to upper left corner"""
    print(escape + f'[{vpos};{hpos}H', end='')


def move_to_next_line():
    """Move to next line"""
    print(escape + 'E', end='')


def save_cursor_position():
    """Save cursor position and attributes"""
    print(escape + '7', end='')


def restore_cursor_position():
    """Restore cursor position and attributes"""
    print(escape + '8', end='')


def get_cursor_position():
    """Get cursor position as a tuple (x, y)"""

    buf = ""
    stdin = sys.stdin.fileno()
    tattr = termios.tcgetattr(stdin)

    try:
        tty.setcbreak(stdin, termios.TCSANOW)
        sys.stdout.write(escape + '[6n')
        sys.stdout.flush()

        while True:
            buf += sys.stdin.read(1)
            if buf[-1] == 'R':
                break

    finally:
        termios.tcsetattr(stdin, termios.TCSANOW, tattr)

    matches = re.match(r"^\x1b\[(\d*);(\d*)R", buf)
    groups = matches.groups()

    return (int(groups[1]), int(groups[0]))


########
# Terminal settings
########


def set_columns_to_132():
    """Set number of columns to 132"""
    print(escape + '[?3h', end='')


def set_smooth_scrolling():
    """Set smooth scrolling"""
    print(escape + '[?4h', end='')


def set_reverse_video_on_screen():
    """Set reverse video on screen"""
    print(escape + '[?5h', end='')


def set_normal_video_on_screen():
    """Set normal video on screen"""
    print(escape + '[?5l', end='')


def set_origin_relative():
    """Set origin to relative"""
    print(escape + '[?6h', end='')


def set_origin_absolute():
    """Set origin to absolute"""
    print(escape + '[?6l', end='')


def set_auto_wrap_mode():
    """Set auto-wrap mode"""
    print(escape + '[?7h', end='')


def reset_auto_wrap_mode():
    """Reset auto-wrap mode"""
    print(escape + '[?7l', end='')
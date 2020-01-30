import sys
import os
import re
import termios
import tty
import time
from io import StringIO

escape = chr(27)

########
# Screen
########


def clear_screen():
    """Clear entire screen"""
    print(escape + '[2J', end='')


def scroll_window_up():
    """Move/scroll window up one line"""
    print(escape + 'D', end='')


def scroll_window_down():
    """Move/scroll window down one line"""
    print(escape + 'M', end='')


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


def set_columns_to_80():
    """Set number of columns to 80"""
    print(escape + '[?3l', end='')


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


def set_auto_repeat_mode():
    """Set auto-repeat mode"""
    print(escape + '[?8h', end='')


def reset_auto_repeat_mode():
    """Reset auto-repeat mode"""
    print(escape + '[?8l', end='')


def set_interlacing_mode():
    """Set interlacing mode"""
    print(escape + '[?9h', end='')


def reset_interlacing_mode():
    """Reset interlacing mode"""
    print(escape + '[?9l', end='')


def set_line_feed_mode():
    """Set line feed mode"""
    print(escape + '[?20l', end='')


def set_cursor_to_key_mode():
    """Set cursor key to cursor"""
    print(escape + '[?1l', end='')


########
# Characters settings
########


def turn_off_characters_attributes():
    """Turn off character attributes"""
    print(escape + '[m', end='')


def turn_bold_mode_on():
    """Turn bold mode on"""
    print(escape + '[1m', end='')


def turn_low_intensity_mode_on():
    """Turn low intensity mode on"""
    print(escape + '[2m', end='')


def turn_underline_mode_on():
    """Turn underline mode on"""
    print(escape + '[4m', end='')


def turn_blinking_mode_on():
    """Turn blinking mode on"""
    print(escape + '[5m', end='')


def turn_reverse_video_mode_on():
    """Turn reverse video on"""
    print(escape + '[7m', end='')


def turn_invisible_text_mode_on():
    """Turn invisible text mode on"""
    print(escape + '[8m', end='')
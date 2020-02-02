import sys
import os
import re
import termios
import tty
import time
from io import StringIO

escape = chr(27)

########
# Screen clearing and movement
########


def clear_screen():
    """Clear entire screen"""
    print(escape + '[2J', end='')


def clear_line_from_cursor_right():
    """Clear line from cursor right"""
    print(escape + '[K', end='')


def clear_line_from_cursor_left():
    """Clear line from cursor left"""
    print(escape + '[1K', end='')


def clear_line_from_cursor_down():
    """Clear line from cursor down"""
    print(escape + '[J', end='')


def clear_line_from_cursor_up():
    """Clear line from cursor up"""
    print(escape + '[1J', end='')


def clear_entire_line():
    """Clear entire line"""
    print(escape + '[2K', end='')


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


def set_cursor_key_to_application():
    """Set cursor key to application"""
    print(escape + '[?1h', end='')


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


def set_new_line_mode():
    """Set new line mode"""
    print(escape + '[20h', end='')


def set_vt52():
    """Set VT52 (versus ANSI)"""
    print(escape + '[?2l', end='')


def set_jump_scrolling():
    """Set jump scrolling"""
    print(escape + '[?4l', end='')


def set_top_and_bottom_lines_of_a_window(top_line, bottom_line):
    """Set top and bottom lines of a window"""
    print(escape + f'[{top_line};{bottom_line}r', end='')


def reset_terminal_to_initial_state():
    """Reset terminal to initial state"""
    print(escape + 'c', end='')


########
# Characters settings
########


def set_united_kingdom_g0_character_set():
    """Set United Kingdom G0 character set"""
    print(escape + '(A', end='')


def set_united_kingdom_g1_character_set():
    """Set United Kingdom G1 character set"""
    print(escape + ')A', end='')


def set_united_states_g0_character_set():
    """Set United States G0 character set"""
    print(escape + '(B', end='')


def set_united_states_g1_character_set():
    """Set United States G1 character set"""
    print(escape + ')B', end='')


def set_g0_special_chars_and_line_set():
    """Set G0 special chars. & line set"""
    print(escape + '(0', end='')


def set_g1_special_chars_and_line_set():
    """Set G1 special chars. & line set"""
    print(escape + ')0', end='')


def set_g0_alternate_character_rom():
    """Set G0 alternate character ROM"""
    print(escape + '(1', end='')


def set_g1_alternate_character_rom():
    """Set G1 alternate character ROM"""
    print(escape + ')1', end='')


def set_g0_alt_char_rom_and_spec_graphics():
    """Set G0 alt char ROM and spec. graphics"""
    print(escape + '(2', end='')


def set_g1_alt_char_rom_and_spec_graphics():
    """Set G1 alt char ROM and spec. graphics"""
    print(escape + ')2', end='')


def set_single_shift_2():
    """Set single shift 2"""
    print(escape + 'N', end='')


def set_single_shift_3():
    """Set single shift 3"""
    print(escape + 'O', end='')


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


def double_height_letters_top_half():
    """Double-height letters, top half"""
    print(escape + '#3', end='')


def double_height_letters_bottom_half():
    """Double-height letters, bottom half"""
    print(escape + '#4', end='')


def single_width_single_height_letters():
    """Single width, single height letters"""
    print(escape + '#5', end='')


def double_width_single_height_letters():
    """Double width, single height letters"""
    print(escape + '#6', end='')


########
# Keypad settings
########


def set_alternate_keypad_mode():
    """Set alternate keypad mode"""
    print(escape + '=', end='')


def set_numeric_keypad_mode():
    """Set numeric keypad mode"""
    print(escape + '>', end='')


########
# Tabs
########


def set_a_tab_at_the_current_column():
    """Set a tab at the current column"""
    print(escape + 'H', end='')


def clear_a_tab_at_the_current_column():
    """Clear a tab at the current column"""
    print(escape + '[g', end='')


def clear_all_tabs():
    """Clear all tabs"""
    print(escape + '[3g', end='')


########
# Display settings
########


def screen_alignment_display():
    """Screen alignment display"""
    print(escape + '#8', end='')


########
# LEDS
########


def turn_off_all_four_leds():
    """Turn off all four leds"""
    print(escape + '[0q', end='')


def turn_on_led_1():
    """Turn on LED #1"""
    print(escape + '[1q', end='')


def turn_on_led_2():
    """Turn on LED #2"""
    print(escape + '[2q', end='')


def turn_on_led_3():
    """Turn on LED #3"""
    print(escape + '[3q', end='')


def turn_on_led_4():
    """Turn on LED #4"""
    print(escape + '[4q', end='')

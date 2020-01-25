########
# Screen clearing
########
def clear_screen():
    """Clear entire screen"""
    print(chr(27) + '[2J')


########
# Cursor movement
########
def move_cursor_up(nb_line):
    """Move cursor up n lines"""
    print(chr(27) + f'[{nb_line}A', end='')


def move_cursor_down(nb_line):
    """Move cursor down n lines"""
    print(chr(27) + f'[{nb_line}B', end='')


def move_cursor_right(nb_line):
    """Move cursor right n lines"""
    print(chr(27) + f'[{nb_line}C', end='')


def move_cursor_left(nb_line):
    """Move cursor left n lines"""
    print(chr(27) + f'[{nb_line}D', end='')


def move_cursor_upper_left():
    """Move cursor to upper left corner"""
    print(chr(27) + '[H', end='')


def move_cursor_to_location(vpos, hpos):
    """Move cursor to upper left corner"""
    print(chr(27) + f'[{vpos};{hpos}H', end='')


def move_to_next_line():
    """Move to next line"""
    print(chr(27) + 'E', end='')


def save_cursor_position():
    """Save cursor position and attributes"""
    print(chr(27) + '7', end='')


def restore_cursor_position():
    """Restore cursor position and attributes"""
    print(chr(27) + '8', end='')
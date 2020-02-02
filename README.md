# py100

python wrapper for VT100 escape sequences, which are supported by most modern terminals (on linux at least).

## Installation

`git clone https://github.com/pboardman/py100`

`cd py100`

`python3 setup.py install --user`

## Usage

`from py100 import py100`

`py100.some_function_from_the_table_below()`

## Progress

This is the list of what is currently supported and what should be supported in the future. If a sequence isn't marked as planned it may just mean I didn't have a look at it yet.

| Sequence | Description | Name | Supported | Planned | Function |
|----------|-------------|------|-----------|---------|----------|
|Esc[20h |Set new line mode |LMN|:heavy_check_mark:|:heavy_check_mark:|set_new_line_mode()|
|Esc[?1h |Set cursor key to application |DECCKM|:heavy_check_mark:|:heavy_check_mark:|set_cursor_key_to_application()|
|Esc[?3h |Set number of columns to 132 |DECCOLM|:heavy_check_mark:|:heavy_check_mark:|set_columns_to_132()|
|Esc[?4h |Set smooth scrolling |DECSCLM|:heavy_check_mark:|:heavy_check_mark:|set_smooth_scrolling()|
|Esc[?5h |Set reverse video on screen |DECSCNM|:heavy_check_mark:|:heavy_check_mark:|set_reverse_video_on_screen()|
|Esc[?6h |Set origin to relative |DECOM|:heavy_check_mark:|:heavy_check_mark:|set_origin_relative()|
|Esc[?7h |Set auto-wrap mode |DECAWM|:heavy_check_mark:|:heavy_check_mark:|set_auto_wrap_mode()|
|Esc[?8h |Set auto-repeat mode |DECARM|:heavy_check_mark:|:heavy_check_mark:|set_auto_repeat_mode()|
|Esc[?9h |Set interlacing mode |DECINLM|:heavy_check_mark:|:heavy_check_mark:|set_interlacing_mode()|
|Esc[20l |Set line feed mode |LMN|:heavy_check_mark:|:heavy_check_mark:|set_line_feed_mode()|
|Esc[?1l |Set cursor key to cursor |DECCKM|:heavy_check_mark:|:heavy_check_mark:|set_cursor_to_key_mode()|
|Esc[?2l |Set VT52 (versus ANSI) |DECANM|:heavy_check_mark:|:heavy_check_mark:|set_vt52()|
|Esc[?3l |Set number of columns to 80 |DECCOLM|:heavy_check_mark:|:heavy_check_mark:|set_columns_to_80()|
|Esc[?4l |Set jump scrolling |DECSCLM|:heavy_check_mark:|:heavy_check_mark:|set_jump_scrolling()|
|Esc[?5l |Set normal video on screen |DECSCNM|:heavy_check_mark:|:heavy_check_mark:|set_normal_video_on_screen()|
|Esc[?6l |Set origin to absolute |DECOM|:heavy_check_mark:|:heavy_check_mark:|set_origin_absolute()|
|Esc[?7l |Reset auto-wrap mode |DECAWM|:heavy_check_mark:|:heavy_check_mark:|reset_auto_wrap_mode()|
|Esc[?8l |Reset auto-repeat mode |DECARM|:heavy_check_mark:|:heavy_check_mark:|reset_auto_repeat_mode()|
|Esc[?9l |Reset interlacing mode |DECINLM|:heavy_check_mark:|:heavy_check_mark:|reset_interlacing_mode()|
|Esc= |Set alternate keypad mode |DECKPAM|:heavy_check_mark:|:heavy_check_mark:|set_alternate_keypad_mode()|
|Esc> |Set numeric keypad mode |DECKPNM|:heavy_check_mark:|:heavy_check_mark:|set_numeric_keypad_mode()|
|Esc(A |Set United Kingdom G0 character set |setukg0|:heavy_check_mark:|:heavy_check_mark:|set_united_kingdom_g0_character_set()|
|Esc)A |Set United Kingdom G1 character set |setukg1|:heavy_check_mark:|:heavy_check_mark:|set_united_kingdom_g1_character_set()|
|Esc(B |Set United States G0 character set |setusg0|:heavy_check_mark:|:heavy_check_mark:|set_united_states_g0_character_set()|
|Esc)B |Set United States G1 character set |setusg1|:heavy_check_mark:|:heavy_check_mark:|set_united_states_g1_character_set()|
|Esc(0 |Set G0 special chars. & line set |setspecg0|:heavy_check_mark:|:heavy_check_mark:|set_g0_special_chars_and_line_set()|
|Esc)0 |Set G1 special chars. & line set |setspecg1|:heavy_check_mark:|:heavy_check_mark:|set_g1_special_chars_and_line_set()|
|Esc(1 |Set G0 alternate character ROM |setaltg0|:heavy_check_mark:|:heavy_check_mark:|set_g0_alternate_character_rom()|
|Esc)1 |Set G1 alternate character ROM |setaltg1|:heavy_check_mark:|:heavy_check_mark:|set_g1_alternate_character_rom()|
|Esc(2 |Set G0 alt char ROM and spec. graphics |setaltspecg0|:heavy_check_mark:|:heavy_check_mark:|set_g0_alt_char_rom_and_spec_graphics()|
|Esc)2 |Set G1 alt char ROM and spec. graphics |setaltspecg1|:heavy_check_mark:|:heavy_check_mark:|set_g1_alt_char_rom_and_spec_graphics()|
|EscN |Set single shift 2 |SS2|:heavy_check_mark:|:heavy_check_mark:|set_single_shift_2()|
|EscO |Set single shift 3 |SS3|:heavy_check_mark:|:heavy_check_mark:|set_single_shift_3()|
|Esc[m |Turn off character attributes |SGR0|:heavy_check_mark:|:heavy_check_mark:|turn_off_characters_attributes()|
|Esc[0m |Turn off character attributes |SGR0|:heavy_check_mark:|:heavy_check_mark:|turn_off_characters_attributes()|
|Esc[1m |Turn bold mode on |SGR1|:heavy_check_mark:|:heavy_check_mark:|turn_bold_mode_on()|
|Esc[2m |Turn low intensity mode on |SGR2|:heavy_check_mark:|:heavy_check_mark:|turn_low_intensity_mode_on()|
|Esc[4m |Turn underline mode on |SGR4|:heavy_check_mark:|:heavy_check_mark:|turn_underline_mode_on()|
|Esc[5m |Turn blinking mode on |SGR5|:heavy_check_mark:|:heavy_check_mark:|turn_blinking_mode_on()|
|Esc[7m |Turn reverse video on |SGR7|:heavy_check_mark:|:heavy_check_mark:|turn_reverse_video_mode_on()|
|Esc[8m |Turn invisible text mode on |SGR8|:heavy_check_mark:|:heavy_check_mark:|turn_invisible_text_mode_on()|
|Esc[Line;Liner |Set top and bottom lines of a window |DECSTBM|:heavy_check_mark:|:heavy_check_mark:|set_top_and_bottom_lines_of_a_window(top_line, bottom_line)|
|Esc[ValueA |Move cursor up n lines |CUU|:heavy_check_mark:|:heavy_check_mark:|move_cursor_up()|
|Esc[ValueB |Move cursor down n lines |CUD|:heavy_check_mark:|:heavy_check_mark:|move_cursor_down()|
|Esc[ValueC |Move cursor right n lines |CUF|:heavy_check_mark:|:heavy_check_mark:|move_cursor_right()|
|Esc[ValueD |Move cursor left n lines |CUB|:heavy_check_mark:|:heavy_check_mark:|move_cursor_left()|
|Esc[H |Move cursor to upper left corner |cursorhome|:heavy_check_mark:|:heavy_check_mark:|move_cursor_upper_left()|
|Esc[;H |Move cursor to upper left corner |cursorhome|:heavy_check_mark:|:heavy_check_mark:|move_cursor_upper_left()|
|Esc[Line;ColumnH |Move cursor to screen location v,h |CUP|:heavy_check_mark:|:heavy_check_mark:|move_cursor_to_location()|
|Esc[f |Move cursor to upper left corner |hvhome|:heavy_check_mark:|:heavy_check_mark:|move_cursor_upper_left()|
|Esc[;f |Move cursor to upper left corner |hvhome|:heavy_check_mark:|:heavy_check_mark:|move_cursor_upper_left()|
|Esc[Line;Columnf |Move cursor to screen location v,h |CUP|:heavy_check_mark:|:heavy_check_mark:|move_cursor_to_location()|
|EscD |Move/scroll window up one line |IND|:heavy_check_mark:|:heavy_check_mark:|scroll_window_up()|
|EscM |Move/scroll window down one line |RI|:heavy_check_mark:|:heavy_check_mark:|scroll_window_down()|
|EscE |Move to next line |NEL|:heavy_check_mark:|:heavy_check_mark:|move_to_next_line()|
|Esc7 |Save cursor position and attributes |DECSC|:heavy_check_mark:|:heavy_check_mark:|save_cursor_position()|
|Esc8 |Restore cursor position and attributes |DECSC|:heavy_check_mark:|:heavy_check_mark:|restore_cursor_position()|
|EscH |Set a tab at the current column |HTS|:heavy_check_mark:|:heavy_check_mark:|set_a_tab_at_the_current_column()|
|Esc[g |Clear a tab at the current column |TBC|:heavy_check_mark:|:heavy_check_mark:|clear_a_tab_at_the_current_column()|
|Esc[0g |Clear a tab at the current column |TBC|:heavy_check_mark:|:heavy_check_mark:|clear_a_tab_at_the_current_column()|
|Esc[3g |Clear all tabs |TBC|:heavy_check_mark:|:heavy_check_mark:|clear_all_tabs()|
|Esc#3 |Double-height letters, top half |DECDHL|heavy_check_mark:|heavy_check_mark:|double_height_letters_top_half()|
|Esc#4 |Double-height letters, bottom half |DECDHL|:heavy_check_mark:|:heavy_check_mark:|double_height_letters_bottom_half()|
|Esc#5 |Single width, single height letters |DECSWL|:heavy_check_mark:|:heavy_check_mark:|single_width_single_height_letters()|
|Esc#6 |Double width, single height letters |DECDWL|:heavy_check_mark:|:heavy_check_mark:|double_width_single_height_letters()|
|Esc[K |Clear line from cursor right |EL0|:heavy_check_mark:|:heavy_check_mark:|clear_line_from_cursor_right()|
|Esc[0K |Clear line from cursor right |EL0|:heavy_check_mark:|:heavy_check_mark:|clear_line_from_cursor_right()|
|Esc[1K |Clear line from cursor left |EL1|:heavy_check_mark:|:heavy_check_mark:|clear_line_from_cursor_left()|
|Esc[2K |Clear entire line |EL2|:heavy_check_mark:|:heavy_check_mark:|clear_entire_line()|
|Esc[J |Clear screen from cursor down |ED0|:heavy_check_mark:|:heavy_check_mark:|clear_line_from_cursor_down()|
|Esc[0J |Clear screen from cursor down |ED0|:heavy_check_mark:|:heavy_check_mark:|clear_line_from_cursor_down()|
|Esc[1J |Clear screen from cursor up |ED1|:heavy_check_mark:|:heavy_check_mark:|clear_line_from_cursor_up()|
|Esc[2J |Clear entire screen |ED2|:heavy_check_mark:|:heavy_check_mark:|clear_screen()|
|Esc5n |Device status report |DSR||:heavy_check_mark:||
|Esc0n |Response: terminal is OK |DSR||:heavy_check_mark:||
|Esc3n |Response: terminal is not OK |DSR||:heavy_check_mark:||
|Esc6n |Get cursor position |DSR|:heavy_check_mark:|:heavy_check_mark:|get_cursor_position()|
|EscLine;ColumnR |Response: cursor is at v,h |CPR|:heavy_check_mark:|:heavy_check_mark:|get_cursor_position()|
|Esc[c |Identify what terminal type |DA||:heavy_check_mark:||
|Esc[0c |Identify what terminal type (another) |DA||:heavy_check_mark:||
|Esc[?1;Value0c |Response: terminal type code n |DA||heavy_check_mark:||
|Escc |Reset terminal to initial state |RIS|:heavy_check_mark:|:heavy_check_mark:|reset_terminal_to_initial_state()|
|Esc#8 |Screen alignment display |DECALN|:heavy_check_mark:|:heavy_check_mark:|screen_alignment_display()|
|Esc[2;1y |Confidence power up test |DECTST||||
|Esc[2;2y |Confidence loopback test |DECTST||||
|Esc[2;9y |Repeat power up test |DECTST||||
|Esc[2;10y |Repeat loopback test |DECTST||||
|Esc[0q |Turn off all four leds |DECLL0|:heavy_check_mark:|:heavy_check_mark:|turn_off_all_four_leds()|
|Esc[1q |Turn on LED #1 |DECLL1|:heavy_check_mark:|:heavy_check_mark:|turn_on_led_1()|
|Esc[2q |Turn on LED #2 |DECLL2|:heavy_check_mark:|:heavy_check_mark:|turn_on_led_2()|
|Esc[3q |Turn on LED #3 |DECLL3|:heavy_check_mark:|:heavy_check_mark:|turn_on_led_3()|
|Esc[4q |Turn on LED #4 |DECLL4|:heavy_check_mark:|:heavy_check_mark:|turn_on_led_4()|

## Info on the VT100 escape sequences
Information on all the VT100 escape sequences can be found [here](http://ascii-table.com/ansi-escape-sequences-vt-100.php) (This is where my list comes from).

More information on the DEC Terminals can be found on [vt100.net](https://vt100.net).

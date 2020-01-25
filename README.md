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
|Esc[20h |Set new line mode |LMN||||
|Esc[?1h |Set cursor key to application |DECCKM||||
|none |Set ANSI (versus VT52) |DECANM||||
|Esc[?3h |Set number of columns to 132 |DECCOLM||:heavy_check_mark:||
|Esc[?4h |Set smooth scrolling |DECSCLM||||
|Esc[?5h |Set reverse video on screen |DECSCNM||||
|Esc[?6h |Set origin to relative |DECOM||||
|Esc[?7h |Set auto-wrap mode |DECAWM||||
|Esc[?8h |Set auto-repeat mode |DECARM||||
|Esc[?9h |Set interlacing mode |DECINLM||||
|Esc[20l |Set line feed mode |LMN||||
|Esc[?1l |Set cursor key to cursor |DECCKM||||
|Esc[?2l |Set VT52 (versus ANSI) |DECANM||||
|Esc[?3l |Set number of columns to 80 |DECCOLM||:heavy_check_mark:||
|Esc[?4l |Set jump scrolling |DECSCLM||||
|Esc[?5l |Set normal video on screen |DECSCNM||||
|Esc[?6l |Set origin to absolute |DECOM||||
|Esc[?7l |Reset auto-wrap mode |DECAWM||||
|Esc[?8l |Reset auto-repeat mode |DECARM||||
|Esc[?9l |Reset interlacing mode |DECINLM||||
|Esc= |Set alternate keypad mode |DECKPAM||||
|Esc> |Set numeric keypad mode |DECKPNM||||
|Esc(A |Set United Kingdom G0 character set |setukg0||||
|Esc)A |Set United Kingdom G1 character set |setukg1||||
|Esc(B |Set United States G0 character set |setusg0||||
|Esc)B |Set United States G1 character set |setusg1||||
|Esc(0 |Set G0 special chars. & line set |setspecg0||||
|Esc)0 |Set G1 special chars. & line set |setspecg1||||
|Esc(1 |Set G0 alternate character ROM |setaltg0||||
|Esc)1 |Set G1 alternate character ROM |setaltg1||||
|Esc(2 |Set G0 alt char ROM and spec. graphics |setaltspecg0||||
|Esc)2 |Set G1 alt char ROM and spec. graphics |setaltspecg1||||
|EscN |Set single shift 2 |SS2||||
|EscO |Set single shift 3 |SS3||||
|Esc[m |Turn off character attributes |SGR0||||
|Esc[0m |Turn off character attributes |SGR0||||
|Esc[1m |Turn bold mode on |SGR1||||
|Esc[2m |Turn low intensity mode on |SGR2||||
|Esc[4m |Turn underline mode on |SGR4||||
|Esc[5m |Turn blinking mode on |SGR5||||
|Esc[7m |Turn reverse video on |SGR7||||
|Esc[8m |Turn invisible text mode on |SGR8||||
|Esc[Line;Liner |Set top and bottom lines of a window |DECSTBM||||
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
|EscD |Move/scroll window up one line |IND||||
|EscM |Move/scroll window down one line |RI||||
|EscE |Move to next line |NEL|:heavy_check_mark:|:heavy_check_mark:|move_to_next_line()|
|Esc7 |Save cursor position and attributes |DECSC|:heavy_check_mark:|:heavy_check_mark:|save_cursor_position()|
|Esc8 |Restore cursor position and attributes |DECSC|:heavy_check_mark:|:heavy_check_mark:|restore_cursor_position()|
|EscH |Set a tab at the current column |HTS||||
|Esc[g |Clear a tab at the current column |TBC||||
|Esc[0g |Clear a tab at the current column |TBC||||
|Esc[3g |Clear all tabs |TBC||||
|Esc#3 |Double-height letters, top half |DECDHL||||
|Esc#4 |Double-height letters, bottom half |DECDHL||||
|Esc#5 |Single width, single height letters |DECSWL||||
|Esc#6 |Double width, single height letters |DECDWL||||
|Esc[K |Clear line from cursor right |EL0||:heavy_check_mark:||
|Esc[0K |Clear line from cursor right |EL0||:heavy_check_mark:||
|Esc[1K |Clear line from cursor left |EL1||:heavy_check_mark:||
|Esc[2K |Clear entire line |EL2||:heavy_check_mark:||
|Esc[J |Clear screen from cursor down |ED0||:heavy_check_mark:||
|Esc[0J |Clear screen from cursor down |ED0||:heavy_check_mark:||
|Esc[1J |Clear screen from cursor up |ED1||:heavy_check_mark:||
|Esc[2J |Clear entire screen |ED2|:heavy_check_mark:|:heavy_check_mark:|clear_screen()|
|Esc5n |Device status report |DSR||:heavy_check_mark:||
|Esc0n |Response: terminal is OK |DSR||||
|Esc3n |Response: terminal is not OK |DSR||||
|Esc6n |Get cursor position |DSR||:heavy_check_mark:||
|EscLine;ColumnR |Response: cursor is at v,h |CPR||||
|Esc[c |Identify what terminal type |DA||:heavy_check_mark:||
|Esc[0c |Identify what terminal type (another) |DA||:heavy_check_mark:||
|Esc[?1;Value0c |Response: terminal type code n |DA||||
|Escc |Reset terminal to initial state |RIS||:heavy_check_mark:||
|Esc#8 |Screen alignment display |DECALN||||
|Esc[2;1y |Confidence power up test |DECTST||||
|Esc[2;2y |Confidence loopback test |DECTST||||
|Esc[2;9y |Repeat power up test |DECTST||||
|Esc[2;10y |Repeat loopback test |DECTST||||
|Esc[0q |Turn off all four leds |DECLL0||||
|Esc[1q |Turn on LED #1 |DECLL1||||
|Esc[2q |Turn on LED #2 |DECLL2||||
|Esc[3q |Turn on LED #3 |DECLL3||||
|Esc[4q |Turn on LED #4 |DECLL4|||

## Info on the VT100 escape sequences
Information on all the VT100 escape sequences can be found [here](http://ascii-table.com/ansi-escape-sequences-vt-100.php) (This is where my list comes from).

More information on the DEC Terminals can be found on [vt100.net](https://vt100.net).

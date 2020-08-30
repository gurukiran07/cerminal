import sys
from time import sleep

def cprint(text, color=None, background=None, bold=False, italic=False, underline=False):
    """
    prints the given text to stdout with color `color
    and resets back to normal after printing. Supported
    colors are 'black', 'red', 'green', 'yellow', 'blue', 
    'magenta', 'cyan', 'white'.
    """
    _reset = "\033[0m"
    if background is not None:
        _set_background(background)
    _set_color(color, bold, italic, underline)
    out = text+_reset
    sys.stdout.write(out)

def _set_color(color, bold=False, italic=False, underline=False):
    """
    For setting color of the cursor with `color`.
    Accepted colors alias are 'black', 'red', 'green',
    'yellow', 'blue', 'magenta', 'cyan', 'white'.
    Can also gives an values between 0 to 255.
    Check `get_color_codes()` for more info.
    """
    #print(color.isnumeric())
    if not isinstance(color, (int, str)):
        raise TypeError("Expected an int or str type but given {} type".format(type(color).__name__))

    if (isinstance(color, int) and (color>=0 and color<256)) or (color.isnumeric() and (int(color)>=0 and int(color)<256)):
        sys.stdout.write("\033[38;5;{}m".format(color))
        return

    if color is None:
        color = "no_color"
    _bold = ";1" if bold else ""
    _italic = ";3" if italic else ""
    _underline = ";4" if underline else ""

    accepted_colors = {'black':"\033[30{}{}{}m", 'red':"\033[31{}{}{}m", 'green':"\033[32{}{}{}m",
                       'yellow':"\033[33{}{}{}m", 'blue':"\033[34{}{}{}m", 'magenta':"\033[35{}{}{}m", 
                       'cyan':"\033[36{}{}{}m", 'white':"\033[37{}{}{}m", 'no_color':"\033[{}{}{}m"}

    if color not in accepted_colors:
        raise ValueError("Unknown color given {}".format(color))

    sys.stdout.write(accepted_colors[color].format(_bold, _italic, _underline))

def _set_background(color:str):
    """
    Sets the background of the cursor with color
    `color`.
    """
    # TODO: Error handling and extend to support int values from 0 to 256.
    accepted_colors = {'black':"\033[40m", 'red':"\033[41m", 'green':"\033[42m",
                       'yellow':"\033[43m", 'blue':"\033[44m", 'magenta':"\033[45m", 
                       'cyan':"\033[46m", 'white':"\033[47m"}
    if color not in accepted_colors:
        raise ValueError(f"Unknown color given {color}")
    sys.stdout.write(accepted_colors[color])
 
def get_color_codes(animation=False):
    """
    prints color codes in it's respective color,
    used for visual reference.
    """
    v = 0.1 if animation else 0
    for i in range(32):
        for j in range(8):
            #sleep(v)
            code = str(i*8 + j)
            sys.stdout.write("\033[38;5;{}m{}".format(code, code.ljust(4)))
        print('\n')
    print("\033[0m")

cprint("hello world",color=164,bold=True)

#get_color_codes(animation=True)

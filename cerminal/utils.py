from colors import FontStyle, FontColor, BackgroundColor, RESET
import sys
from time import sleep

type_error = "Expected an int or str type but given {} type"


def cprint(
    text,
    color=None,
    background=None,
    bold=False,
    italic=False,
    underline=False,
    end="\n",
):
    """
    prints the given text to stdout with color `color`
    and `background` resets back to normal after printing. 
    Supported colors are 'black', 'red', 'green', 'yellow', 
    'blue', 'magenta', 'cyan', 'white'.
    """
    _reset = "\033[0m"
    bg = "" if background is None else _set_background(background)
    font_color = _set_color(color, bold, italic, underline)
    out = bg + font_color + text + _reset + end
    sys.stdout.write(out)


def _set_color(color, bold=False, italic=False, underline=False):
    """
    For setting color of the cursor with `color`.
    Accepted colors alias are 'black', 'red', 'green',
    'yellow', 'blue', 'magenta', 'cyan', 'white'.
    Can also gives an values between 0 to 255.
    Check `get_color_codes()` for more info.
    """

    if color is not None and not isinstance(color, (int, str)):
        raise TypeError(type_error.format(type(color).__name__))

    _bold = ";1" if bold else ""
    _italic = ";3" if italic else ""
    _underline = ";4" if underline else ""

    if color is None:
        return "\033[39{}{}{}m".format(_bold, _italic, _underline)

    if (isinstance(color, int) and (color >= 0 and color < 256)) or (
        color.isnumeric() and (int(color) >= 0 and int(color) < 256)
    ):
        return "\033[38;5;{}{}{}{}m".format(color, _bold, _italic, _underline)

    accepted_colors = {
        "black": "\033[30{}{}{}m",
        "red": "\033[31{}{}{}m",
        "green": "\033[32{}{}{}m",
        "yellow": "\033[33{}{}{}m",
        "blue": "\033[34{}{}{}m",
        "magenta": "\033[35{}{}{}m",
        "cyan": "\033[36{}{}{}m",
        "white": "\033[37{}{}{}m",
    }

    if color not in accepted_colors:
        raise ValueError("Unknown color given {}".format(color))

    return accepted_colors[color].format(_bold, _italic, _underline)


def _set_background(color):
    """
    Returns the background of the cursor with color
    `color` ansi esacape code. Accepted colors alias are 
    'black', 'red', 'green','yellow', 'blue', 'magenta',
    'cyan', 'white'. Can also gives an values between 0 to 255.
    """

    if not isinstance(color, (int, str)):
        raise TypeError(type_error.format(type(color).__name__))
    if _condition_for_int(color):
        return "\033[48;5;{}m".format(color)

    accepted_colors = {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m",
    }
    if color not in accepted_colors:
        raise ValueError(f"Unknown color given {color}")
    return accepted_colors[color]


def get_color_codes(animation=False, background=False):
    """
    prints color codes in it's respective color,
    used for visual reference.
    """

    ansi_code = "\033[48;5;{}m{}" if background else "\033[38;5;{}m{}"
    v = 0.1 if animation else 0
    for i in range(32):
        for j in range(8):
            sleep(v)
            code = str(i * 8 + j)
            sys.stdout.write(ansi_code.format(code, code.ljust(4)))
            sys.stdout.write("\033[0m")
        sys.stdout.write("\n")


cprint("hello world", color="123", bold=True, italic=True)

get_color_codes(animation=True, background=True)

from colors import Color, FontStyle, FontColor, BackgroundColor
import sys
from time import sleep


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

    _reset = Color.RESET
    bg = "" if background is None else _set_background(background)
    font_color = "" if color is None else _set_color(color)
    font_style = _set_font_style(bold=bold, italic=italic, underline=underline)
    output_style = bg + font_color + font_style
    sys.stdout.write(output_style)
    sys.stdout.write(text)
    sys.stdout.write(_reset + end)


def _set_color(color):
    """
    For setting color of the cursor with `color`.
    Accepted colors alias are 'black', 'red', 'green',
    'yellow', 'blue', 'magenta', 'cyan', 'white'.
    Can also gives an values between 0 to 255.
    Check `get_color_codes()` for more info.
    """

    return FontColor.get_color(color, add_reset=False)


def _set_background(color):
    """
    Returns the background of the cursor with color
    `color` ansi esacape code. Accepted colors alias are
    'black', 'red', 'green','yellow', 'blue', 'magenta',
    'cyan', 'white'. Can also gives an values between 0 to 255.
    """

    return BackgroundColor.get_color(color, add_reset=False)


def _set_font_style(**styles):
    return "".join(
        [
            FontStyle.get_style(style, add_reset=False)
            for style, cond in styles.items()
            if cond
        ]
    )


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


#cprint("hello world", color="123", bold=True, italic=True)

# get_color_codes(background=True)

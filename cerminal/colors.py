type_error = "Expected an int or str type but given {} type"


def _condition_for_int(color):
    return (isinstance(color, int) and (color >= 0 and color < 256)) or (
        color.isnumeric() and (int(color) >= 0 and int(color) < 256)
    )


class Color:
    accepted_color_alias = {
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
    }
    RESET = "\033[0m"


class FontColor(Color):
    """
    Font color class
    """

    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

    @classmethod
    def get_color(self, color, value="", add_reset=True):
        if not isinstance(color, (int, str)):
            raise TypeError(type_error.format(type(color).__name__))

        _reset = self.RESET * add_reset

        if _condition_for_int(color):
            return "\033[38;5;{}m{}{}".format(color, value, _reset)

        if color not in self.accepted_color_alias:
            raise ValueError("Unknown color given {}".format(color))
        return getattr(self, color) + str(value) + _reset


class BackgroundColor(Color):
    """
    Background colors class
    """

    black = "\033[40m"
    red = "\033[41m"
    green = "\033[42m"
    yellow = "\033[43m"
    blue = "\033[44m"
    magenta = "\033[45m"
    cyan = "\033[46m"
    white = "\033[47m"

    @classmethod
    def get_color(self, color, value, add_reset=True):
        if not isinstance(color, (int, str)):
            raise TypeError(type_error.format(type(color).__name__))

        _reset = self.RESET * add_reset

        if _condition_for_int(color):
            return "\033[48;5;{}m{}{}".format(color, value, _reset)

        if color not in self.accepted_color_alias:
            raise ValueError("Unknown color given {}".format(color))

        return getattr(self, color) + str(value) + _reset


class FontStyle(Color):
    """
    Font style class
    """

    bold = "\033[1m"
    italic = "\033[3m"
    underline = "\033[4m"

    @classmethod
    def get_style(self, style, value="", add_reset=True):
        if not isinstance(value, str):
            raise TypeError("Only str type allowed")

        return getattr(self, style) + value + self.RESET * add_reset


#s = f'{FontColor.get_color("red", "im")} {BackgroundColor.get_color("cyan", "danger")}'
# print(s)

# print(FontStyle.get_style('underline', 'HEll'))

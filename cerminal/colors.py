type_error = "Expected an int or str type but given {} type"
RESET = "\033[0m"


def _condition_for_int(color):
    return (isinstance(color, int) and (color >= 0 and color < 256)) or (
        color.isnumeric() and (int(color) >= 0 and int(color) < 256)
    )


class FontColor:
    """
    Font color class
    """
    black="\033[30m"
    red ="\033[31m"
    green ="\033[32m"
    yellow ="\033[33m"
    blue ="\033[34m"
    magenta ="\033[35m"
    cyan ="\033[36m"
    white ="\033[37m"

    @classmethod
    def get_color(self, value, color, add_reset=True):
        if not isinstance(color, (int, str)):
            raise TypeError(type_error.format(type(color).__name__))
        
        if not add_reset:
            _reset = RESET
        _reset = RESET        
        
        if _condition_for_int(color):
            return "\033[38;5;{}m{}{}".format(color, value, _reset)
        
        accepted_color_alias = {
            "black": self.black,
            "red": self.red,
            "green": self.green,
            "yellow": self.yellow,
            "blue": self.blue,
            "magenta": self.magenta,
            "cyan": self.cyan,
            "white": self.white,
        }
        if color not in accepted_color_alias:
            raise ValueError("Unknown color given {}".format(color))
        return accepted_color_alias[color] + str(value) + _reset


class BackgroundColor:
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
    def get_color(self, value, color, add_reset=True):
        if not isinstance(color, (int, str)):
            raise TypeError(type_error.format(type(color).__name__))
        
        if not add_reset:
            _reset = ''
        else:
            _reset = RESET
            
        if _condition_for_int(color):
            return "\033[48;5;{}m{}{}".format(color, value, _reset)

        accepted_color_alias = {
            "black": self.black,
            "red": self.red,
            "green": self.green,
            "yellow": self.yellow,
            "blue": self.blue,
            "magenta": self.magenta,
            "cyan": self.cyan,
            "white": self.white,
        }
        if color not in accepted_color_alias:
            raise ValueError("Unknown color given {}".format(color))

        return accepted_color_alias[color] + str(value) + _reset


class FontStyle:
    """
    Font style class
    """
    bold = "\033[1m"
    italic = "\033[3m"
    underline = "\033[4m"

    @classmethod
    def get_style(self, value, style, add_reset=True):
        if not isinstance(value, str):
            raise TypeError("Only str type allowed")
        if not add_reset:
            return getattr(self, style) + value
        return getattr(self, style) + value + RESET


#s = f'{FontColor.get_color("im", "red")} {BackgroundColor.get_color("danger","cyan")}'
#print(s)

#print(FontStyle.get_style('Hell', 'underline'))

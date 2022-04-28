import config
import config.colour as Style
from config.colour import *

rt = "<class 'config.colour.{}"

def style(string:str, foreground:Style.text = Style.text.white, background:Style.back = None, effect:Style.effect = None):
    """Returns a string with an applied colour and/or effect."""
    # filter valid/invalid arguments
    if True not in [str(type(background)).startswith(rt.format('back')), background == None]:
        raise TypeError('VIPER -> function "style" > "background" parameter must be of type viper.Style.back or None')
    if not str(type(foreground)).startswith(rt.format('text')):
        raise TypeError('VIPER -> function "style" > "foreground" parameter must be of type viper.Style.text')
    if True not in [str(type(effect)).startswith(rt.format('effect')), effect == None]:
        raise TypeError('VIPER -> function "style" > "effect" parameter must be of type viper.Style.effect or None')
    # logic for returning based on available arguments
    if background == None and effect == None:
        return f'{foreground}{string}{Style.end()}'
    elif background == None and effect != None:
        return f'{foreground}{effect}{string}{Style.end()}'
    elif background != None and effect != None:
        return f'{foreground}{background}{effect}{string}{Style.end()}'
    elif background != None and effect == None:
        return f'{foreground}{background}{string}{Style.end()}'
#import kivy
#from kivy.core.text import LabelBase
#
#kivy.resources.resource_add_path('/Library/Fonts/')
##font = kivy.resources.resource_find('DroidSansFallback.ttf')
#font = kivy.resources.resource_find('Songti.ttc')
#LabelBase.register("Roboto", font)

from kivy.config import Config
 
Config.set('kivy', 'default_font', [
    'songti',
    '/Library/Fonts/Songti.ttc'])

fonts_path = 'fonts/'
font = {
        "name": "Roboto",
        "fn_regular": fonts_path + "DroidSansFallback.ttf",
#        "fn_bold": fonts_path + "Roboto-Bold.ttf",
#        "fn_italic": fonts_path + "Roboto-Italic.ttf",
#        "fn_bolditalic": fonts_path + "Roboto-BoldItalic.ttf",
    }
from kivy.core.text import LabelBase
LabelBase.register(**font)


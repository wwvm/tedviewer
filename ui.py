from kivymd.app import MDApp
from kivymd.uix.list import TwoLineIconListItem
from kivy.properties import StringProperty
import savedb
import os

import chn_support

path = '../data/'

class CustomTwoLineIconListItem(TwoLineIconListItem):
    mediaUrl = StringProperty()
    courseId = StringProperty()

    def on_release(self):
        media = f'{path}{self.courseId}.mkv'

        if os.path.exists(media):
            os.system(f'python simple_VLCplayer.py {media}')
            return
            import vlc
            from simple_VLCplayer import simpleVLCplay
            print(media)
            p = vlc.MediaPlayer(media)
            print('playing...')

            simpleVLCplay(p, title=self.text)  # never returns
        elif self.mediaUrl is None:
            print('retrieving...')
            # retrieve media url
            # download file
            print('downloading...')
        else:
            os.system(f'python simple_VLCplayer.py {self.mediaUrl}')
            # download
            print('downloading...')


class UiApp(MDApp):
    def build(self):
        pass

    def search(self, text):
        self.root.ids.rv.data = []
        if text:
            data = savedb.filter_by_title(text)
            self.root.ids.matched.text = f'{len(data)}条'
            for c in data:
                self.root.ids.rv.data.append({
                    'viewclass': 'CustomTwoLineIconListItem',
                    'text': c.title,
                    'secondary_text': c.courseUrl,
                    'mediaUrl': c.mediaUrl,
                    'courseId': c.courseId,
                    })


if __name__ == '__main__':
    UiApp().run()

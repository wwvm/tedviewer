from kivymd.app import MDApp
from kivymd.uix.list import TwoLineIconListItem
from kivy.properties import StringProperty
import savedb
import os
from multiprocessing import Process
from videotrack import titleLike, downloadVideo
import chn_support

path = '../data/'

class CustomTwoLineIconListItem(TwoLineIconListItem):
    mediaUrl = StringProperty()
    courseId = StringProperty()
    icon = StringProperty()

    def on_release(self):
        media = f'{path}{self.courseId}.mkv'

        if os.path.exists(media):
            os.system(f'open {media}')
        elif self.mediaUrl == '':
            print('Not Found!')
        else:
            proc = Process(target=downloadVideo, args=(path, self.courseId, self.mediaUrl))
            proc.start()
            proc.join()
            #os.system(f'python simple_VLCplayer.py {self.mediaUrl}')
            # download
            #print('downloading...')


class UiApp(MDApp):

    def search(self, text):
        self.root.ids.rv.data = []

        if text is not None and len(text) > 1:
            data = titleLike(text) # savedb.filter_by_title(text)
            self.root.ids.matched.text = f'{len(data)}条'
            for c in data:
                self.root.ids.rv.data.append({
                    'viewclass': 'CustomTwoLineIconListItem',
                    'text': c.title,
                    'secondary_text': c.courseUrl,
                    'mediaUrl': c.mediaUrl if c.mediaUrl is not None else '',
                    'icon': 'play-circle' if c.mediaUrl is not None else 'arrow-down-circle',
                    'courseId': c.courseId,
                    })


if __name__ == '__main__':
    UiApp().run()

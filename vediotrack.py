import requests
import re
import codecs
import savedb

rule = r'mp4ShdUrl(?:Orign)?:"(?=http)([^"]+)'
rule1 = r'dUrl(?:Orign)?:"(?=http)([^"]+)'
url = 'http://open.163.com/movie/2019/3/A/3/MEA98R1GG_MEA98TAA3.html'

def getMedia(url):
    res = requests.get(url)
    match = re.search(rule1, res.text)
    if match:
        mediaUrl = codecs.decode(match.group(1), 'unicode-escape')
        return mediaUrl

    return None

def titleLike(title):
    rs = savedb.filter_by_title(title)
    for c in rs:
        mediaUrl = getMedia(c.courseUrl)
        if mediaUrl is not None:
            savedb.update_media_url(c.Id, mediaUrl)
            print(c.title, mediaUrl)
        else:
            print(c.title, 'Media url not found')
            

#getMedia(url)
titleLike('我的')


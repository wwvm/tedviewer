import requests
import csv
import time
import savedb

url = 'https://c.open.163.com/open/pc/v2/search/searchCourse.do?keyword=TED&pageNum=%d&pSize=120'
csvfile = '../data/tedtalks.csv'

def create():
    with open(csvfile, 'w') as fo:
        fo.write('\ufeff')

def retrieve(page):
    res = requests.post(url % page)
    json = res.json()

    savedb.save_all(json['dtos'])
    #save(json['dtos'])
    #for d in json['dtos']:
    #    print(d['courseId'], d['title'], d['courseUrl'], d['description'])

    base = json['baseQuery']
    print (base)
    if base['pageIndex'] < base['totlePageCount'] and base['pageIndex']:
        time.sleep(1)
        retrieve(int(base['pageIndex'] + 1))

def save(data):
    with open(csvfile, 'a+', encoding='utf8') as fo:
        writer = csv.writer(fo, quotechar='"')
        rows = [[d['courseId'], d['title'], d['courseUrl'], d['description']] for d in data]
        writer.writerows(rows)

if __name__ == '__main__':
    #create()
    savedb.create_all()
    retrieve(1)


from sqlalchemy import create_engine
from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Course(Base):
    __tablename__ = 'course'

    Id = Column(Integer, primary_key=True)
    courseId = Column(String)
    courseType = Column(Integer)
    instructor = Column(String)
    school = Column(String)
    title = Column(String)
    movieCount = Column(Integer)
    description = Column(String)
    subject = Column(String)
    category = Column(String)
    tags = Column(String)
    courseUrl = Column(String)
    picUrl = Column(String)
    startTime = Column(String)
    bigPicUrl = Column(String)
    mediaUrl = Column(String)
    status = Column(String)


engine = create_engine('sqlite:///../data/ted.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)

def create_all():
    Base.metadata.create_all()

def save_all(data):
    session = Session()
    rows = [Course(courseId=it['courseId'],
        courseType=it['courseType'],
        instructor=it['instructor'],
        school=it['school'],
        title=it['title'],
        movieCount=it['movieCount'],
        description=it['description'],
        subject=it['subject'],
        category=it['category'],
        tags=it['tags'],
        courseUrl=it['courseUrl'],
        picUrl=it['picUrl'],
        startTime=it['startTime'],
        bigPicUrl=it['bigPicUrl'])
        for it in data]
    session.add_all(rows)
    session.commit()

def filter_by_title(title):
    session = Session()
    return session.query(Course).filter(Course.title.like(f'%{title}%'), Course.mediaUrl.is_(None)).all()

def update_media_url(id, url):
    session = Session()
    session.query(Course).filter(Course.Id == id).update({'mediaUrl': url})
    session.commit()



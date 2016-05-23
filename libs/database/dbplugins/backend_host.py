import uuid
from sqlalchemy.schema import Column
from sqlalchemy.types import String, DateTime, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import time
from datetime import datetime

from ..database import DBModel

Base = declarative_base()

class NmapHostBackend(DBModel):

    class Reports(Base):
        __tablename__ = 'result_ips'

        id = Column('id', Integer, primary_key=True)
        taskid = Column('taskid', String(256))
        inserted = Column('inserted', DateTime)
        domain = Column('domain', String(256))
        address = Column('address', String(128))
        is_up = Column('is_up', String(128))
        os =Column('os', Text)

        def __init__(self, host_struct):
            self.taskid = host_struct.taskid
            self.inserted = datetime.fromtimestamp(time.time())
            self.domain = host_struct.domain
            self.address = host_struct.address
            self.is_up = host_struct.is_up
            self.os = host_struct.os

    def __init__(self, **kwargs):
        DBModel.__init__(self)
        self.Session = sessionmaker()
        self.engine = None
        self.url = None

        if 'url' not in kwargs:
            raise ValueError('Need database connect url')

        self.url = kwargs['url']
        del kwargs['url']
        try:
            self.engine = create_engine(self.url, **kwargs)
            Base.metadata.create_all(bind=self.engine, checkfirst=True)
            self.Session.configure(bind=self.engine)
        except Exception as e:
            raise

    def insert(self, host_struct):
        sess = self.Session()
        sess.add(NmapHostBackend.Reports(host_struct))
        sess.commit()
        sess.close()

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

class NmapServiceBackend(DBModel):

    class Reports(Base):
        __tablename__ = 'result_ports'

        id = Column('id', Integer, primary_key=True)
        taskid = Column('taskid', String(256))
        inserted = Column('inserted', DateTime(), default='now')
        address = Column('address', String(256))
        port = Column('port', Integer)
        service = Column('service', String(256))
        state = Column('state', String(12))
        protocol = Column('protocol', String(12))
        product = Column('product', String(64))
        product_version = Column('product_version', String(64))
        product_extrainfo = Column('product_extrainfo', String(128))
        # banner = Column('banner', String(256))
        scripts_results = Column('scripts_results', Text)

        def __init__(self, service_struct):
            self.taskid = service_struct.taskid
            self.inserted = datetime.fromtimestamp(time.time())
            self.address = str(service_struct.address)
            self.port = service_struct.port
            self.service = str(service_struct.service)
            self.state = str(service_struct.state)
            self.protocol = str(service_struct.protocol)
            self.product = str(service_struct.product)
            self.product_version = str(service_struct.product_version)
            self.product_extrainfo = str(service_struct.product_extrainfo)
            self.scripts_results = str(service_struct.scripts_results)


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

    def insert(self, service_struct):
        sess = self.Session()
        sess.add(NmapServiceBackend.Reports(service_struct))
        sess.commit()
        sess.close()

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CustomBase(Base):
    __abstract__ = True

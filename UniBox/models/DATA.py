from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from UniBox.models.meta import Base


class Data(Base):
    __tablename__ = 'DATA'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    phone = Column(Text)
    email = Column(Text)


Index('my_index', Data.id, unique=True, mysql_length=255)


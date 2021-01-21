from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from UniBox.models.meta import Base


class QA(Base):
    __tablename__ = 'Q_A'
    id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(Text)
    count = Column(Integer)

def __repr__(self):
    return '<QA(question = "{}", answer = "{}">', format(self.question, self.answer)


Index('my_index', QA.id, unique=True, mysql_length=255)


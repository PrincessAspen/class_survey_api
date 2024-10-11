from .base import Base

class Topic(Base, table=True):
    __tablename__ = "topics"

    topic_name: str
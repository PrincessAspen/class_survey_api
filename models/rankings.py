from .base import Base

class Ranking(Base, table=True):
    __tablename__ = "rankings"

    ranking_name: str
    ranking_value: int
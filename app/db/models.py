from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    embedding = Column(Text, nullable=False)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..db.models import Document
from ..models.schemas import DocumentCreate, Question
import openai
import json

router = APIRouter()

# Ingestion Endpoint
@router.post("/documents/")
def create_document(doc: DocumentCreate, db: Session = Depends(get_db)):
    embedding = "dummy_embedding"  # Replace with LLM-generated embedding
    new_doc = Document(title=doc.title, content=doc.content, embedding=embedding)
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

# Retrieval Endpoint
@router.post("/qa/")
def answer_question(q: Question, db: Session = Depends(get_db)):
    docs = db.query(Document).all()
    if not docs:
        raise HTTPException(status_code=404, detail="No documents found.")
    
    # Dummy Retrieval Logic
    response = f"Based on my knowledge, here's an answer to '{q.question}'"
    return {"question": q.question, "answer": response}

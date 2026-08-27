from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentResponse

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/", response_model=DocumentResponse, status_code=201)
def create_document(document: DocumentCreate, db: Session=Depends(get_db)):
    new_document = Document(filename=document.filename,
                            file_type=document.file_type,
                            status="uploaded")

    db.add(new_document)
    db.commit()
    db.refresh(new_document)
    return new_document


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int, db: Session = Depends(get_db)):
    document = (db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return document
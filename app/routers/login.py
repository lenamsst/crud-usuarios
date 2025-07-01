from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import auth, models
from ..database import SessionLocal

router = APIRouter(prefix="/login", tags=["auth"])

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    
    token = auth.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}



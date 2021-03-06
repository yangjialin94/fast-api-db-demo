from fastapi import status, HTTPException
from .. import models, token
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


def login(request: OAuth2PasswordRequestForm, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials",
        )
    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Password",
        )
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

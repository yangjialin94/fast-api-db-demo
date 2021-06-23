from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(prefix="/blog", tags=["Blogs"])
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = blog.get_all(db)
    return blogs


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = blog.create(request, db)
    return new_blog


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def destroy(id, db: Session = Depends(get_db)):
    return blog.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    return blog.show(id, db)

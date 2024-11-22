from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Welcome to the FastAPI product CRUD API!'}


@app.post('/products/', response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate, db: Session = Depends(get_db)
):
    try:
        return crud.create_product(db=db, product=product)
    except IntegrityError as e:
        db.rollback()

        if 'CHECK constraint failed' in str(e):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='The product price must be greater than zero.',
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='An unexpected error occurred while creating the product.',
            )

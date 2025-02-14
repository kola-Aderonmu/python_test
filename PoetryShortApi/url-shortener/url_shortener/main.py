from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import shortuuid
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


from . import models, schemas, database
from .config import Settings

app = FastAPI()

# Create tables

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# creating Controllers Routes

@app.get("/")
def read_root():
    return {"message": "Welcome to URL shortener API"}

@app.post("/urls/", response_model=schemas.URL)
def create_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    #Generate a short ID
    short_id = shortuuid.uuid()[:8]

    # Create URL instance
    db_url = models.URL(id=short_id, original_url=str(url.target_url)
    )

    # Save to database

    db.add(db_url)
    db.commit()
    db.refresh(db_url)



    # Return with the short URL
    return schemas.URL(
        target_url=url.target_url,
        short_url=f"{Settings.base_url}/{short_id}",
        created_at=db_url.created_at,
    )   



# User make their request

@app.get("/{short_id}")
def forward_to_target_url(short_id: str, db: Session = Depends(get_db)):
    # Look up URL in database
    db_url = (
        db.query(models.URL)
        .filter(models.URL.id == short_id, models.URL.is_active)
        .first()
    )

    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return {"url": db_url.original_url}


# Function to start our program


def start():
    
    uvicorn.run("url_shortener.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()

    
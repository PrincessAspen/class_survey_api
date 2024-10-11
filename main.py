import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from db import get_session

from models.rankings import Ranking
from models.topics import Topic

origins = [
    'http://localhost',
    'http://localhost:3000'
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

@app.get('/')
def root():
    return {'message' : 'Root Route'}

@app.get('/rankings')
def get_rankings(session: Session = Depends(get_session)):
    statement = select(Ranking)
    results = session.exec(statement).all()
    return results

@app.get('/topics')
def get_rankings(session: Session = Depends(get_session)):
    statement = select(Topic)
    results = session.exec(statement).all()
    return results

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
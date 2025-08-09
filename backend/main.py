from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .data import ARTICLE_SUMMARIES, ARTICLES, NARRATIVES

app = FastAPI(title="Bias Lab API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
    ,
    allow_headers=["*"],
)


@app.get("/articles")
def get_articles():
    return ARTICLE_SUMMARIES.model_dump()


@app.get("/articles/{article_id}")
def get_article(article_id: str):
    for a in ARTICLES:
        if a.id == article_id:
            return a.model_dump()
    raise HTTPException(status_code=404, detail="Not found")


@app.get("/narratives")
def get_narratives():
    return NARRATIVES.model_dump()



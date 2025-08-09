from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from data import ARTICLE_SUMMARIES, ARTICLES, NARRATIVES
from models import ArticleDetail, ArticleSummary, NarrativeCluster, ApiList

app = FastAPI(title="Bias Lab API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/articles", response_model=ApiList[ArticleSummary])
def get_articles():
    return ARTICLE_SUMMARIES

@app.get("/articles/{article_id}", response_model=ArticleDetail)
def get_article(article_id: str):
    for a in ARTICLES:
        if a.id == article_id:
            return a
    raise HTTPException(status_code=404, detail="Not found")

@app.get("/narratives", response_model=ApiList[NarrativeCluster])
def get_narratives():
    return NARRATIVES
# models.py
from typing import Generic, List, Literal, Optional, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel

BiasDimension = Literal["ideology", "factual", "framing", "emotion", "transparency"]

class BiasScores(BaseModel):
    ideology: int
    factual: int
    framing: int
    emotion: int
    transparency: int

class PrimarySource(BaseModel):
    title: str
    url: str

class Highlight(BaseModel):
    start: int
    end: int
    dimension: BiasDimension
    score: int
    note: Optional[str] = None

class ArticleSummary(BaseModel):
    id: str
    title: str
    outlet: str
    publishedAt: str
    url: str
    scores: BiasScores

class ArticleDetail(ArticleSummary):
    author: Optional[str] = None
    content: str
    highlights: List[Highlight]
    timeline: Optional[List[dict]] = None

class NarrativeCluster(BaseModel):
    id: str
    title: str
    summary: str
    keywords: List[str]
    intensity: int
    sentiment: float
    topArticles: List[ArticleSummary]
    sparkline: List[int]

# ---------- Generic wrapper ----------
T = TypeVar("T")

class ApiList(GenericModel, Generic[T]):
    items: List[T]
    updatedAt: str
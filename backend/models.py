from __future__ import annotations
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, Field


BiasDimension = Literal["ideology", "factual", "framing", "emotion", "transparency"]


class BiasScores(BaseModel):
    ideology: int = Field(ge=0, le=100)
    factual: int = Field(ge=0, le=100)
    framing: int = Field(ge=0, le=100)
    emotion: int = Field(ge=0, le=100)
    transparency: int = Field(ge=0, le=100)


class HighlightSpan(BaseModel):
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
    highlights: List[HighlightSpan]
    timeline: Optional[List[Dict[str, int | str]]] = None


class NarrativeCluster(BaseModel):
    id: str
    title: str
    summary: str
    keywords: List[str]
    intensity: int
    sentiment: float
    topArticles: List[ArticleSummary]
    sparkline: List[int]


class ApiList(BaseModel):
    items: List
    updatedAt: str



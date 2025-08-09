from __future__ import annotations
from datetime import datetime, timedelta
from typing import List
from .models import (
    BiasScores,
    ArticleDetail,
    ArticleSummary,
    NarrativeCluster,
    ApiList,
)


now = datetime.utcnow()


def clamp(v: int) -> int:
    return max(0, min(100, v))


def scores(**kwargs) -> BiasScores:
    base = dict(ideology=50, factual=75, framing=50, emotion=40, transparency=65)
    base.update(kwargs)
    # Ensure values are 0..100 so the radar chart geometry is correct
    base = {k: clamp(int(v)) for k, v in base.items()}
    return BiasScores(**base)


ARTICLES: List[ArticleDetail] = [
    ArticleDetail(
        id="a1",
        title="Federal Policy Shifts Spark Market Debate",
        outlet="Global Ledger",
        author="Ava Singh",
        publishedAt=(now - timedelta(hours=3)).isoformat(),
        url="https://example.com/a1",
        scores=scores(ideology=66, factual=82, framing=58, emotion=36, transparency=72),
        content=(
            "Analysts disagreed on whether the policy would slow inflation. "
            "While some called it prudent, others warned of job losses. "
            "The administration framed the move as temporary stabilization."
        ),
        highlights=[
            dict(start=9, end=18, dimension="framing", score=62, note="disagreed"),
            dict(start=94, end=101, dimension="ideology", score=70, note="warned"),
            dict(start=132, end=176, dimension="framing", score=64, note="framed the move as"),
            dict(start=177, end=209, dimension="emotion", score=38, note="temporary stabilization"),
        ],
        timeline=[
            dict(date=(now - timedelta(days=13 - i)).isoformat(), biasIndex=45 + round(10 * __import__("math").sin(i / 2)))
            for i in range(14)
        ],
    ),
    ArticleDetail(
        id="a2",
        title="Regional Grid Faces Strain Amid Heatwave",
        outlet="Northstar News",
        author="Liam Zhou",
        publishedAt=(now - timedelta(hours=26)).isoformat(),
        url="https://example.com/a2",
        scores=scores(ideology=44, factual=79, framing=52, emotion=48, transparency=60),
        content=(
            "Officials urged conservation as demand surged. Critics argued that deferred maintenance left systems vulnerable. "
            "Utilities said they were prepared for peak conditions."
        ),
        highlights=[
            dict(start=0, end=8, dimension="emotion", score=52, note="Officials urged"),
            dict(start=54, end=84, dimension="factual", score=80, note="deferred maintenance"),
            dict(start=118, end=131, dimension="framing", score=55, note="prepared"),
        ],
        timeline=[
            dict(date=(now - timedelta(days=13 - i)).isoformat(), biasIndex=52 + round(8 * __import__("math").cos(i / 2)))
            for i in range(14)
        ],
    ),
    ArticleDetail(
        id="a3",
        title="New Study Maps Urban Transit Equity Gaps",
        outlet="Civic Review",
        author="Maya Ortiz",
        publishedAt=(now - timedelta(days=2)).isoformat(),
        url="https://example.com/a3",
        scores=scores(ideology=58, factual=88, framing=62, emotion=34, transparency=80),
        content=(
            "Researchers identified disparities in access across neighborhoods. "
            "Advocates welcomed the findings, calling for targeted investment. "
            "City officials promised a comprehensive review."
        ),
        highlights=[
            dict(start=0, end=11, dimension="factual", score=86, note="Researchers identified"),
            dict(start=85, end=111, dimension="emotion", score=40, note="welcomed the findings"),
            dict(start=143, end=167, dimension="framing", score=60, note="comprehensive review"),
        ],
        timeline=[
            dict(date=(now - timedelta(days=13 - i)).isoformat(), biasIndex=48 + round(12 * __import__("math").sin(0.5 + i / 3)))
            for i in range(14)
        ],
    ),
]


ARTICLE_SUMMARIES = ApiList(
    items=[
        ArticleSummary(
            id=a.id,
            title=a.title,
            outlet=a.outlet,
            publishedAt=a.publishedAt,
            url=a.url,
            scores=a.scores,
        )
        for a in ARTICLES
    ],
    updatedAt=now.isoformat(),
)


NARRATIVES = ApiList(
    items=[
        NarrativeCluster(
            id="1",
            title="Policy vs Markets",
            summary="Debate over whether rate moves cool inflation without harming jobs.",
            keywords=["inflation", "rates", "jobs", "stabilization"],
            intensity=78,
            sentiment=0.1,
            topArticles=[ARTICLE_SUMMARIES.items[0], ARTICLE_SUMMARIES.items[1]],
            sparkline=[20, 28, 33, 45, 52, 49, 61, 66, 62, 58, 63, 72],
        ),
        NarrativeCluster(
            id="2",
            title="Grid Reliability",
            summary="Heatwave pressures aging infrastructure; preparedness questioned.",
            keywords=["grid", "heatwave", "maintenance", "peak"],
            intensity=64,
            sentiment=-0.05,
            topArticles=[ARTICLE_SUMMARIES.items[1], ARTICLE_SUMMARIES.items[2]],
            sparkline=[12, 14, 18, 19, 23, 27, 31, 29, 34, 36, 42, 48],
        ),
        NarrativeCluster(
            id="3",
            title="Transit Equity",
            summary="Study highlights uneven access; calls for targeted investment.",
            keywords=["transit", "equity", "access", "investment"],
            intensity=55,
            sentiment=0.2,
            topArticles=[ARTICLE_SUMMARIES.items[2], ARTICLE_SUMMARIES.items[0]],
            sparkline=[10, 11, 13, 17, 18, 20, 23, 22, 25, 27, 29, 35],
        ),
        NarrativeCluster(
            id="4",
            title="Water Policy & Drought",
            summary="Allocation rules face scrutiny as reservoirs fall and consumption rises.",
            keywords=["drought", "reservoirs", "allocation", "consumption"],
            intensity=61,
            sentiment=-0.02,
            topArticles=[ARTICLE_SUMMARIES.items[0], ARTICLE_SUMMARIES.items[2]],
            sparkline=[15, 16, 19, 22, 24, 23, 28, 30, 33, 31, 35, 39],
        ),
        NarrativeCluster(
            id="5",
            title="AI in Classrooms",
            summary="Debate over safeguards, benefits, and the future of assessment.",
            keywords=["education", "AI", "assessment", "policy"],
            intensity=59,
            sentiment=0.05,
            topArticles=[ARTICLE_SUMMARIES.items[1], ARTICLE_SUMMARIES.items[0]],
            sparkline=[9, 12, 15, 18, 21, 25, 27, 29, 28, 31, 34, 38],
        ),
    ],
    updatedAt=now.isoformat(),
)



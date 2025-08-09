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
    base = {k: clamp(int(v)) for k, v in base.items()}
    return BiasScores(**base)


def make_highlights(text: str, specs: List[tuple[str, str, int, str | None]]):
    spans = []
    cursor = 0
    lower = text.lower()
    for phrase, dim, score, note in specs:
        p = phrase.lower()
        idx = lower.find(p, cursor)
        if idx == -1:
            idx = lower.find(p)
        if idx == -1:
            continue
        spans.append({
            "start": idx,
            "end": idx + len(phrase),
            "dimension": dim,  # type: ignore
            "score": score,
            "note": note,
        })
        cursor = idx + len(phrase)
    return spans


ARTICLES: List[ArticleDetail] = [
    ArticleDetail(
        id="a1",
        title="Federal Policy Shifts Spark Market Debate",
        outlet="Global Ledger",
        author="Ava Singh",
        publishedAt=(now - timedelta(hours=3)).isoformat(),
        url="https://www.federalreserve.gov/monetarypolicy.htm",
        scores=scores(ideology=66, factual=82, framing=58, emotion=36, transparency=72),
        content=(
            "Federal Reserve officials signaled that rates may remain elevated while inflation cools unevenly across sectors. "
            "Analysts disagreed about the near‑term effect on hiring; some described the posture as prudent stabilization, while others warned it could weigh on investment. "
            "In public remarks, the administration framed the policy as temporary stabilization tied to incoming data and emphasized transparency in future guidance."
        ),
        highlights=make_highlights(
            text=(
                "Federal Reserve officials signaled that rates may remain elevated while inflation cools unevenly across sectors. "
                "Analysts disagreed about the near‑term effect on hiring; some described the posture as prudent stabilization, while others warned it could weigh on investment. "
                "In public remarks, the administration framed the policy as temporary stabilization tied to incoming data and emphasized transparency in future guidance."
            ),
            specs=[
                ("disagreed", "framing", 62, "disagreement"),
                ("warned", "emotion", 60, "risk language"),
                ("framed the policy as temporary stabilization", "framing", 64, "official framing"),
                ("transparency", "transparency", 76, "commitment to guidance"),
            ],
        ),
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
        url="https://www.nerc.com/pa/RAPA/ra/Pages/default.aspx",
        scores=scores(ideology=44, factual=79, framing=52, emotion=48, transparency=60),
        content=(
            "With temperatures rising across the region, officials urged conservation as demand surged toward record territory. "
            "Critics argued that deferred maintenance over multiple seasons left parts of the system vulnerable to heat‑related failures. "
            "Utilities said they were prepared for peak conditions and emphasized that crews and spare capacity had been staged in advance."
        ),
        highlights=make_highlights(
            text=(
                "With temperatures rising across the region, officials urged conservation as demand surged toward record territory. "
                "Critics argued that deferred maintenance over multiple seasons left parts of the system vulnerable to heat‑related failures. "
                "Utilities said they were prepared for peak conditions and emphasized that crews and spare capacity had been staged in advance."
            ),
            specs=[
                ("officials urged", "emotion", 52, "call to act"),
                ("deferred maintenance", "factual", 80, "infrastructure detail"),
                ("prepared for peak", "framing", 55, "readiness framing"),
            ],
        ),
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
        url="https://transitcenter.org/",
        scores=scores(ideology=58, factual=88, framing=62, emotion=34, transparency=80),
        content=(
            "In a newly released analysis, researchers identified disparities in transit access that track with historic investment patterns. "
            "Community advocates welcomed the findings and called for targeted investment in frequent service, accessible stations, and safer connections. "
            "City officials promised a comprehensive review and said an update to the capital plan would prioritize corridors with the largest equity gaps."
        ),
        highlights=make_highlights(
            text=(
                "In a newly released analysis, researchers identified disparities in transit access that track with historic investment patterns. "
                "Community advocates welcomed the findings and called for targeted investment in frequent service, accessible stations, and safer connections. "
                "City officials promised a comprehensive review and said an update to the capital plan would prioritize corridors with the largest equity gaps."
            ),
            specs=[
                ("researchers identified", "factual", 86, "method/claim"),
                ("welcomed the findings", "emotion", 40, "reception"),
                ("comprehensive review", "framing", 60, "scope framing"),
            ],
        ),
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
            id="n1",
            title="Policy vs Markets",
            summary="Debate over whether rate moves cool inflation without harming jobs.",
            keywords=["inflation", "rates", "jobs", "stabilization"],
            intensity=78,
            sentiment=0.1,
            topArticles=[ARTICLE_SUMMARIES.items[0], ARTICLE_SUMMARIES.items[1]],
            sparkline=[20, 28, 33, 45, 52, 49, 61, 66, 62, 58, 63, 72],
        ),
        NarrativeCluster(
            id="n2",
            title="Grid Reliability",
            summary="Heatwave pressures aging infrastructure; preparedness questioned.",
            keywords=["grid", "heatwave", "maintenance", "peak"],
            intensity=64,
            sentiment=-0.05,
            topArticles=[ARTICLE_SUMMARIES.items[1], ARTICLE_SUMMARIES.items[2]],
            sparkline=[12, 14, 18, 19, 23, 27, 31, 29, 34, 36, 42, 48],
        ),
        NarrativeCluster(
            id="n3",
            title="Transit Equity",
            summary="Study highlights uneven access; calls for targeted investment.",
            keywords=["transit", "equity", "access", "investment"],
            intensity=55,
            sentiment=0.2,
            topArticles=[ARTICLE_SUMMARIES.items[2], ARTICLE_SUMMARIES.items[0]],
            sparkline=[10, 11, 13, 17, 18, 20, 23, 22, 25, 27, 29, 35],
        ),
        NarrativeCluster(
            id="n4",
            title="Water Policy & Drought",
            summary="Allocation rules face scrutiny as reservoirs fall and consumption rises.",
            keywords=["drought", "reservoirs", "allocation", "consumption"],
            intensity=61,
            sentiment=-0.02,
            topArticles=[ARTICLE_SUMMARIES.items[0], ARTICLE_SUMMARIES.items[2]],
            sparkline=[15, 16, 19, 22, 24, 23, 28, 30, 33, 31, 35, 39],
        ),
        NarrativeCluster(
            id="n5",
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



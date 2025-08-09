import type { ApiList, ArticleDetail, ArticleSummary, NarrativeCluster } from "@/types";
import { narratives as mockNarratives, articleSummaries as mockSummaries, articles as mockArticles } from "@/data/mock";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function fetchNarratives(): Promise<ApiList<NarrativeCluster>> {
  try {
    const res = await fetch(`${API_BASE}/narratives`, { next: { revalidate: 30 } });
    if (!res.ok) throw new Error("Failed to fetch narratives");
    return res.json();
  } catch {
    return mockNarratives as unknown as ApiList<NarrativeCluster>;
  }
}

export async function fetchArticles(): Promise<ApiList<ArticleSummary>> {
  try {
    const res = await fetch(`${API_BASE}/articles`, { next: { revalidate: 30 } });
    if (!res.ok) throw new Error("Failed to fetch articles");
    return res.json();
  } catch {
    return mockSummaries as unknown as ApiList<ArticleSummary>;
  }
}

export async function fetchArticle(id: string): Promise<ArticleDetail> {
  try {
    const res = await fetch(`${API_BASE}/articles/${id}`, { next: { revalidate: 30 } });
    if (!res.ok) throw new Error("Failed to fetch article");
    return res.json();
  } catch {
    const a = mockArticles.find((x) => x.id === id);
    if (!a) throw new Error("Not found");
    return a as unknown as ArticleDetail;
  }
}



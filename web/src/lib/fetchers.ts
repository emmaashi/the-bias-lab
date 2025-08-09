import type {
  ApiList,
  ArticleDetail,
  ArticleSummary,
  NarrativeCluster,
} from "@/types";
import {
  narratives as mockNarratives,
  articleSummaries as mockSummaries,
  articles as mockArticles,
} from "@/data/mock";

const API_BASE =
  process.env.NEXT_PUBLIC_API_URL?.replace(/\/$/, "") || "http://localhost:8000";
const USE_MOCK = process.env.NEXT_PUBLIC_USE_MOCK === "1";

async function fetchJSON<T>(url: string, init?: RequestInit): Promise<T> {
  const res = await fetch(url, init);
  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(`HTTP ${res.status} for ${url}${text ? ` — ${text}` : ""}`);
  }
  return res.json() as Promise<T>;
}

export async function fetchNarratives(): Promise<ApiList<NarrativeCluster>> {
  try {
    return await fetchJSON<ApiList<NarrativeCluster>>(
      `${API_BASE}/narratives`,
      { next: { revalidate: 30 } }
    );
  } catch (err) {
    if (USE_MOCK) return mockNarratives as unknown as ApiList<NarrativeCluster>;
    throw err;
  }
}

export async function fetchArticles(): Promise<ApiList<ArticleSummary>> {
  try {
    return await fetchJSON<ApiList<ArticleSummary>>(
      `${API_BASE}/articles`,
      { next: { revalidate: 30 } }
    );
  } catch (err) {
    if (USE_MOCK) return mockSummaries as unknown as ApiList<ArticleSummary>;
    throw err;
  }
}

export async function fetchArticle(id: string): Promise<ArticleDetail> {
  try {
    return await fetchJSON<ArticleDetail>(
      `${API_BASE}/articles/${encodeURIComponent(id)}`,
      { cache: "no-store" }
    );
  } catch (err) {
    if (USE_MOCK) {
      const a = mockArticles.find((x) => x.id === id);
      if (a) return a as unknown as ArticleDetail;
    }
    throw err;
  }
}
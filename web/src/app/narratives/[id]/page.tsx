import Link from "next/link";
import { narratives, articles } from "@/data/mock";
import { RadarChart } from "@/components/RadarChart";

export const dynamic = "force-dynamic";

function averageScores(ids: string[]) {
  const picked = articles.filter((a) => ids.includes(a.id));
  const sum = { ideology: 0, factual: 0, framing: 0, emotion: 0, transparency: 0 } as const;
  const acc: any = { ...sum };
  picked.forEach((a) => {
    for (const k of Object.keys(a.scores) as Array<keyof typeof acc>) {
      acc[k] += a.scores[k];
    }
  });
  const n = Math.max(1, picked.length);
  for (const k of Object.keys(acc) as Array<keyof typeof acc>) acc[k] = Math.round(acc[k] / n);
  return acc as typeof acc;
}

export default async function NarrativeDetail({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const { items } = narratives;
  const narrative = items.find((n) => n.id === id);
  if (!narrative) {
    return (
      <main className="min-h-dvh bg-background text-foreground"><div className="mx-auto max-w-5xl px-6 md:px-10 py-12">Not found</div></main>
    );
  }
  const avg = averageScores(narrative.topArticles.map((a) => a.id));

  return (
    <main className="min-h-dvh bg-background text-foreground">
      <div className="mx-auto max-w-6xl px-6 md:px-10 py-12 md:py-16">
        <div className="flex items-center justify-between">
          <Link href="/narratives" className="text-sm hover:opacity-70">← Narratives</Link>
        </div>
        <header className="mt-6">
          <h1 className="text-3xl md:text-4xl font-semibold tracking-tight">{narrative.title}</h1>
          <p className="mt-2 text-foreground/70 max-w-2xl">{narrative.summary}</p>
          <div className="mt-3 text-xs text-foreground/50">{narrative.keywords.join(" · ")}</div>
        </header>

        <section className="mt-10 grid grid-cols-1 md:grid-cols-3 gap-10">
          <div className="md:col-span-2">
            <h2 className="text-sm font-semibold tracking-tight">Bias over time</h2>
            <div className="mt-3 h-40 rounded-xl border border-foreground/10 p-3">
              <svg viewBox="0 0 600 140" width="100%" height="100%">
                <rect x="0" y="0" width="600" height="140" fill="none" stroke="currentColor" strokeOpacity="0.08" />
                {/* sparkline scaled to container */}
                {(() => {
                  const values = narrative.sparkline;
                  const min = Math.min(...values);
                  const max = Math.max(...values);
                  const range = Math.max(1, max - min);
                  const pts = values.map((v, i) => {
                    const x = (i / (values.length - 1)) * 600;
                    const y = 140 - ((v - min) / range) * 140;
                    return `${x},${y}`;
                  });
                  return (
                    <polyline points={pts.join(" ")} fill="none" stroke="#0ea5e9" strokeWidth={2} />
                  );
                })()}
              </svg>
            </div>
          </div>
          <aside className="md:col-span-1 rounded-2xl border border-foreground/10 p-4">
            <h2 className="text-sm font-semibold tracking-tight">Average bias profile</h2>
            <div className="mt-4"><RadarChart scores={avg} /></div>
          </aside>
        </section>

        <section className="mt-10">
          <h3 className="text-sm font-semibold tracking-tight">Top articles</h3>
          <div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
            {narrative.topArticles.map((a) => (
              <div key={a.id} className="rounded-xl border border-foreground/10 p-4 flex items-start justify-between">
                <div>
                  <Link href={`/articles/${a.id}`} className="font-medium hover:opacity-80">{a.title}</Link>
                  <div className="text-xs text-foreground/60 mt-1">{a.outlet}</div>
                </div>
                <a href={a.url} target="_blank" rel="noopener noreferrer" className="text-xs rounded-full border border-foreground/15 px-3 py-1.5 hover:bg-foreground/5">Primary</a>
              </div>
            ))}
          </div>
        </section>
      </div>
    </main>
  );
}



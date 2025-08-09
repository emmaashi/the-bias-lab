"use client";
import * as React from "react";
import type { HighlightSpan, BiasDimension } from "@/types";

const colorByDim: Record<BiasDimension, string> = {
  ideology: "#3b82f6",
  factual: "#22c55e",
  framing: "#a855f7",
  emotion: "#ef4444",
  transparency: "#f59e0b",
};

export function Highlights({
  text,
  spans,
}: {
  text: string;
  spans: HighlightSpan[];
}) {
  const [hovered, setHovered] = React.useState<number | null>(null);
  const parts: Array<React.ReactNode> = [];

  let cursor = 0;
  spans
    .slice()
    .sort((a, b) => a.start - b.start)
    .forEach((span, idx) => {
      if (span.start > cursor) {
        parts.push(<span key={`t-${cursor}`}>{text.slice(cursor, span.start)}</span>);
      }
      const color = colorByDim[span.dimension];
      parts.push(
        <span
          key={`h-${idx}`}
          onMouseEnter={() => setHovered(idx)}
          onMouseLeave={() => setHovered(null)}
          style={{
            background: hovered === idx ? `${color}22` : `${color}14`,
            borderBottom: `1px solid ${color}44`,
          }}
          className="cursor-help rounded-[6px] px-0.5"
          title={`${span.dimension} • ${span.score}` + (span.note ? ` • ${span.note}` : "")}
        >
          {text.slice(span.start, span.end)}
        </span>
      );
      cursor = span.end;
    });
  if (cursor < text.length) parts.push(<span key={`t-${cursor}`}>{text.slice(cursor)}</span>);

  return <p className="leading-relaxed text-foreground/80">{parts}</p>;
}



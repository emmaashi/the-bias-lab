import { NextResponse } from "next/server";
import { articleSummaries } from "@/data/mock";

export async function GET() {
  return NextResponse.json(articleSummaries, { status: 200 });
}



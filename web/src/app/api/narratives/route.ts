import { NextResponse } from "next/server";
import { narratives } from "@/data/mock";

export async function GET() {
  return NextResponse.json(narratives, { status: 200 });
}



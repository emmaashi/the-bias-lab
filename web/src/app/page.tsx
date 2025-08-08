import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-dvh bg-background text-foreground">
      <div className="mx-auto max-w-7xl px-6 md:px-10">
        <nav className="flex items-center justify-between py-6">
          <div className="flex items-center gap-3">
            <div className="size-8 rounded-full bg-foreground" />
            <span className="text-sm font-medium tracking-tight">The Bias Lab</span>
          </div>
          <div className="hidden md:flex items-center gap-6 text-sm">
            <Link href="#work" className="hover:opacity-70 transition-opacity">Work</Link>
            <Link href="#about" className="hover:opacity-70 transition-opacity">About</Link>
            <Link href="#contact" className="hover:opacity-70 transition-opacity">Contact</Link>
            <a
              href="https://vercel.com/new"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center rounded-full bg-foreground text-background px-4 py-2 text-sm font-medium hover:opacity-90"
            >
              Launch on Vercel
            </a>
          </div>
        </nav>

        <section className="grid grid-cols-1 md:grid-cols-12 items-center gap-8 py-16 md:py-28">
          <div className="md:col-span-7">
            <h1 className="text-4xl md:text-6xl font-semibold tracking-tight leading-[1.05]">
              Design with restraint. Build with precision.
            </h1>
            <p className="mt-6 text-base md:text-lg text-foreground/70 max-w-xl">
              A crisp, modern foundation for a research-first product. Minimal surfaces, generous whitespace, and thoughtful defaults.
            </p>
            <div className="mt-10 flex items-center gap-3">
              <Link
                href="#get-started"
                className="inline-flex items-center rounded-full bg-foreground text-background px-5 py-3 text-sm font-semibold hover:opacity-90"
              >
                Get started
              </Link>
              <Link
                href="#learn-more"
                className="inline-flex items-center rounded-full border border-foreground/15 px-5 py-3 text-sm font-semibold hover:bg-foreground/5"
              >
                Learn more
              </Link>
            </div>
          </div>
          <div className="md:col-span-5">
            <div className="aspect-[4/3] rounded-2xl border border-foreground/10 bg-gradient-to-br from-foreground/[.06] to-transparent" />
          </div>
        </section>

        <section id="work" className="py-16 md:py-24 border-t border-foreground/10">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[
              { title: "Clean Typography", desc: "Geist fonts, optical balance, tight leading." },
              { title: "Adaptive Surfaces", desc: "Light/dark aware tokens, high contrast controls." },
              { title: "Production Ready", desc: "Type-safe, accessible, Vercel-native." },
            ].map((card) => (
              <div key={card.title} className="rounded-2xl border border-foreground/10 p-6">
                <h3 className="text-base font-semibold tracking-tight">{card.title}</h3>
                <p className="mt-2 text-sm text-foreground/70">{card.desc}</p>
              </div>
            ))}
          </div>
        </section>

        <footer className="py-10 border-t border-foreground/10 text-sm text-foreground/60">
          <div className="flex items-center justify-between">
            <span>© {new Date().getFullYear()} The Bias Lab</span>
            <div className="flex items-center gap-4">
              <Link href="/" className="hover:opacity-70">Home</Link>
              <a href="https://nextjs.org" target="_blank" rel="noopener noreferrer" className="hover:opacity-70">Next.js</a>
            </div>
          </div>
        </footer>
      </div>
    </main>
  );
}

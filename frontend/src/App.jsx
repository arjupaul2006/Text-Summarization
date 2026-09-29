import { useState } from "react";
import "./App.css";
import axios from "axios";

const contentTypes = [
  { name: "News Article", note: "Headlines, reports, and updates", icon: "01" },
  { name: "Medical Paper", note: "Research and clinical findings", icon: "02" },
  // {
  //   name: "Bills and Acts",
  //   note: "Legislation and legal documents",
  //   icon: "03",
  // },
];

const backendUrl = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

function App() {
  const [contentType, setContentType] = useState(contentTypes[0].name);
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const wordCount = text.trim() ? text.trim().split(/\s+/).length : 0;

  async function handleSummarize() {
    if (!text.trim()) {
      setError("Add some content before generating a summary.");
      return;
    }

    setError("");
    setIsLoading(true);
    setSummary("");

    try {
      const formData = new FormData();
      formData.append("text", text);
      formData.append("type", contentType);
      const response = await axios.post(
        `${backendUrl}/api/summarize`,
        formData,
      );
      const data = await response.data;

      if (data.error)
        throw new Error(data.error || "The summary could not be generated.");
      setSummary(data.summary);
    } catch (requestError) {
      setError(requestError.message || "Unable to connect to the summarizer.");
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <main className="min-h-screen overflow-hidden bg-[#f4f7f2] text-[#18302a]">
      <div className="mx-auto min-h-screen max-w-[1440px] px-5 py-5 sm:px-8 lg:px-12 lg:py-7">
        <nav className="flex items-center justify-between border-b border-[#18302a]/15 pb-5">
          <div className="flex items-center gap-3">
            <div className="grid h-9 w-9 place-items-center rounded-full bg-[#f26745] text-sm font-bold text-white">
              S
            </div>
            <span className="text-sm font-semibold tracking-[0.16em] uppercase">
              Sift / AI
            </span>
          </div>
          <span className="hidden text-xs font-semibold tracking-[0.16em] text-[#18302a]/55 uppercase sm:block">
            Document intelligence
          </span>
          <span className="flex items-center gap-2 text-xs font-medium text-[#18302a]/65">
            <i className="h-2 w-2 rounded-full bg-[#55a66b]" />
            System ready
          </span>
        </nav>

        <section className="grid gap-12 pb-12 pt-14 lg:grid-cols-[1fr_0.82fr] lg:items-end lg:gap-20 lg:pt-20">
          <div>
            <p className="mb-5 flex items-center gap-3 text-xs font-bold tracking-[0.2em] text-[#f26745] uppercase">
              <span className="h-px w-8 bg-[#f26745]" />A clearer read
            </p>
            <h1 className="max-w-3xl font-serif text-5xl leading-[0.98] tracking-[-0.045em] text-[#18302a] sm:text-7xl">
              Turn dense pages into{" "}
              <em className="font-normal text-[#f26745]">clear thinking.</em>
            </h1>
            <p className="mt-7 max-w-xl text-base leading-7 text-[#18302a]/65 sm:text-lg">
              Drop in a document and let Sift surface the signal. Built for the
              stories, studies, and statutes that deserve your full attention.
            </p>
          </div>
          <div className="relative border-l border-[#18302a]/15 pl-7 lg:mb-2">
            <span className="font-serif text-6xl leading-none text-[#f26745]/35">
              “
            </span>
            <p className="-mt-4 max-w-sm font-serif text-2xl leading-snug text-[#18302a]">
              The best summary leaves you with more understanding, not just
              fewer words.
            </p>
          </div>
        </section>

        <section className="border-t border-[#18302a]/15 pt-7">
          <div className="mb-5 flex flex-col justify-between gap-3 sm:flex-row sm:items-end">
            <div>
              <p className="mb-1 text-xs font-bold tracking-[0.16em] text-[#18302a]/45 uppercase">
                01 / Choose a format
              </p>
              <h2 className="font-serif text-2xl">What are you reading?</h2>
            </div>
            <p className="text-sm text-[#18302a]/50">
              The right model makes all the difference.
            </p>
          </div>
          <div className="grid gap-3 md:grid-cols-3">
            {contentTypes.map((type) => (
              <button
                key={type.name}
                type="button"
                onClick={() => setContentType(type.name)}
                className={`group flex items-center justify-between border p-5 text-left transition ${contentType === type.name ? "border-[#18302a] bg-[#18302a] text-[#f4f7f2]" : "border-[#18302a]/15 bg-transparent hover:border-[#18302a]/45"}`}
              >
                <span>
                  <span className="mb-5 block font-mono text-xs text-[#f26745]">
                    {type.icon}
                  </span>
                  <strong className="block text-sm">{type.name}</strong>
                  <span
                    className={`mt-1 block text-xs ${contentType === type.name ? "text-white/55" : "text-[#18302a]/50"}`}
                  >
                    {type.note}
                  </span>
                </span>
                <span
                  className={`grid h-7 w-7 place-items-center rounded-full border text-sm transition ${contentType === type.name ? "border-[#f26745] text-[#f26745]" : "border-[#18302a]/20 text-transparent group-hover:text-[#18302a]/30"}`}
                >
                  ↗
                </span>
              </button>
            ))}
          </div>
        </section>

        <section className="grid gap-4 py-12 lg:grid-cols-2">
          <div className="flex min-h-[410px] flex-col border border-[#18302a]/15 bg-white/45 p-5 sm:p-7">
            <div className="mb-6 flex items-start justify-between">
              <div>
                <p className="mb-1 text-xs font-bold tracking-[0.16em] text-[#18302a]/45 uppercase">
                  02 / Original text
                </p>
                <h2 className="font-serif text-2xl">Your document</h2>
              </div>
              <span className="rounded-full border border-[#18302a]/15 px-3 py-1 text-xs text-[#18302a]/50">
                {wordCount} words
              </span>
            </div>
            <textarea
              value={text}
              onChange={(event) => setText(event.target.value)}
              placeholder="Paste an article, paper, bill, or act here..."
              className="min-h-56 flex-1 resize-none bg-transparent text-base leading-7 text-[#18302a] outline-none placeholder:text-[#18302a]/30"
            />
            <div className="mt-6 flex items-center justify-between border-t border-[#18302a]/10 pt-5">
              <span className="text-xs text-[#18302a]/45">{contentType}</span>
              <button
                type="button"
                onClick={handleSummarize}
                disabled={isLoading}
                className="flex items-center gap-3 bg-[#f26745] px-5 py-3 text-sm font-bold text-white transition hover:bg-[#d95132] disabled:cursor-wait disabled:opacity-60"
              >
                {isLoading ? "Sifting..." : "Generate summary"}{" "}
                <span aria-hidden="true">→</span>
              </button>
            </div>
          </div>
          <div className="flex min-h-[410px] flex-col bg-[#dbe8d7] p-5 sm:p-7">
            <div className="mb-6 flex items-start justify-between">
              <div>
                <p className="mb-1 text-xs font-bold tracking-[0.16em] text-[#18302a]/45 uppercase">
                  03 / Refined version
                </p>
                <h2 className="font-serif text-2xl">Your summary</h2>
              </div>
              {summary && (
                <span className="text-xs font-bold tracking-[0.1em] text-[#55a66b] uppercase">
                  Ready
                </span>
              )}
            </div>
            <div className="flex flex-1 items-center">
              {summary ? (
                <p className="whitespace-pre-wrap text-base leading-7 text-[#18302a]/80">
                  {summary}
                </p>
              ) : (
                <div className="max-w-xs">
                  <span className="mb-5 block text-4xl text-[#55a66b]">✦</span>
                  <p className="font-serif text-2xl leading-snug text-[#18302a]/55">
                    Your summary will appear here, distilled and ready to use.
                  </p>
                </div>
              )}
            </div>
            {error && (
              <p
                role="alert"
                className="mt-6 border-t border-[#d45d46]/30 pt-4 text-sm text-[#b74935]"
              >
                {error}
              </p>
            )}
          </div>
        </section>

        <footer className="flex flex-col justify-between gap-3 border-t border-[#18302a]/15 py-6 text-xs text-[#18302a]/45 sm:flex-row">
          <span>Sift / AI Document Summarizer</span>
          <span>Thoughtful compression for busy minds.</span>
        </footer>
      </div>
    </main>
  );
}

export default App;

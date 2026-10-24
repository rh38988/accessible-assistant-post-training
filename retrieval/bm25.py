"""Small BM25 retriever over support documentation.

Documents are .md or .txt files in a folder (default: retrieval/docs/).
Optional header lines at the top of each file record where it came from:

    Source: https://support.apple.com/...
    Accessed: 2026-10-24

Each file is split into chunks of about CHUNK_WORDS words so that retrieved
context stays short. BM25 then scores chunks against the user's question.

BM25 in one sentence: a chunk scores higher when it contains the query's
words often (term frequency), when those words are rare across all chunks
(inverse document frequency), with a penalty for very long chunks.

Standard library only. Try it:
    python retrieval/bm25.py "how do I make text bigger on iphone"
"""
import math
import re
import sys
from collections import Counter
from pathlib import Path

CHUNK_WORDS = 180
# English/number words, or single CJK characters (Chinese has no spaces).
TOKEN_RE = re.compile(r"[a-z0-9]+|[一-鿿]")
# Common words that carry no topic. Without this, "how do I ... my ..." matches
# any document that happens to contain "do" or "my".
STOPWORDS = set("""
a an and are as at be but by can could do does for from had has have how i if in
into is it its me my of on or our should so than that the their them then there
these they this to up was we what when where which who why will with would you your
""".split())


def tokenize(text):
    return [t for t in TOKEN_RE.findall(text.lower()) if t not in STOPWORDS]


def split_into_chunks(text, max_words=CHUNK_WORDS):
    """Group paragraphs into chunks of up to max_words words."""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, current, count = [], [], 0
    for p in paragraphs:
        n = len(p.split())
        if current and count + n > max_words:
            chunks.append("\n\n".join(current))
            current, count = [], 0
        current.append(p)
        count += n
    if current:
        chunks.append("\n\n".join(current))
    return chunks


def load_documents(doc_dir):
    """Return a list of chunks: {doc, source, accessed, text}."""
    chunks = []
    for path in sorted(Path(doc_dir).glob("*")):
        if path.suffix not in {".md", ".txt"} or path.name.lower() == "readme.md":
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        meta = {"source": "", "accessed": ""}
        # Read "Source:" / "Accessed:" header lines, then the body.
        while lines and re.match(r"^(source|accessed):", lines[0], re.I):
            key, value = lines.pop(0).split(":", 1)
            meta[key.strip().lower()] = value.strip()
        body = "\n".join(lines)
        for text in split_into_chunks(body):
            chunks.append({"doc": path.name, **meta, "text": text})
    return chunks


class BM25Retriever:
    def __init__(self, doc_dir, k1=1.5, b=0.75):
        self.k1, self.b = k1, b
        self.chunks = load_documents(doc_dir)
        self.tokens = [tokenize(c["text"]) for c in self.chunks]
        self.avg_len = sum(map(len, self.tokens)) / max(len(self.tokens), 1)
        # Document frequency: how many chunks contain each term.
        df = Counter(term for toks in self.tokens for term in set(toks))
        n = len(self.chunks)
        self.idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}

    def score(self, query_tokens, i):
        toks = self.tokens[i]
        tf = Counter(toks)
        norm = self.k1 * (1 - self.b + self.b * len(toks) / self.avg_len)
        return sum(
            self.idf.get(q, 0.0) * tf[q] * (self.k1 + 1) / (tf[q] + norm)
            for q in query_tokens if q in tf
        )

    def search(self, query, k=3):
        q = tokenize(query)
        scored = [(self.score(q, i), i) for i in range(len(self.chunks))]
        scored = [s for s in scored if s[0] > 0]
        scored.sort(reverse=True)
        return [{**self.chunks[i], "score": round(s, 3)} for s, i in scored[:k]]


def format_context(results):
    """Turn retrieved chunks into the text block we put in the system message."""
    parts = []
    for r in results:
        header = f"[{r['doc']}]"
        if r.get("source"):
            header += f" Source: {r['source']} (accessed {r.get('accessed') or 'unknown'})"
        parts.append(f"{header}\n{r['text']}")
    return "\n\n---\n\n".join(parts)


if __name__ == "__main__":
    doc_dir = Path(__file__).parent / "docs"
    query = " ".join(sys.argv[1:]) or "make text bigger iphone"
    for r in BM25Retriever(doc_dir).search(query):
        print(f"{r['score']:>7}  {r['doc']}  {r['text'][:80]!r}")

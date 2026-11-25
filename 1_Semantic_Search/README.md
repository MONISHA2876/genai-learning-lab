# 🧠 Semantic Search

**What if computers could understand what you mean, instead of just matching the words you type?**

That's Semantic Search!

Unlike traditional keyword search, semantic search finds information based on **contextual meaning**, not just exact word matches.

### ⚡ How does it work?

1. **Embeddings:** Convert text into numerical vectors using an embedding model.
2. **Vector Representation:** Similar meanings are represented by vectors that tend to be close in the embedding space.
3. **Cosine Similarity:** Measure how similar two vectors are by comparing their directions.
4. **Retrieval:** Return the document with the highest similarity score.

### 👑 A Little Mathematical Magic

Remember this famous NLP example?

\[
King - Man + Woman \approx Queen
\]

And another one:

\[
Paris - France + Japan \approx Tokyo
\]

Word embeddings can capture interesting relationships like these!

### 🔍 Example

**Query:** `Who has the strongest gravity?`

**Document:** `A black hole's gravity is so strong that light cannot escape.`

Even without exact keyword matching, semantic search understands the relationship and retrieves the relevant document.

### 🛠️ Tech Used

- Python
- Google Gemini Embeddings (`gemini-embedding-001`)
- NumPy
- Scikit-learn (Cosine Similarity)

### 🚀 What's Next?

Semantic search is a fundamental building block of **RAG (Retrieval-Augmented Generation)**, AI chatbots, recommendation systems, and intelligent search engines.

**Words → Vectors → Similarity → Meaningful Results.**
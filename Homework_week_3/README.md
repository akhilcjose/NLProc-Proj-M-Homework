# Retriever Class

Reusable Python class (`Retriever`) that supports vector-based semantic search over text documents using **SentenceTransformers** for embeddings and **FAISS** for fast similarity search. It supports `.txt` and `.pdf` files and is ideal for querying large text corpora semantically.

---

## Implements

- Sentence embeddings using `all-MiniLM-L6-v2`
- Fast nearest neighbor search using FAISS
- Handles `.txt` files
- Customizable text chunking

---

## GithubLInk
https://github.com/akhilcjose/NLProc-Proj-M-Homework

---
## Requirements

This project requires Python 3.10 and the following packages:

```txt
python==3.10
sentence-transformers==2.2.2
faiss-cpu==1.7.4
PyMuPDF==1.23.5
numpy==1.26.4
pickle5==0.0.11




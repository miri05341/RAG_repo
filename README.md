#RAG_repo

## Mini RAG (Python, AI‑oriented)

Download the `Sample_Docs_Markdown` folder from Hugging Face: https://huggingface.co/datasets/vibrantlabsai/Sample_Docs_Markdown

### Task
Build a RAG pipeline in Python that allows a user to ask questions about the documents.

The system should:
- Load all `.md` files
- Split documents into chunks
- Create embeddings
- Index them in a vector store
- Retrieve the top‑k most relevant chunks for a query
- Generate an answer grounded in the retrieved context

### Output requirements
The output should include:
- The generated answer
- Supporting references (file name + chunk id or snippet)


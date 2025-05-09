# Initialize the retriever
from retriever import Retriever


retriever = Retriever()

# Example documents
documents = [
    "Lakshmi is a software engineer known for her contributions to machine learning.",
    "She works at a top tech company and has been recognized for her achievements."
]

# Add the documents to the retriever
retriever.add_documents(documents)

# Query the retriever
query = "Who is Lakshmi?"
results = retriever.query(query, top_k=1)

# Display results
for chunk, score in results:
    print(f"Score: {score:.2f} | Chunk: {chunk}")

def read_text_file(filepath):
    """Function to read content from a text file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Example Usage
retriever = Retriever()

# Read the text file content
file_path = 'C:/Users/Lenov/retriever_project/lakshmi.txt'
document_content = read_text_file(file_path)

# Add the document to the retriever
retriever.add_documents([document_content])

# Query the retriever
query = "who is Lakshmi?"
results = retriever.query(query, top_k=1)

# Display results
for chunk, score in results:
    print(f"Score: {score:.2f} | Chunk: {chunk}")

def read_text_file(filepath):
    """Function to read content from a text file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Example Usage
retriever = Retriever()

# Read the text file content
file_path = 'C:/Users/Lenov/retriever_project/winnie_the_pooh.txt'
document_content = read_text_file(file_path)

# Add the document to the retriever
retriever.add_documents([document_content])

# Query the retriever
query = "can i use this book inside USA?"
results = retriever.query(query, top_k=1)

# Display results
for chunk, score in results:
    print(f"Score: {score:.2f} | Chunk: {chunk}")


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

def create_vector_store(transcript: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=150)
    documents = splitter.create_documents([transcript])
    return FAISS.from_documents(documents, embeddings)

# def get_retriever(vectorstore):
#     return vectorstore.as_retriever(search_kwargs={"k": 6})

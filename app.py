from fastapi import FastAPI
from pydantic import BaseModel

from transcript import get_transcript
from vectorstore import create_vector_store
from rag_pipeline import build_chain
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    video_id: str
    question: str

@app.post("/ask")
def ask_video(query: Query):
    transcript = get_transcript(query.video_id)
    vector_store = create_vector_store(transcript)
    retriever = vector_store.as_retriever(search_kwargs={"k": 6})

    chain = build_chain(retriever)
    answer = chain.invoke(query.question)

    return {"answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

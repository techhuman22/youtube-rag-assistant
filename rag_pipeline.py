from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from config import llm

prompt = PromptTemplate(
    template="""
You are an AI assistant that answers questions about a YouTube video.

Use the transcript context below to answer as clearly and helpfully as possible.
Summarize or explain when appropriate.

If the transcript does not contain the answer, say:
"The video does not mention this."

Transcript context:
{context}

Question: {question}

Answer:
""",
    input_variables=["context", "question"]
)

parser = StrOutputParser()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def build_chain(retriever):
    return (
        RunnableParallel(
            context=retriever | RunnableLambda(format_docs),
            question=RunnablePassthrough()
        )
        | prompt
        | llm
        | parser
    )

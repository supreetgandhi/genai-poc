from langchain.tools.retriever import create_retriever_tool

def retriever_tool(retriever):
    retriever_tool = create_retriever_tool(
        retriever,
        "retrieve documents in pdf, xls, txt",
        "Search and return the most relevant information about posts.",
    )


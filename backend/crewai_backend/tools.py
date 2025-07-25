from langchain.agents import Tool
from langchain_community.document_loaders import UnstructuredFileLoader

# def parse_document(doc_path: str) -> str:
#   with open(doc_path, 'r', encoding='utf-8', errors='ignore') as f:
#       return f.read()
  

def parse_document(doc_path: str):
    loader = UnstructuredFileLoader(doc_path)
    docs = loader.load()

    return docs[0].page_content



def read_doc_tool():

    read_docs_tool = Tool(
        name="parse_document",
        func=parse_document,
        description="A tool can read the documents",
    )

    return read_docs_tool
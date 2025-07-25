from crewai import Agent
from .tools import read_doc_tool



def read_doc_agent(llm_model):

    tool = read_doc_tool()

    read_doc_agent = Agent(
        role="Read Document Agent",
        goal="To read a document that is provided to be passed to the summarization agent",
        backstory="This agent designed to help in reading the documents to be passed to the summerization agent",
        llm=llm_model,
        tools=[tool],
        verbose=True
    )

    return read_doc_agent



def summarization_agent(llm_model):
    summarize_agent = Agent(
        role="Summarizer",
        goal="Summarize content and generate 3 follow-up questions",
        backstory="You're a simple assistant that can summarize the content and generate follow-up questions.",
        llm=llm_model,
        tools=[],
        verbose=True
    )

    return summarize_agent
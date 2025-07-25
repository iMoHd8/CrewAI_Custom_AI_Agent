from crewai import Task
from .agents import read_doc_agent, summarization_agent
from .output_format import AllSearchResults



def read_docs_task(llm_model):

    agent = read_doc_agent(llm_model)

    read_doc_task = Task(
        description="""The user is looking to read this document {doc_path}. 
                    The user wants the content in the document to passed them into a summarization agent next step.""",
        
        expected_output="Summary + follow-up questions",
        agent=agent,
        output_json=AllSearchResults
    )

    return read_doc_task



def summarization_task(llm_model):

    agent = summarization_agent(llm_model)

    summarize_task = Task(
        description="""The user is looking to summrize the content of the ducument. 
                    The user is looking for a follow-up questions that are related to the content.
                    The user wants the summary first and then the follow-up questions.""",
        
        expected_output="Summary + follow-up questions",
        agent=agent
    )

    return summarize_task
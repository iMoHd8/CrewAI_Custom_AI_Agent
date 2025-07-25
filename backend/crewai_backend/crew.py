from crewai import Crew, LLM
from .agents import read_doc_agent, summarization_agent
from .tasks import read_docs_task, summarization_task
from .config import LLM_MODEL_ID
from dotenv import load_dotenv
load_dotenv()
import os



def initiat_model(model_id: str=LLM_MODEL_ID):
    llm = LLM(
        model= model_id,
        api_key= os.getenv("GEMINI_API_KEY")
    )

    return llm


def initiat_crew(model):

    crew = Crew(
        agents=[
            read_doc_agent(model),
            summarization_agent(model)
        ],

        tasks=[
            read_docs_task(model),
            summarization_task(model)
        ]
    )

    return crew



def get_crew_results(doc_path: str):

    model = initiat_model()

    crew = initiat_crew(model)

    results = crew.kickoff(
        inputs={
            "doc_path": f"{doc_path}",
        }
    )

    return results

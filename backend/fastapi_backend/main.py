from fastapi import FastAPI
from pydantic import BaseModel
from backend.crewai_backend.crew import get_crew_results

class AgentRequest(BaseModel):
    doc_path: str

app = FastAPI()

@app.post("/run-agent")
def run_agent(doc_path: AgentRequest):
    response = get_crew_results(doc_path)

    return {"response": response.model_dump().get('raw')}
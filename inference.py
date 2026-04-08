from fastapi import FastAPI
from pydantic import BaseModel
from env import TrafficEnv

app = FastAPI()

envs = {}

class ResetRequest(BaseModel):
    level: str = "easy"

class StepRequest(BaseModel):
    action: int
    session_id: str = "default"

@app.post("/reset")
def reset(req: ResetRequest):
    env = TrafficEnv(level=req.level)
    state = env.reset()
    envs[req.level] = env
    return {"state": state}

@app.get("/state")
def get_state(level: str = "easy"):
    if level not in envs:
        return {"error": "No env found. Call /reset first."}
    return {"state": envs[level].state_fn()}

@app.post("/step")
def step(req: StepRequest):
    level = req.session_id if req.session_id in envs else "easy"
    if level not in envs:
        return {"error": "No env found. Call /reset first."}
    state, reward, done = envs[level].step(req.action)
    return {"state": state, "reward":

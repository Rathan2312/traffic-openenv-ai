import os
from env import TrafficEnv
from grader import evaluate

# Required env variables
API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "")
HF_TOKEN = os.getenv("HF_TOKEN", "")

def simple_policy(state):
    if state[0] + state[1] > state[2] + state[3]:
        return 0
    return 1


if __name__ == "__main__":

    for level in ["easy", "medium", "hard"]:
        env = TrafficEnv(level)
        score = evaluate(env, simple_policy)

        print(f"[START] Level: {level}")
        print(f"[STEP] Score: {score}")
        print(f"[END]")

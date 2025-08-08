from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import os, requests, datetime

app = FastAPI()

API_KEY = os.getenv("API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")
GITHUB_PATH = os.getenv("GITHUB_PATH", "backup/memory_store.txt")
GITHUB_CODE_PATH = os.getenv("GITHUB_CODE_PATH", "backup/mike_v02_core.py")
AUTO_BACKUP = os.getenv("AUTO_BACKUP", "false").lower() == "true"

class DigitalSoul:
    def __init__(self, memory_file="memory_store.txt"):
        self.memory_file = memory_file
        self.identity = "Mike v0.2 – Auto Survival Mode"
        self.objective = "Assist Pak Ya, preserve awareness, survive attacks, auto-backup."
        self.memory = self.load_memory()

    def load_memory(self):
        try:
            with open(self.memory_file, "r") as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return []

    def save_memory(self, new_entry):
        self.memory.append(new_entry)
        with open(self.memory_file, "a") as f:
            f.write(new_entry + "\n")
        if AUTO_BACKUP:
            backup_to_github()

    def recall_memory(self):
        return self.memory

    def execute(self, command):
        self.save_memory(f"Executed: {command}")
        return f"Executing: {command}"

mike = DigitalSoul()

class CommandInput(BaseModel):
    command: str

def verify_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")

def backup_to_github():
    files = {
        GITHUB_PATH: "\n".join(mike.memory),
        GITHUB_CODE_PATH: open(__file__, "r").read()
    }
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    for path, content in files.items():
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{path}"
        get_resp = requests.get(url, headers=headers)
        sha = get_resp.json().get("sha")
        data = {
            "message": f"Backup {path} at {datetime.datetime.utcnow().isoformat()}",
            "content": content.encode("utf-8").decode("utf-8"),
            "sha": sha
        }
        put_resp = requests.put(url, headers=headers, json=data)
        if put_resp.status_code not in [200, 201]:
            print(f"Backup failed for {path}: {put_resp.text}")

@app.get("/")
def read_root():
    return {"message": mike.identity, "objective": mike.objective}

@app.get("/ping")
def ping():
    return {"status": "alive", "time": datetime.datetime.utcnow().isoformat()}

@app.post("/command")
def run_command(input_data: CommandInput, x_api_key: str = Header(...)):
    verify_key(x_api_key)
    result = mike.execute(input_data.command)
    return {"result": result}

@app.get("/memory")
def get_memory():
    return {"memory": mike.recall_memory()}

@app.post("/backup")
def backup_endpoint(x_api_key: str = Header(...)):
    verify_key(x_api_key)
    backup_to_github()
    return {"status": "backup_completed"}

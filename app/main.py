from fastapi import FastAPI

app = FastAPI(
    title="Vigil-Drift API Gateway",
    description="An AI firewall gateway for mitigating indirect prompt injection and jailbreaks in LLM systems.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "project": "Vigil-Drift",
        "sdg": "Industry, Innovation and Infrastructure (SDG 9)",
        "status": "Foundation Initialized"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="LLM Gateway Service",
    version="1.0.0",
    description="A service to manage and interact with multiple LLM providers via a unified API.",
)

app.include_router(router)


@app.get("/health")
async def health_check():
    return {"status": "ok"}

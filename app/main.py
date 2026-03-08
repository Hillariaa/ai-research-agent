from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Research Agent")


@app.get("/")
def root():
    return {"message": "AI Research Agent API is running"}


app.include_router(router)

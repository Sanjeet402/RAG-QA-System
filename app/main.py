from fastapi import FastAPI
from app.api.routes import router
import uvicorn

app = FastAPI(title="RAG-Based Q&A System")

app.include_router(router, prefix="/api", tags=["RAG Q&A"])

@app.get("/")
def root():
    return {"message": "Welcome to the RAG-based Q&A System!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

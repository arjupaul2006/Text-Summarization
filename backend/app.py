from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.summarization import router

app = FastAPI(title="AI Document Summarizer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


@app.get("/")
def root():
    return {"message": "AI Document Summarizer API is running"}
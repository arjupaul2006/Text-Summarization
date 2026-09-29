from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.model_manager import ModelManager
from routes.summarization import router

load_dotenv()

FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:5173')


# --------------------------------------------------
# Lifespan
# --------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Starting AI Document Summarizer...")

    # Create ModelManager
    app.state.model_manager = ModelManager()

    # Load all Hugging Face models
    print("Loading all Hugging Face models...")

    app.state.model_manager.load_all_models()

    print("All models loaded successfully.")
    print("FastAPI is ready.")

    # Application runs here
    yield

    # Runs when FastAPI shuts down
    print("Shutting down AI Document Summarizer...")


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="AI Document Summarizer",
    lifespan=lifespan
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        # Add your deployed frontend URL here
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Routes
# --------------------------------------------------

app.include_router(
    router,
    prefix="/api"
)


# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "AI Document Summarizer API is running"
    }


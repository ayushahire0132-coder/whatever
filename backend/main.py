from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import todos

app = FastAPI(
    title="Todo Application API",
    description="A robust FastAPI Todo application with complete CRUD operations.",
    version="1.0.0"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(todos.router)

@app.get("/", tags=["root"])
def read_root():
    """
    Root health check endpoint.
    """
    return {
        "message": "Welcome to the FastAPI Todo Application API!",
        "docs_url": "/docs",
        "health": "healthy"
    }

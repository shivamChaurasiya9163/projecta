from contextlib import asynccontextmanager
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ================================
# Database
# ================================
from app.database.base import Base
from app.database.session import engine

# ================================
# Import ALL Models
# ================================
from app.models.user import User
# from app.models.role import Role
# from app.models.permission import Permission

# ================================
# Import Routers
# ================================
from app.api.v1.auth.router import router as auth_router
from app.api.v1.chat.router import router as chat_router



# ===========================================
# Startup & Shutdown
# ===========================================

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("🚀 Starting SGENOVIX Backend...")

    # Create Database Tables
    Base.metadata.create_all(bind=engine)

    print("✅ Database Connected")
    print("✅ Tables Created")

    yield

    print("🛑 Shutting Down Backend...")


# ===========================================
# FastAPI App
# ===========================================

app = FastAPI(
    title="SGENOVIX API",
    description="""
# SGENOVIX Backend API

Enterprise SaaS Platform

## Modules

- Authentication
- User Management
- CRM
- ERP
- HRMS
- Finance
- AI

Version **1.0.0**
""",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "Frontend"

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")
 
app.include_router(
    chat_router,
    prefix="/api/v1/chat",
    tags=["Chatbot"]
)
# ===========================================
# CORS
# ===========================================

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:8000",

    "http://localhost:5173",
    "http://127.0.0.1:5173",
    
    "http://localhost:5500",
    "http://127.0.0.1:50586",

    "http://localhost:5500",
    "http://127.0.0.1:5500",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===========================================
# Home
# ===========================================
# ===========================================
# Home
# ===========================================

@app.get("/", include_in_schema=False)
async def home():
    return FileResponse(FRONTEND_DIR / "index.html")


# ===========================================
# Health Check
# ===========================================



@app.get("/health", tags=["Health"])
async def health():

    return {
        "status": "Healthy"
    }


# ===========================================
# Authentication Routes
# ===========================================

app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Authentication"]
)
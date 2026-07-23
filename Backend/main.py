from contextlib import asynccontextmanager

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
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
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

@app.get("/", tags=["Home"])
async def home():

    return {
        "success": True,
        "application": "SGENOVIX",
        "version": "1.0.0",
        "message": "Backend Running Successfully"
    }


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
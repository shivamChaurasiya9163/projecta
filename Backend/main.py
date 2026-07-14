from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import Routers
from app.api.v1.auth.router import router as auth_router

app = FastAPI(
    title="SGENOVIX API",
    description="""
## SGENOVIX Backend API

Enterprise SaaS Platform

Modules
- Authentication
- User Management
- Employee Management
- CRM
- ERP
- AI
- Finance

Version: 1.0.0
""",
    version="1.0.0",
    contact={
        "name": "SGENOVIX",
        "email": "support@sgenovix.com",
        "url": "https://sgenovix.com",
    },
    license_info={
        "name": "Proprietary",
    },
    docs_url="/docs",
    redoc_url="/redoc",
)

##############################################################
# CORS
##############################################################

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

##############################################################
# Startup Event
##############################################################

@app.on_event("startup")
async def startup():
    print("🚀 SGENOVIX Backend Started")

##############################################################
# Shutdown Event
##############################################################

@app.on_event("shutdown")
async def shutdown():
    print("🛑 SGENOVIX Backend Stopped")

##############################################################
# Root API
##############################################################

@app.get("/", tags=["Home"])
async def home():
    return {
        "success": True,
        "message": "Welcome to SGENOVIX API",
        "version": "1.0.0"
    }

##############################################################
# Health Check
##############################################################

@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "healthy"
    }

##############################################################
# Register Routers
##############################################################

app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Authentication"]
)
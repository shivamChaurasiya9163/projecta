from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import SignupRequest, LoginRequest
from app.database.session import get_db
from app.api.v1.auth.controller import AuthController

router = APIRouter()


# ==========================
# SIGNUP
# ==========================
@router.post("/signup")
async def signup(
    request: SignupRequest,
    db: Session = Depends(get_db)
):
    return AuthController.signup(request, db)


# ==========================
# LOGIN
# ==========================
@router.post("/login")
async def login(request: LoginRequest):
    return {
        "success": True,
        "message": "Login API Working",
        "request": request.model_dump()
    }


# ==========================
# LOGOUT
# ==========================
@router.post("/logout")
async def logout():
    return {
        "success": True,
        "message": "Logout API Working"
    }


# ==========================
# REFRESH TOKEN
# ==========================
@router.post("/refresh-token")
async def refresh_token():
    return {
        "success": True,
        "message": "Refresh Token API Working"
    }


# ==========================
# FORGOT PASSWORD
# ==========================
@router.post("/forgot-password")
async def forgot_password(request: LoginRequest):
    return {
        "success": True,
        "message": "Forgot Password API Working",
        "email": request.email
    }


# ==========================
# RESET PASSWORD
# ==========================
@router.post("/reset-password")
async def reset_password():
    return {
        "success": True,
        "message": "Reset Password API Working"
    }


# ==========================
# SEND OTP
# ==========================
@router.post("/send-otp")
async def send_otp(request: LoginRequest):
    return {
        "success": True,
        "message": "Send OTP API Working",
        "email": request.email
    }


# ==========================
# VERIFY OTP
# ==========================
@router.post("/verify-otp")
async def verify_otp():
    return {
        "success": True,
        "message": "Verify OTP API Working"
    }


# ==========================
# VERIFY EMAIL
# ==========================
@router.post("/verify-email")
async def verify_email():
    return {
        "success": True,
        "message": "Verify Email API Working"
    }


# ==========================
# CURRENT USER
# ==========================
@router.get("/me")
async def get_me():
    return {
        "success": True,
        "message": "Current User API Working"
    }
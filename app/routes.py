from fastapi import APIRouter
from app.endpoints import home, dashboard

router = APIRouter()

router.include_router(home.router)
router.include_router(dashboard.router)

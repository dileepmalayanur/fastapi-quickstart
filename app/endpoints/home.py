from fastapi import APIRouter

router = APIRouter(
    tags=["Home"],
    responses={404: {"description": "Not found"}},
)

@router.get("/health")
async def health():
    return {"status": "success"}

@router.post("/register")
async def register():
    return {"status": "success"}

@router.post("/login")
async def login():
    return {"status": "success"}

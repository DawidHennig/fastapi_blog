from fastapi import APIRouter


router = APIRouter()

@router.get("/register")
async def register_get():
    ...


@router.post("/register")
async def register_post():
    ...


@router.get("/login")
async def login_get():
    ...


@router.post("/login")
async def login_post():
    ...

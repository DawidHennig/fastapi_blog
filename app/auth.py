from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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

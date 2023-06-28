
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi import responses
from fastapi import status
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.templating import Jinja2Templates
from schemas.jobs import JobCreate
from sqlalchemy.orm import Session
from webapps.jobs.forms import JobCreateForm


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request}
    )

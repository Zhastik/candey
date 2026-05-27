from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

app = FastAPI(
    title="ХолодСамара",
    description="Простой сайт услуг по обслуживанию кондиционеров в Самаре",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


SERVICES = [
    {
        "title": "Чистка кондиционера",
        "description": "Разборка внутреннего блока, промывка фильтров, обработка испарителя и дренажа.",
        "price": "от 2 000 ₽",
    },
    {
        "title": "Заправка фреоном",
        "description": "Проверка давления, поиск явных утечек, дозаправка системы хладагентом.",
        "price": "от 2 500 ₽",
    },
]

REVIEWS = [
    {
        "name": "Алексей",
        "text": "Быстро приехали, почистили кондиционер, стало заметно тише и холоднее.",
        "rating": 5,
    },
    {
        "name": "Марина",
        "text": "Нужно было срочно дозаправить фреон. Всё сделали в тот же день.",
        "rating": 5,
    },
    {
        "name": "Игорь",
        "text": "Понравилось, что заранее назвали цену и ничего лишнего не навязывали.",
        "rating": 5,
    },
]

COVERAGE = [
    "Самара",
    "Новокуйбышевск",
    "Кинель",
    "Красный Яр",
    "Волжский",
    "Курумоч",
    "Управленческий",
    "Мехзавод",
    "Южный город",
]

MASTERS = [
    {
        "name": "Данил",
        "role": "Мастер по чистке и диагностике",
        "photo": "/static/images/master_1.svg",
    },
    {
        "name": "Артём",
        "role": "Мастер по чистке и диагностике",
        "photo": "/static/images/master_2.svg",
    },
]


class LeadRequest(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    phone: str = Field(min_length=5, max_length=30)
    message: str = Field(default="", max_length=500)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "services": SERVICES,
            "reviews": REVIEWS,
            "coverage": COVERAGE,
            "masters": MASTERS,
            "phone": "+7 987 958 32 00 ",
        },
    )


@app.get("/api/services")
async def get_services():
    return SERVICES


@app.get("/api/reviews")
async def get_reviews():
    return REVIEWS


@app.get("/api/coverage")
async def get_coverage():
    return COVERAGE


@app.post("/api/lead")
async def create_lead(lead: LeadRequest):
    # В реальном проекте тут можно сохранить заявку в БД или отправить в Telegram.
    return JSONResponse(
        {
            "ok": True,
            "message": f"{lead.name}, заявка принята. Мы перезвоним по номеру {lead.phone}.",
        }
    )

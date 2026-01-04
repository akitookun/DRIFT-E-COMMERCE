from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from database.helper import (
    fetch_items,
    add_cart_item,
    remove_cart_item,
    get_cart,
    authenticate_user
)


def create_app() -> FastAPI:
    app = FastAPI(
        title="Drift Backend",
        description="FastAPI backend for Drift e-commerce",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.mount(
        "/static",
        StaticFiles(directory="src/static"),
        name="static",
    )

    templates = Jinja2Templates(directory="src/templates")

    @app.get("/", response_class=HTMLResponse)
    async def home(request: Request):
        return templates.TemplateResponse(
            "index.html",
            {"request": request},
        )

    @app.get("/explore", response_class=HTMLResponse)
    async def explore(request: Request):
        return templates.TemplateResponse(
            "explore.html",
            {"request": request},
        )

    @app.get("/cart", response_class=HTMLResponse)
    async def cart(request: Request):
        return templates.TemplateResponse(
            "cart.html",
            {"request": request},
        )

    @app.get("/login", response_class=HTMLResponse)
    async def login(request: Request):
        return templates.TemplateResponse(
            "login.html",
            {"request": request},
        )

    @app.get("/api/items")
    async def get_items(search: str = None, sort: str = None):
        return await fetch_items(search=search, sort=sort)

    @app.post("/api/cart/add")
    async def add_to_cart(data: dict = Body(...)):
        await add_cart_item("demo_user", data["item_id"])
        return {"status": "added"}

    @app.delete("/api/cart/remove")
    async def remove_from_cart(data: dict = Body(...)):
        await remove_cart_item("demo_user", data["item_id"])
        return {"status": "removed"}

    @app.get("/api/cart")
    async def cart_items():
        items, total = await get_cart("demo_user")
        return {"items": items, "total": total}

    @app.post("/api/login")
    async def login_user(data: dict = Body(...)):
        user = await authenticate_user(data["email"], data["password"])
        if not user:
            return {"error": "Invalid credentials"}
        return {"status": "success"}

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )

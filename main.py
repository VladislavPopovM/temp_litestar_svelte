from pathlib import Path
from litestar import Litestar, get, MediaType
from litestar.static_files import create_static_files_router
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ASSETS_DIR = Path("static")


def on_startup():
    ASSETS_DIR.mkdir(exist_ok=True)
    ASSETS_DIR.joinpath("hello.txt").write_text("Hello, world!")

# Маршрут для корневого URL, возвращающий index.html
@get("/", media_type=MediaType.HTML)
async def index() -> str:
    with open("static/index.html", "r", encoding="utf-8") as f:
        return str(f.read())

@get(path="/page", media_type=MediaType.HTML)
async def health_check() -> str:
    return """
    <html>
        <body>
            <div>
                <span>Hello World!</span>
            </div>
        </body>
    </html>
    """


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


app = Litestar(
    route_handlers=[
        create_static_files_router(path="/static", directories=["static"]),
        index, 
        get_book, 
        health_check
    ],
    on_startup=[on_startup],
)
from fastapi import APIRouter

router = APIRouter(tags=["hello"])


@router.get("/")
async def hello_world():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def hello_name(name: str):
    return {"message": f"Hello {name}"}

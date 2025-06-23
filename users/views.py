from fastapi import APIRouter

router = APIRouter()

@router.get("/users/", include_in_schema=True)
def get_users():
    return {"users": ["Alice", "Bob"]}

@router.get("/users/test/", include_in_schema=True)
def test_users():
    return {"test": "ok"}
from fastapi import APIRouter
import traceback
from users.schemas import CreateUser
from users import crud


router = APIRouter(prefix="/users")

@router.post("/create_user/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)

@router.get("/{user_id}/info/")
def info_user(user_id: int):
    return crud.get_user(user_id)

@router.get("/all_users/")
def get_all_users():
    return  crud.get_all_users()

@router.post("/{user_id}/update_recomends/")
def update_recomendations(user_id: int):
    try:
        crud.update_recommends(user_id)
        return {"msg": "Ok"}
    except:
        traceback.print_exc()
        return {'msg': "error"}


@router.get("/{user_id}/get_recomends_profile/")
def get_rec_profile(user_id: int):
    return crud.get_recomend_profile(user_id)

@router.post("/{user_id}/update/image/")
def update_image(user_id:int, image:str):
    return crud.update_image(user_id, image)

@router.post("/{user_id}/update/name/")
def update_image(user_id:int, name:str):
    return crud.update_name(user_id, name)

@router.post("/{user_id}/update/games/")
def update_image(user_id:int, games:str):
    return crud.update_games(user_id, games)

@router.post("/{user_id}/update/age/")
def update_image(user_id:int, age:int):
    return crud.update_age(user_id, age)

@router.post("/{user_id}/update/description/")
def update_image(user_id:int, description:str):
    return crud.update_description(user_id, description)
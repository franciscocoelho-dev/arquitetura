from fastapi import APIRouter, status, HTTPException
from db import USERS
from utils.generator_id import gerar_id
from schemas.users import UserListSchema, UserPublicSchema, UserSchema, UserUpdateSchema

router = APIRouter()
contador_id = 0

@router.get(path = '/', response_model = UserListSchema, status_code = status.HTTP_200_OK)
def user_list():
    return {'users': USERS}


@router.post(path='/', response_model=UserPublicSchema, status_code = status.HTTP_201_CREATED)
def user_add(user: UserSchema):
    user_new = UserPublicSchema(**user.model_dump(), id = gerar_id())
    USERS.append(user_new)
    return user_new

@router.put(
    path='/{id_user}',
    response_model=UserPublicSchema,
    status_code=status.HTTP_201_CREATED
)
def user_update(user: UserSchema, id_user: int):
    updated_user = UserPublicSchema(**user.model_dump(), id = id_user)

    for index, item in enumerate(USERS):
        if item.id == id_user:
            USERS[index] = updated_user
            return updated_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ID User não encontrado')
    
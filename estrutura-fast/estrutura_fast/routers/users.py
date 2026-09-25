from fastapi import APIRouter, status, HTTPException
from db import USERS
from utils.generator_id import gerar_id
from schemas.users import UserListSchema, UserPublicSchema, UserSchema, UserUpdateSchema


router = APIRouter()


@router.get(
    path = '/',
    response_model = UserListSchema,
    status_code = status.HTTP_200_OK
)
def user_get():
    return {'users': USERS}


@router.post(
    path='/',
    response_model=UserPublicSchema,
    status_code = status.HTTP_201_CREATED
)
def user_post(user: UserSchema):
    user_new = UserPublicSchema(**user.model_dump(), id = gerar_id())
    USERS.append(user_new)
    return user_new


@router.put(
    path='/{id_user}',
    response_model=UserPublicSchema,
    status_code=status.HTTP_201_CREATED
)
def user_put(user: UserSchema, id_user: int):
    updated_user = UserPublicSchema(**user.model_dump(), id = id_user)

    for index, item in enumerate(USERS):
        if item.id == id_user:
            USERS[index] = updated_user
            return updated_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ID User não encontrado')


@router.patch(
    path='/{id_user}',
    response_model=UserPublicSchema,
    status_code=status.HTTP_200_OK
)
def user_patch(user: UserUpdateSchema, id_user: int):
    for index, item in enumerate(USERS):
        if item.id == id_user:
            # Pegar SOMENTE os dados a serem atualizados
            update_data = user.model_dump(exclude_unset=True)
            # Criou uma cópia de atualização mudando apenas os dados alterados pelo usuário
            updated_user = item.model_copy(update = update_data)
            # Inserir os novos dados do usuário no indice dele na lista por meio do index do enumerate()
            USERS[index] = updated_user
            return updated_user
        # Retorna uma exception se o ID não for encontrado
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ID User não encontrado') 


@router.delete(
    path='/{id_user}',
    status_code=status.HTTP_204_NO_CONTENT
)
def user_delete(id_user: int):
    for index, item in enumerate(USERS):
        if item.id == id_user:
            del USERS[index]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ID User não encontrado') 

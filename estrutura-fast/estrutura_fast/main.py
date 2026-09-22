from fastapi import FastAPI
from routers.users import router

app = FastAPI()
app.include_router(
    router = router,
    prefix = '/api/users',
    tags = ['users',]
)



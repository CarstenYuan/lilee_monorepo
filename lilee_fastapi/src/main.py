from fastapi import FastAPI
from uvicorn import run as uvicorn_run
from fastapi.middleware.cors import CORSMiddleware

from controllers.users import users_statistic_router

app = FastAPI(title='LiLee Web Server APIs', docs_url='/swagger')
app.include_router(users_statistic_router)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn_run('main:app', host='0.0.0.0', port=9000, reload=True)

from fastapi import FastAPI

from api.routers import task, done,row

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)
app.include_router(row.router)
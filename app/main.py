from fastapi import FastAPI
from api.routes import router
from core.scheduler import start_scheduler


app=FastAPI(
    title="translation data exchange manager",
    version="1.0.0"
)

app.include_router(router)


@app.on_event("startup")
def startup_event():
    start_scheduler()
from fastapi import FastAPI
from routers import clustering, frequent_pattern_mining

app = FastAPI()
app.include_router(frequent_pattern_mining.router)
app.include_router(clustering.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}

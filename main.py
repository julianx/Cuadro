from typing import Annotated

from fastapi import Depends
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
async def root():
    return {"message": "Hello World from cuadro!"}


@app.get("/secure/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

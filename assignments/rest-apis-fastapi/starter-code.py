from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


# Armazenamento em memória: {id: Item}
items: dict[int, Item] = {}

# Crie suas rotas abaixo.

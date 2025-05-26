import logging
import os
import re

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import RedirectResponse

app = FastAPI()


load_dotenv(".private.env")

logging.basicConfig(level='INFO')
logging.getLogger(re.sub(r"\.app$", "", __name__))\
    .setLevel(os.getenv('LOGGING_LEVEL', 'INFO'))


@app.get("/")
async def root():
  return RedirectResponse(url="/docs")


from app.belote.belote import play as play_belote

@app.post("/play")
async def play(request: Request):
    game_state = await request.json()
    result = await play_belote(game_state)
    return {"option": result}

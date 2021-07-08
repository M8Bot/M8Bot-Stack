import logging
import os
import random
import time

import string
import uvicorn
from dataclasses import asdict
from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI, Request, Response
from fastapi_sqlalchemy import DBSessionMiddleware, db

app = FastAPI(
    title="M8 bot's API",
    description="M8 is a open source bot base on Discord.py",
    version="0.0.2",
)

logger = logging.getLogger("fastapi")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# ENV ---------------------------------------------------------------------------------------------
debug = int(os.environ.get('DEBUG', '0')) != 0

# MIDLEWARE ---------------------------------------------------------------------------------------
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.middleware("http")
# @app.middleware("https") # Not supported YET
async def log_requests(request: Request, call_next):
    """Log the request

    :param request: the request made
    :param call_next: the function to call for the request
    :return: the response
    """
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()

    response: Response = await call_next(request)

    logger.info(f"rid={idem} completed_in={(time.time() - start_time) * 1000:.2f}ms status_code={response.status_code}")

    return response


@app.get("/")
def root():
    return {"Hello": "World"}


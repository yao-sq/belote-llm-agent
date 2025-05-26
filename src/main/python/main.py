import logging
import os

import uvicorn

from app import app

if __name__ == "__main__":
    logging.getLogger("").setLevel(os.getenv('LOGGING_LEVEL', 'DEBUG'))
    uvicorn.run(app, host="0.0.0.0")
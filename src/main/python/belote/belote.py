import json
import logging
import re

import openai
import pydantic
from pydantic import Field

from llm.openai_client import call as llm_call


logger = logging.getLogger(__name__)


with open('src/main/resources/instructions.txt', 'r') as f:
    game_instructions = f.read()


class LlmPlayResponse(pydantic.BaseModel):
    explanation: str = Field(description="The thoughts and reasoning of why you chose the specific option, along with a detailed explanations and deliberations of all the other options.")
    option: int = Field(description="The zero-based index of the option you chose to play.")

async def play(game_state) -> int:
    logger.info("Playing belote...")

    response = await llm_call(
        instructions=game_instructions,
        input=json.dumps(game_state),
        response_type=LlmPlayResponse
    )

    logger.info("Playing option %s", response.option)
    logger.debug("Play reasoning: %s", response.explanation)
    return response.option
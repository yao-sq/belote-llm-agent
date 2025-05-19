import json
import logging
import re

from llm.openai_client import client as llm


logger = logging.getLogger(__name__)


default_model = "gpt-4o"

with open('src/main/resources/instructions.txt', 'r') as f:
    game_instructions = f.read()


pattern_result = re.compile(r"`\[Option (\d+)] Action:")

async def play(game_state) -> int:
    logger.info("Playing belote...")

    response = await llm.responses.create(
        model=default_model,
        instructions=game_instructions,
        input=json.dumps(game_state)
    )

    logger.debug("Got LLM response: %s", response)

    match = pattern_result.search(response.output_text)
    if match:
        return int(match.group(1))
    else:
        return -1
import logging

from openai import AsyncOpenAI

logger = logging.getLogger(__name__)

llm = AsyncOpenAI()

default_model = "gpt-4o-mini"

async def call(
  input,
  instructions = None,
  response_type = None
):
    if response_type is None:
        response = await llm.responses.create(
            model=default_model,
            instructions=instructions,
            input=input
        )

        logger.debug("Got LLM response: %s", response)
        return response;

    response = await llm.responses.parse(
        model=default_model,
        instructions=instructions,
        input=input,
        text_format=response_type)

    logger.debug("Got LLM response: %s", response)
    return response.output_parsed

from google import genai
from google.genai import types
import logging

logger = logging.getLogger(__name__)

llm = genai.Client()

default_model = "gemini-2.0-flash"

async def call(
  input,
  instructions = None,
  response_type = None
):
    if response_type is None:
        response = llm.models.generate_content(
            model=default_model,
            config=types.GenerateContentConfig(
                system_instruction=instructions
            ),
            contents=input)
    else:
        response = llm.models.generate_content(
            model=default_model,
            config=types.GenerateContentConfig(
                system_instruction=instructions,
                response_mime_type="application/json",
                response_schema=response_type
            ),
            contents=input)
        response = response.parsed

    logger.debug("Got LLM response: %s", response)
    return response

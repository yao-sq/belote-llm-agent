# import logging
#
# from openai import AsyncOpenAI
#
# logger = logging.getLogger(__name__)
#
# llm = AsyncOpenAI()
#
# default_model = "gpt-4o-mini"
#
# async def call(
#   input,
#   instructions = None,
#   response_type = None
# ):
#     if response_type is None:
#         response = await llm.responses.create(
#             model=default_model,
#             instructions=instructions,
#             input=input
#         )
#
#         logger.debug("Got LLM response: %s", response)
#         return response;
#
#     response = await llm.responses.parse(
#         model=default_model,
#         instructions=instructions,
#         input=input,
#         text_format=response_type)
#
#
#
#     # import anthropic
#     #
#     # # FIXME: 1.code does not compile; 2.I need to pay for anthropic?? ...
#     # client = anthropic.Anthropic()
#     # message = client.messages.create(instructions=instructions,
#     #                                  input=input,
#     #                                  tools=tools,
#     #                                  tool_choice=response_type??
#     #
#     #     model="claude-opus-4-20250514",
#     #     max_tokens=1000,
#     #     temperature=1,
#     #     system="You are a world-class poet. Respond only with short poems.",
#     #     messages=[
#     #         {
#     #             "role": "user",
#     #             "content": [
#     #                 {
#     #                     "type": "text",
#     #                     "text": "Why is the ocean salty?"
#     #                 }
#     #             ]
#     #         }
#     #     ]
#     # )
#     # response = await
#
#     logger.debug("Got LLM response: %s", response)
#     return response.output_parsed

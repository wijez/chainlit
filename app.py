from openai import AsyncOpenAI
import chainlit as cl

client = AsyncOpenAI()

cl.instrument_openai()

settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
}
topic = input("Filter (python , postgreSQL, fastapi, Django, AI): ")
prompt = f"You are an expert in {topic} and answer questions related to them., you always reply in Vietnamese"


@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": prompt,
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()

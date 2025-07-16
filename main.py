import chainlit as cl
from search_stackoverflow import search_stackoverflow
from gemini_helper import summarize_answer

@cl.on_message
async def handle_message(message: cl.Message):
    user_query = message.content.strip()
    
    await cl.Message(content="🔎 Searching StackOverflow...").send()
    try:
        results = search_stackoverflow(user_query)
        await cl.Message(content=results).send()

        await cl.Message(content="💡 Summarizing best solution...").send()
        summary = summarize_answer(user_query, results)
        await cl.Message(content=summary).send()
    except Exception as e:
        await cl.Message(content=f"❌ Error: {str(e)}").send()

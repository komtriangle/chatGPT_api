from fastapi import FastAPI
import openai
import uvicorn

app = FastAPI()

openai.api_key = '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'


@app.get("/ask")
async def root(qustion):
    try:
        return get_answer(qustion)
    except:
        return "невалидный токен"


@app.post("/set_token")
async def set_token(token):
    openai.api_key = token


def get_answer(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
        ]
    )
    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")

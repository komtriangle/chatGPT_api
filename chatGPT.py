from fastapi import FastAPI
import openai
import uvicorn

app = FastAPI()

prompt = "user"
openai.api_key = ""


@app.get("/ask")
async def root(qustion):
    try:
        return get_answer(qustion)
    except:
        return "невалидный токен"


@app.post("/set_token")
async def set_token(token):
    openai.api_key = token


@app.post("/set_prompt")
async def set_promt(prompt):
    prompt = prompt


def get_answer(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{prompt}. Answer the following question ({question})"},
        ]
    )
    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")

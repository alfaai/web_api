from typing import Union
from fastapi import FastAPI
import inference_replicate as infrence

app = FastAPI()


@app.post("/sticker")
def sticker(prompt):
    output = infrence.sticker(prompt)
    return output


@app.post("/pulid")
def sticker(prompt, image):
    output = infrence.pulid(image, prompt)
    return output

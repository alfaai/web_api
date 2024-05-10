from typing import Union
from fastapi import FastAPI
import inference_replicate as infrence


app = FastAPI()


@app.get("/sticker")
def sticker(prompt):
    output = infrence.sticker(prompt)
    return output


@app.get("/pulid")
def sticker(prompt, image):
    output = infrence.pulid(image, prompt)
    return output

from fastapi import FastAPI
from pydantic import BaseModel
from Inference.prediction import Classifier
from Utils import config
import uvicorn

class Message(BaseModel):
    text: list

model_dir = config.MODEL_DIR
classifier = Classifier(model_dir)

app = FastAPI()


@app.post("/")
async def home(msg:Message):
    categories, confidence = classifier.predict(msg.text)
    return {"category":categories, "confidence":str(confidence)}

    
if __name__=="__main__":    
    uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True)

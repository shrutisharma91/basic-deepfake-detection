from fastapi import APIRouter, File, UploadFile
from app.controllers.predict_controller import predict_image

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    return await predict_image(file)

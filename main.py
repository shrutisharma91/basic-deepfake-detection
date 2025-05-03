from fastapi import FastAPI
from app.routers.predict_router import router as predict_router

app = FastAPI()

# Include the predict router
app.include_router(predict_router)

#uvicorn app.main:app --reload
#uvicorn main:app --host 0.0.0.0 --port 10000
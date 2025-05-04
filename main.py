import os
from fastapi import FastAPI
from app.routers.predict_router import router as predict_router
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Add this below your app = FastAPI() line
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify ["http://localhost:10000"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# Root endpoint for testing
@app.get("/")
def read_root():
    return {"status": "API is running", "endpoints": ["/predict"]}

# Include the predict router
app.include_router(predict_router)

# For local development
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Render's dynamic port
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)



# uvicorn main:app --reload

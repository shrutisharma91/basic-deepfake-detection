import os
from fastapi import FastAPI
from app.routers.predict_router import router as predict_router

app = FastAPI()

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
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)

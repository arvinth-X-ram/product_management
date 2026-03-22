from fastapi import FastAPI
from api.v1.route.product import router as product_router

app = FastAPI(title="Product Management API")

app.include_router(product_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API v1 is active"}

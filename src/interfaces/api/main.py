from fastapi import FastAPI
from interfaces.api.routes import user, product
from repositories.sql_database.connection import engine
from repositories.user_repository import UserModel
from repositories.product_repository import ProductModel

# Create all tables
UserModel.metadata.create_all(bind=engine)
ProductModel.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(product.router, prefix="/products", tags=["Products"])

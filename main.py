from fastapi import FastAPI
from router.user import user_router
from router.book import book_router
from router.borrow_record import borrow_record_router

app = FastAPI(
    title="E-Library API System",
    description="API for managing an online library system. Includes user, book, and borrowing record management.",
    version="1.0.0"
)

app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(borrow_record_router, prefix="/borrow-records", tags=["Borrow Records"])
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def home():
    return {"message": "An E-Library API Management System"}

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


app = FastAPI()


@app.exception_handlers(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # handles validation errors in the application and provides a consistent error response format.
    # JSONResponse gives a custom error response with details about the validation error.
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Validation error occurred",
            "errors": exc.errors(),
            "body": exc.body,
        },
    )
    
    
# general HTTPException handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    
    # handles HTTPExceptions and provides a consistent error response format.
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
            "headers": exc.headers
        },
    )
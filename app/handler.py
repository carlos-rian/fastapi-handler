from fastapi import FastAPI, status, Request

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def init_app(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    def error_handler_validation_request(request: Request, exc: RequestValidationError) -> JSONResponse:
        try:
            if request.url.path == "/login":
                # TODO
                JSONResponse(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    content={"message": "user found"},
                )

            # TODO

        except Exception as e:

            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={"message": "user not found"},
            )

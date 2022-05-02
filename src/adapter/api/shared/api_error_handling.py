from fastapi import HTTPException

from src.domain.api_exception import ApiException


class ApiErrorHandling:

    @staticmethod
    def http_error(error_message: str, exception: Exception) -> HTTPException:
        if isinstance(exception, ApiException):
            return HTTPException(status_code=400, detail=str(exception.message))
        else:
            return HTTPException(status_code=400, detail=error_message)

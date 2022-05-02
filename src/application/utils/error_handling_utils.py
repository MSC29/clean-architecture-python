from src.domain.api_exception import ApiException


class ErrorHandlingUtils:

    @staticmethod
    def application_error(error_message: str, exception: Exception) -> ApiException:
        if isinstance(exception, ApiException):
            return ApiException(str(exception))
        else:
            return ApiException(error_message)

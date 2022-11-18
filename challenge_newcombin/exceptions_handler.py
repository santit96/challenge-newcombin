from django.conf import settings

from django.core.exceptions import ValidationError
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if isinstance(exc, ValidationError):
        return Response (
                    exc,
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                )

    if response is None and not(settings.DEBUG):
        return Response(
                    "An error has ocurred",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


    return response


from fastapi import HTTPException, status


class DatasetNotFound(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Dataset file not found.",
        )

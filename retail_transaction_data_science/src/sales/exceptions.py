from fastapi import HTTPException, status


class InvalidHourRange(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="start_hour must be between 0-23 and less than end_hour.",
        )


class NoDataFound(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No sales data found for the given filters.",
        )

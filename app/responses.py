from typing import Any, Optional


class Response:
    status: str = 'ok'

    def __init__(self, status: Optional[str] = None, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.status = status or self.status

from datetime import datetime
from dataclasses import dataclass


@dataclass
class UserDTO:
    username: str
    first_name: str
    last_name: str
    email: str
    id: int | None = None
    password: str | None = None
    is_superuser: bool | None = None
    is_staff: bool | None = None
    date_joined: datetime | None = None

from pydantic import BaseModel

class Notification(BaseModel):
    id: int
    message: str
    user_id: int
    is_read: bool = False
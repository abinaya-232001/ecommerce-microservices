from fastapi import FastAPI
from models import Notification
from data import notifications

app = FastAPI(title="Notification Service")

# Get all notifications
@app.get("/notifications")
def get_notifications():
    return notifications

# Create new notification
@app.post("/notifications")
def create_notification(notification: Notification):
    notifications.append(notification)
    return {"message": "Notification added", "data": notification}

# Mark as read
@app.put("/notifications/{id}")
def mark_as_read(id: int):
    for n in notifications:
        if n.id == id:
            n.is_read = True
            return {"message": "Marked as read"}
    return {"error": "Notification not found"}
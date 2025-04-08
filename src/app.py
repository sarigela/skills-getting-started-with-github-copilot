"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Swimming": {
        "description": "Learn swimming techniques and participate in water sports",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
    },
    "Kayaking": {
        "description": "Explore kayaking and water navigation skills",
        "schedule": "Saturdays, 10:00 AM - 12:00 PM",
        "max_participants": 10,
        "participants": ["noah@mergington.edu", "ava@mergington.edu"]
    },
    "Rock Climbing": {
        "description": "Learn rock climbing techniques and safety measures",
        "schedule": "Thursdays, 3:00 PM - 5:00 PM",
        "max_participants": 8,
        "participants": ["liam@mergington.edu", "isabella@mergington.edu"]
    },
    "Hiking Club": {
        "description": "Explore nature trails and learn hiking essentials",
        "schedule": "Sundays, 8:00 AM - 12:00 PM",
        "max_participants": 20,
        "participants": ["elijah@mergington.edu", "amelia@mergington.edu"]
    },
    "Archery": {
        "description": "Practice archery skills and participate in competitions",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["james@mergington.edu", "charlotte@mergington.edu"]
    },
    "Shooting Range": {
        "description": "Learn precision shooting and firearm safety",
        "schedule": "Fridays, 5:00 PM - 6:30 PM",
        "max_participants": 10,
        "participants": ["benjamin@mergington.edu", "harper@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]


    # Check email is valid
    if "@" not in email or "." not in email.split("@")[-1]:
        raise HTTPException(status_code=400, detail="Invalid email address")
    # Check email is from Mergington High School
    if not email.endswith("@mergington.edu"):
        raise HTTPException(status_code=400, detail="Email must be from Mergington High School domain")
    # Check email is not empty
    if not email:
        raise HTTPException(status_code=400, detail="Email cannot be empty")

    # Check max participants
    if len(activity["participants"]) >= activity["max_participants"]:
        raise HTTPException(status_code=400, detail="Activity is full")
    
    # Check studient is already signed up

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}

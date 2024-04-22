from pydantic import BaseModel
from datetime import date
from enum import Enum

class AppointmentStatus(Enum):
    ongoing = "ongoing"
    completed = "completed"
    cancelled = "cancelled"

class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: date
    status: str= AppointmentStatus.ongoing.value

class AppointmentCreate(BaseModel):
    patient_id: int
    date: date

appointments = []



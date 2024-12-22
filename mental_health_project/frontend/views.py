import os
from django.shortcuts import render, redirect
import json

data_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'mental_health_system.json')

def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"users": [], "patients": [], "doctors": []}

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def index(request):
    return render(request, 'frontend/index.html')

def add_patient(request):
    if request.method == "POST":
        new_name = request.POST.get("name")
        new_id = request.POST.get("id")
        data = load_data()
        data["patients"].append({"name": new_name, "id": new_id})
        save_data(data)
        return redirect('index')
    return render(request, 'frontend/add_patient.html')

def add_doctor(request):
    if request.method == "POST":
        new_name = request.POST.get("name")
        new_id = request.POST.get("id")
        data = load_data()
        data["doctors"].append({"name": new_name, "id": new_id})
        save_data(data)
        return redirect('index')
    return render(request, 'frontend/add_doctor.html')

def add_user(request):
    if request.method == "POST":
        new_name = request.POST.get("name")
        new_id = request.POST.get("id")
        data = load_data()
        data["users"].append({"name": new_name, "id": new_id})
        save_data(data)
        return redirect('index')
    return render(request, 'frontend/add_user.html')

def view_users(request):
    data = load_data()
    return render(request, 'frontend/view_users.html', {'data': data})

def register_problem(request):
    # Implement the logic for registering a problem
    return render(request, 'frontend/register_problem.html')

def book_therapy_session(request):
    # Implement the logic for booking a therapy session
    return render(request, 'frontend/book_therapy_session.html')

def follow_up(request):
    # Implement the logic for following up with a patient
    return render(request, 'frontend/follow_up.html')

def consult_doctor(request):
    # Implement the logic for consulting a doctor
    return render(request, 'frontend/consult_doctor.html')

def prescribe_medication(request):
    # Implement the logic for prescribing medication
    return render(request, 'frontend/prescribe_medication.html')

def set_sessions(request):
    if request.method == "POST":
        doctor_id = request.POST.get("doctor_id")
        session_details = request.POST.get("session_details")
        data = load_data()
        doctor = next((d for d in data["doctors"] if d["id"] == doctor_id), None)
        if doctor:
            doctor["sessions"] = session_details
            save_data(data)
            return redirect('index')
        else:
            return render(request, 'frontend/set_sessions.html', {'error': 'Doctor not found'})
    return render(request, 'frontend/set_sessions.html')
import json

# Initialize or load data from a JSON file (acting as our database)
data_file = "mental_health_system.json"

def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": [], "patients": [], "doctors": []}

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

# Base User class
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def create_account(self):
        return {"name": self.name, "id": self.user_id}

    def check_profile(self):
        return {"name": self.name, "id": self.user_id}

# Patient class
class Patient(User):
    def __init__(self, name, user_id, age, goal):
        super().__init__(name, user_id)
        self.age = age
        self.goal = goal

    def register_problem(self, problem):
        return f"Problem '{problem}' registered for patient {self.name}."

    def follow_up(self):
        return f"Follow-up scheduled for patient {self.name}."

    def consult_doctor(self, doctor):
        return f"Consultation booked with Dr. {doctor.name}."

    def book_therapy_session(self):
        return f"Therapy session booked for patient {self.name}."

    def view_similar_cases(self):
        return f"Similar cases viewed for patient {self.name}."

# Doctor class
class Doctor(User):
    def __init__(self, name, user_id, age_range):
        super().__init__(name, user_id)
        self.age_range = age_range

    def respond_to_patient(self, patient):
        return f"Responded to patient {patient.name}."

    def prescribe_meds(self, patient):
        return f"Medication prescribed to patient {patient.name}."

    def set_sessions(self, patient):
        return f"Sessions set for patient {patient.name}."

    def review_patient_history(self, patient):
        return f"Patient history reviewed for {patient.name}."

    def update_treatment_plan(self, patient):
        return f"Treatment plan updated for {patient.name}."

    def send_notifications(self, patient):
        return f"Notification sent to patient {patient.name}."

# Main program for interaction
def main():
    data = load_data()
    patients = []  # Temporarily hold Patient objects
    doctors = []   # Temporarily hold Doctor objects

    # Load existing patients and doctors into memory
    for p in data["patients"]:
        patients.append(Patient(p["name"], p["id"], p.get("age", "N/A"), p.get("goal", "N/A")))
    for d in data["doctors"]:
        doctors.append(Doctor(d["name"], d["id"], d.get("age_range", "N/A")))

    while True:
        print("\n--- Mental Health System ---")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. View All Users")
        print("4. Register Problem for a Patient")
        print("5. Book Therapy Session")
        print("6. Follow Up for a Patient")
        print("7. Consult Doctor")
        print("8. Doctor: Prescribe Medication")
        print("9. Doctor: Set Sessions")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter patient name: ")
            user_id = input("Enter patient ID: ")
            age = input("Enter patient age: ")
            goal = input("Enter patient goal: ")
            patient = Patient(name, user_id, age, goal)
            patients.append(patient)
            data["patients"].append(patient.create_account())
            save_data(data)
            print(f"Patient {name} added successfully.")

        elif choice == "2":
            name = input("Enter doctor name: ")
            user_id = input("Enter doctor ID: ")
            age_range = input("Enter age range doctor is responsible for: ")
            doctor = Doctor(name, user_id, age_range)
            doctors.append(doctor)
            data["doctors"].append(doctor.create_account())
            save_data(data)
            print(f"Doctor {name} added successfully.")

        elif choice == "3":
            print("\n--- All Users ---")
            print("Patients:", [p.check_profile() for p in patients])
            print("Doctors:", [d.check_profile() for d in doctors])

        elif choice == "4":
            patient_name = input("Enter patient name: ")
            problem = input("Enter the problem: ")
            patient = next((p for p in patients if p.name == patient_name), None)
            if patient:
                print(patient.register_problem(problem))
            else:
                print("Patient not found!")

        elif choice == "5":
            patient_name = input("Enter patient name: ")
            patient = next((p for p in patients if p.name == patient_name), None)
            if patient:
                print(patient.book_therapy_session())
            else:
                print("Patient not found!")

        elif choice == "6":
            patient_name = input("Enter patient name: ")
            patient = next((p for p in patients if p.name == patient_name), None)
            if patient:
                print(patient.follow_up())
            else:
                print("Patient not found!")

        elif choice == "7":
            patient_name = input("Enter patient name: ")
            doctor_name = input("Enter doctor name: ")
            patient = next((p for p in patients if p.name == patient_name), None)
            doctor = next((d for d in doctors if d.name == doctor_name), None)
            if patient and doctor:
                print(patient.consult_doctor())
                print(doctor.respond_to_patient(patient))
            else:
                print("Patient or doctor not found!")

        elif choice == "8":
            doctor_name = input("Enter doctor name: ")
            patient_name = input("Enter patient name: ")
            meds = input("Enter medication to prescribe: ")
            doctor = next((d for d in doctors if d.name == doctor_name), None)
            if doctor:
                print(doctor.prescribe_meds(patient_name, meds))
            else:
                print("Doctor not found!")

        elif choice == "9":
            doctor_name = input("Enter doctor name: ")
            sessions = input("Enter session details: ")
            doctor = next((d for d in doctors if d.name == doctor_name), None)
            if doctor:
                print(doctor.set_sessions(sessions))
            else:
                print("Doctor not found!")

        elif choice == "10":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

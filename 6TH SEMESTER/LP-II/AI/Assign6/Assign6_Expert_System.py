class MedicalExpertSystem:
    def __init__(self):
        self.rules = {
            "Flu": {
                "symptoms": ["fever", "cough", "sore throat", "fatigue", "body ache"],
                "treatment": "Rest, hydration, over-the-counter medications."
            },
            "COVID-19": {
                "symptoms": ["fever", "cough", "shortness of breath", "loss of taste", "loss of smell"],
                "treatment": "Isolation, oxygen support if severe, antiviral medications."
            },
            "Diabetes": {
                "symptoms": ["frequent urination", "excessive thirst", "fatigue", "blurry vision"],
                "treatment": "Lifestyle changes, insulin or oral medications."
            },
            "Hypertension": {
                "symptoms": ["headache", "dizziness", "chest pain", "shortness of breath"],
                "treatment": "Low-sodium diet, blood pressure medications."
            },
            "Migraine": {
                "symptoms": ["headache", "nausea", "sensitivity to light", "blurred vision"],
                "treatment": "Pain relief medications, rest in a dark room."
            }
        }
        
        self.resources = {
            "beds_available": 5,
            "doctors_available": 3
        }
        
        self.patient_history = {}  # Stores patient records

    def diagnose(self, symptoms):
        """Diagnose possible conditions based on symptoms."""
        scores = {disease: 0 for disease in self.rules}
        
        for disease, details in self.rules.items():
            scores[disease] = sum(1 for symptom in symptoms if symptom in details["symptoms"])
        
        best_match = max(scores, key=scores.get)
        if scores[best_match] > 0:
            return best_match, self.rules[best_match]["treatment"]
        else:
            return "Unknown Condition", "Consult a doctor for further diagnosis."

    def check_resources(self):
        """Check hospital resource availability."""
        return f"Beds Available: {self.resources['beds_available']}, Doctors Available: {self.resources['doctors_available']}"

    def emergency_alert(self, symptoms):
        """Trigger emergency alert for critical symptoms."""
        critical_conditions = ["chest pain", "shortness of breath", "severe headache"]
        if any(symptom in critical_conditions for symptom in symptoms):
            return " EMERGENCY ALERT! Immediate medical attention needed!"
        return "No emergency detected."

    def store_patient_history(self, name, symptoms, diagnosis, treatment):
        """Store patient history."""
        if name in self.patient_history:
            self.patient_history[name].append({"Symptoms": symptoms, "Diagnosis": diagnosis, "Treatment": treatment})
        else:
            self.patient_history[name] = [{"Symptoms": symptoms, "Diagnosis": diagnosis, "Treatment": treatment}]
        print(f" Patient history updated for {name}.")

    def get_patient_history(self, name):
        """Retrieve patient history."""
        if name in self.patient_history:
            print(f"\n Patient History for {name}:")
            for i, record in enumerate(self.patient_history[name], 1):
                print(f"\nRecord {i}:")
                print(f"Symptoms: {', '.join(record['Symptoms'])}")
                print(f"Diagnosis: {record['Diagnosis']}")
                print(f"Treatment: {record['Treatment']}")
        else:
            print(f"\n No history found for {name}.")

# Initialize the expert system
medical_system = MedicalExpertSystem()

while True:
    print("\n--- Medical Expert System ---")
    print("1. Diagnose a patient")
    print("2. View patient history")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        patient_name = input("Enter patient name: ")
        symptoms_input = input("Enter symptoms separated by commas: ").lower().split(", ")

        diagnosis, treatment = medical_system.diagnose(symptoms_input)
        resources_status = medical_system.check_resources()
        emergency_status = medical_system.emergency_alert(symptoms_input)

        # Store patient history
        medical_system.store_patient_history(patient_name, symptoms_input, diagnosis, treatment)

        # Display results
        print(f"\nPossible Diagnosis: {diagnosis}")
        print(f"Suggested Treatment: {treatment}")
        print(f"{resources_status}")
        print(f"{emergency_status}")

    elif choice == "2":
        name = input("Enter patient name to view history: ")
        medical_system.get_patient_history(name)

    elif choice == "3":
        print("Exiting the system. Stay healthy!")
        break  # Exit the loop

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

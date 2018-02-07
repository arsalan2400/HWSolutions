class Patient:
    def __init__(self,name):
        """
        :param name:Patient's name
        """
        self.name=name

    def discharge(self):
        """
        :return:print the name and type of the patient when called
        """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class EmergencyPatient(Patient):
    def __init__(self,name):

        Patient.__init__(self,name)
        self.expectedCost=1000

    def discharge(self):
        print([self.name, 'Emergency patient'])


class HospitalizedPatient(Patient):
    def __init__(self,name):
        Patient.__init__(self,name)
        self.expectedCost=2000

    def discharge(self):
        print([self.name, 'Hospitalized patient'])


class Hospital:
    def __init__(self):
        self.cost=0 # to store hospital total cost
        self.patients = [] # list of admitted patients

    def admit(self,patient):
        self.patients.append(patient)

    def discharge_all(self):
        for patient in self.patients:
            patient.discharge()
            # update hospital cost
            self.cost += patient.expectedCost

    def get_total_cost(self):
        return self.cost


# create patients
A = HospitalizedPatient("A")
B = HospitalizedPatient("B")
C = EmergencyPatient("C")
D = EmergencyPatient("D")
E = EmergencyPatient("E")

# create a hospital
myHospital = Hospital()

# admit patients
myHospital.admit(A)
myHospital.admit(B)
myHospital.admit(C)
myHospital.admit(D)
myHospital.admit(E)

# discharge all patients
myHospital.discharge_all()

# print total cost
print(myHospital.get_total_cost())
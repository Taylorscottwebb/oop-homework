class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
        
    def update_owner(self, owner):
        self.owner = owner
        print(f"The owner has been updated to {self.owner}")
    
vehicle1 = Vehicle('061698', 'subie', 'taylor')
vehicle2 = Vehicle('052198', 'taurus', 'nicholas')
print(vehicle1.registration_number)
print(vehicle1.type)
print(vehicle1.owner)
print(vehicle2.registration_number)
print(vehicle2.type)
print(vehicle2.owner)
vehicle1.update_owner('hailey')





#Task 2



class Event:
    def __init__(self, name, date, part):
        self.name = name
        self.date = date
        self.participants = part
        
    def add_participant(self):
        self.participants += 1
        print("One participant was added!")
    
    def get_participant_count(self):
        print(f"The current participant count is {self.participants}")
    
participants = Event(part = 50, name = "Susie", date = "Feb 10")
participants.add_participant()
participants.add_participant()
participants.add_participant()
participants.get_participant_count()
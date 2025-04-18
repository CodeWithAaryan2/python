import csv

class Participant:
    id_counter = 1
    def __init__(self, name, email):
        self.id = Participant.id_counter
        self.name = name
        self.email = email
        Participant.id_counter += 1
    
    def __str__(self):
        return f"Participant {self.id}: {self.name} ({self.email})"


class Organizer:
    id_counter = 1
    def __init__(self, name, contact):
        self.id = Organizer.id_counter
        self.name = name
        self.contact = contact
        Organizer.id_counter += 1
    
    def __str__(self):
        return f"Organizer {self.id}: {self.name} ({self.contact})"


class Activity:
    def __init__(self, name, time, location):
        self.name = name
        self.time = time
        self.location = location
    
    def __str__(self):
        return f"Activity: {self.name} at {self.time}, Location: {self.location}"


class Event:
    def __init__(self, name, date, venue):
        self.name = name
        self.date = date
        self.venue = venue
        self.organizers = []
        self.participants = []
        self.activities = []
    
    def add_organizer(self, organizer):
        self.organizers.append(organizer)
    
    def register_participant(self, participant):
        self.participants.append(participant)
    
    def add_activity(self, activity):
        for act in self.activities:
            if act.time == activity.time:
                print(f"Schedule Conflict: Another activity already scheduled at {activity.time}")
                return
        self.activities.append(activity)
    
    def remove_participant(self, participant_id):
        self.participants = [p for p in self.participants if p.id != participant_id]
    
    def remove_organizer(self, organizer_id):
        self.organizers = [o for o in self.organizers if o.id != organizer_id]
    
    def search_participant(self, name):
        return [p for p in self.participants if name.lower() in p.name.lower()]
    
    def export_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Email"])
            for participant in self.participants:
                writer.writerow([participant.id, participant.name, participant.email])
        print(f"Data exported to {filename}")
    
    def display_event_details(self):
        print(f"Event: {self.name}\nDate: {self.date}\nVenue: {self.venue}\n")
        print("Organizers:")
        for org in self.organizers:
            print(f"- {org}")
        print("\nParticipants:")
        for part in self.participants:
            print(f"- {part}")
        print("\nActivities:")
        for act in self.activities:
            print(f"- {act}")


# Example Usage
event = Event("TechFest 2025", "15th April 2025", "College Auditorium")

event.add_organizer(Organizer("Aaryan Pandey", "+91-9152889767"))
event.register_participant(Participant("Rahul Verma", "rahul@example.com"))
event.add_activity(Activity("Coding Competition", "10:00 AM", "Room 101"))
event.add_activity(Activity("AI Workshop", "10:00 AM", "Hall 2"))  # This will show a conflict

event.display_event_details()

event.export_to_csv("participants.csv")

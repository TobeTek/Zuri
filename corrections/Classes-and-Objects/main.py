# Python 3.10.1

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name(self, new_name):
        self.name = new_name
        print(f"Changed name to {new_name}")

    def change_age(self, new_age):
        # Validate new_age is an integer (or can become one)
        try:
            new_age = int(new_age)
        except:
            print("Failed to change age. Invalid data type")
            raise Exception 
        # isinstance ... 

        self.age = new_age
        print(f"Changed age to {new_age}")

    def add_track(self, new_track):
        self.tracks.append(new_track)
        print(f"Added new track: {new_track}")

    def get_score(self):
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.get_score())

class Student:
    # [assignment] Skeleton class. Add your code here
    
    # init method or constructor 
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    # change name method
    def change_name(self, new_name):
        self.new_name = new_name
        print("New Name: ", new_name)

    # change age method
    def change_age(self, new_age):
        self.new_age = new_age
        print("New age: ", new_age)

    # change track method
    def add_track(self, new_track):
        self.new_track = new_track
        print("New Track: ", new_track)

    # get score method 
    def get_score(self):
        self.get_score = self.score
        return self.get_score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

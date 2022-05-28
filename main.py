class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age, tracks,score):
        self.name= str(name)
        self.age= int(age)
        self.tracks=tracks.append
        self.score=float(score)
        
        print(f"Name: {name}, Age: {age}, Tracks: {tracks}, Score: {score}")
   
    def change_name(self,new_name):
            print("The New Student details is as follows:")
            print("The new Student Name is: ",str(new_name))
    def change_age(self,new_age):
            print("The new Student Age: ",int(new_age))
    def add_track(self,new_track):
            print("Student Track: ",new_track)
    def get_score(self,new_score):
            print("Student Score: ",new_score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(33.8)

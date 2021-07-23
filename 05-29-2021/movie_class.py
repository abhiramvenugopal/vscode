class Movie:
    def __init__(self):
        self.length_in_minutes=120
        self.num_characters=4
        self.language="English"
    def run(self):
        print("This is a "+self.language+" movie with "+str(self.num_characters)+" characters and is "+str(self.length_in_minutes)+" minutes long.")

m1=Movie()
m1.language=input()
m1.num_characters=int(input())
m1.length_in_minutes=int(input())
m1.run()


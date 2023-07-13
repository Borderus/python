#class animal:
#  species = None
#  name = None
#  sound = None
 
#  def __init__(self, name, species, sound, color): # Include the 'self' in the 'init'
#    self.name = name
#    self.species = species
#    self.sound = sound
#    self.color = color


#  def talk(self):
#    print(self.name+" says "+self.sound+"!")

#cow = animal("Ermintrude", "Bo Taurus", "Moo", "black")
#dog = animal("Brian", "Doggo", "Woof", "Spotty")
#
#dog.talk()
#cow.talk()

#Inheritance is the creation of sub-classes retaining the properties of their parent
#class bird(animal):
#
# def __init__(self, name):
#    self.name = name
#    self.species = "Avian"
#    self.sound = "Tweet"
#    self.color = "green"
#
#polly = bird("Polly")
#polly.talk()

# Fix My Code


#class animal:
#  species = None
#  name = None
#  sound = None
 
#  def __init__(self, name, species, sound, colour):
#    self.name = name
#    self.species = species
#    self.sound = sound
#    self.colour = colour

#class bird():

#  def __init__(self, colour):
#     self.name = "Polly"
#     self.species = "Avian"
#     self.sound = "Tweet"
#     self.colour = colour

#  def talk(self):
#    print(self.name+" want a cracker")


#cow = animal("Ermintrude", "Bo Taurus", "Moo", "Spotty")
#print(cow.sound)
#print(cow.colour)

#polly = bird("Green") 
#polly.talk()
#print(polly.colour)

# Day 64 Challenge

class job:
  def __init__(self, name, salary, hours):
    self.name = name
    self.salary = salary
    self.hours = hours

  def printjob(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")
    print()

class djob(job):
  def __init__(self, name, salary, hours, speciality, experience):
    self.name = name
    self.salary = salary
    self.hours = hours
    self.speciality = speciality
    self.experience = experience

  def printjob(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")
    print(f"Speciality: {self.speciality}")
    print(f"Experience: {self.experience} years")
    print()

class tjob(job):
  def __init__(self, name, salary, hours, subject, position):
    self.name = name
    self.salary = salary
    self.hours = hours
    self.subject = subject
    self.position = position

  def printjob(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")
    print(f"Subject: {self.subject}")
    print(f"Position: {self.position}")
    print()

lawyer = job("Lawyer", "Squillions", "60")
teacher = tjob("Teacher", "Not enough", "All of them", "Computer Science", "Classroom Teacher")
doctor = djob("Doctor", "Doing very nicely thank you", "50", "Pediatric Consultant", "7")

lawyer.printjob()
teacher.printjob()
doctor.printjob()
class Student:
  def __init__(self,name,year):
    self.name=name
    self.year=year
    self.grades=[]
  def add_grade(self,grade):
    if type(grade)==Grade:
      self.grades.append(grade)
      
  def is_passing(self,grade):
    if type(grade)==Grade and grade.score>=grade.minimum_passing:
      return "Passing score!"
    
roger=Student("Roger van der Weyden",10)
sandro=Student("Sandro Botticelli",12)
pieter=Student("Pieter Bruegel the Elder",8)

class Grade:
  minimum_passing=65
  def __init__(self,score):
    self.score=score

pieter.add_grade(Grade(100))   
pieter.is_passing(Grade(100))   
print(pieter.is_passing)
 
class Student(object):

	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.avg_grades = {}
	
	def grade(self, subject, value):
		if type(subject) is str:
			self.avg_grades(subject) = (sum(self.avg_grades(subject))+value) / len(self.avg_grades(subject)) 
			
	


class Student(object):

	grades = {}
	attendance = 0

	def __init__(self, name, surname):
	""" Initialize student name and surname """
		
		if not (isinstance(name, str) and isinstance(surname, str)):
			name, surname = "None", "None"
		self.name, self.surname = name, surname
			
	def add_grades(self, subject_name, grade_list):
	""" Append the list of grades to a specified subject per one class """
	
		if (isinstance(subject_name, str)):
			if (isinstance(grade_list, list)):
				self.grades.setdefault(subject_name, []).append(grade_list)
				self.attendance += 1 if len(grade_list) else 0 
			
	def get_averages(self):
	""" Get the average grade for each subject as a dict """	
		
		averages = {}
		for subject in self.grades.iterkeys():
			averages[subject] = avg(self.grades[subject])
		return averages
	
	

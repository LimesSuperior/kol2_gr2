
from student import Student


class Subject(object):
	
	def __init__(self, name, students_list):
		self.name = name
		self.student_attendance = {}
		for student in students_list:
			student_attendance[student] = 0

	def attendance(self, student):
		self.student_attendance[student] += 1
	

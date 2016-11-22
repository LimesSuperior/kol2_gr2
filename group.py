#!/usr/bin/python


import io, json
import student


class Group(object):

	def __init__(self):
		self.students = []
	
	def add_student(self, new_student):
		""" Add a student to the group """
	
		if isinstance(new_student, student.Student):
			self.students.append(new_student)
	
	def export_students(self, file_name):
		""" Export the group of students """
	
		if isinstance(file_name, str):
			with io.open(file_name, 'w', encoding='utf-8') as f:
				for s in self.students:
					f.write(unicode(json.dumps(s.__dict__, ensure_ascii=False)))
		
	def import_students(self):
		""" Import the group of students """
		
		pass
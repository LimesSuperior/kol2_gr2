#!/usr/bin/python


import json


class Student(object):

	def __init__(self, name, surname):
		""" Initialize student name and surname """
		
		self.grades = {}
		self.attendance = 0
		
		if not (isinstance(name, str) and isinstance(surname, str)):
			name, surname = "None", "None"
		self.name, self.surname = name, surname
			
	def add_grades(self, subject_name, grade_list, attendance=True):
		""" Add grades obtained during the class """ 
	
		if (isinstance(subject_name, str) and isinstance(grade_list, list)):
			for grade in grade_list:
				self.grades.setdefault(subject_name, []).append(grade)
			self.attendance += 1 if attendance else 0 
			
	def get_averages(self):
		""" Get the average grade for each subject as a dict """	
		
		averages = {}
		for subject in self.grades.iterkeys():
			averages[subject] = float(sum(self.grades[subject])) / len(self.grades[subject])
		return averages
	
	def get_total_average(self):
		""" Get total average """
	
		averages = self.get_averages()
		return sum(averages.itervalues()) / len(averages)
	
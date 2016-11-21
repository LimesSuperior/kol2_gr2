#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

from student import Student


def main():
	
	student1 = Student("Adam", "Nowak")
	student2 = Student(555, 888)
	
	print student1, student2
	
	student1.add_grades("UNIX", [4,5])
	student1.add_grades("UNIX", [])
	student1.add_grades("UNIX", [5])
	student1.add_grades("Java", [])
	
	print student1.grades, student1.get_averages()
	

if __name__ == "__main__": 
	main()

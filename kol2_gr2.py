#!/usr/bin/python


from student import Student
from group import Group


def main():
	
	student1 = Student("Adam", "Nowak")
	student2 = Student(555, 888)

	student1.add_grades("UNIX", [4,5])
	student1.add_grades("UNIX", [])
	student1.add_grades("UNIX", [5])
	student1.add_grades("Java", [])
	student1.add_grades("Java", [4,5,5,5])
	student1.add_grades("Java", [3])
	student1.add_grades("Java", [])
	student1.add_grades("Java", [4])
	
	print "Student's 1 partial grades:", student1.grades
	print "Student's 1 averages for each subject:", student1.get_averages()
	print "Student's 1 final average:", student1.get_total_average()
	
	group = Group()
	
	group.add_student(student1)
	group.add_student(student2)
	
	group.export_students("my_group.json")
	
if __name__ == "__main__": 
	main()

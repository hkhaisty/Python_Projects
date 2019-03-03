import random

class Student:
    #adds constructor for Student object
    def __init__(self, name, number, courses):
        self.name = name
        self.number = number
        self.courses = courses

    #creates method to display Student object assigned attributes
    def display_info(self):
        #string formatted to include styling prompts and variable values
        print(f'\nStudent name: {self.name}\nStudent Number:{self.number}\nNumber of courses:{self.courses}')

    #creates method to prompt user to change an attribute in the defined code
    def change_info(self):
        #creates list of variable names to choose
        foo = [self.name, self.number, self.courses]
        #selects random attribute
        choice = random.choice(foo)

        #in case random choice happens to be name attribute
        if choice == self.name:
            #this prompts user to change name and assigns new value
            self.name = input('\nChange student name: ')
            #prints string with new info
            print(f'\nStudent name: {self.name}\nStudent Number:{self.number}\nNumber of courses:{self.courses}')

        #in case random choice happens to be number attribute
        elif choice == self.number:
            #prompts user to change number and assigns new value
            self.number = input('\nChange student number: ')
            #prints string with new info
            print(f'\nStudent name: {self.name}\nStudent Number:{self.number}\nNumber of courses:{self.courses}')

        #in case random choice happens to be course attribute
        else:
            #prompts user to change course number and assigned new value
            self.courses = input('\nChange student courses: ')
            #prints string with new info
            print(f'\nStudent name: {self.name}\nStudent Number:{self.number}\nNumber of courses:{self.courses}')

#main method definition
if __name__ == '__main__':
    #accepts user input for student name
    student_name = input("Student name: ")
    #acepts user input for student number
    student_number = input("Student number: ")
    #accepts user input for student course values
    num_of_courses = input("# of courses: ")

    #creates student object
    stu_1 = Student(student_name, student_number, num_of_courses)
    #calls method to display student info
    stu_1.display_info()
    #calls method to change student info and display
    stu_1.change_info()



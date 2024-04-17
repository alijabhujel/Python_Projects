# Command line interface
#Project '7' : Student Manage System
# Capable of adding ,searching and removing the data

import time
students = ['aliza','monak','sahil','lila','kumari']
print('Welcome to student manage system project...')
time.sleep(0.5)

print('Press 1! to get the list of all the students')
time.sleep(0.5)
print('Press 2! to add the students to the list..')
time.sleep(0.5)
print('Press 3! to search the students from the list..')
time.sleep(0.5)
print('Press 4! to remove the students from the list..')
time.sleep(0.5)

def student_manage():
    while True:              # program will run again and again 17 no. will show again and again
        try:
            user_input = int(input('Enter the given keys values to get the result:\n'))
            if user_input==1:
                print('Here are the list of all the students..')
                for show_std in students:
                    print(show_std ,end = ' ')     # to show all in one line

            elif user_input==2:
                print('Adding the students in the list')
                std_add =input('Enter the name of student:').lower()
                if std_add in students:
                    print(f'Students named { std_add } already exists in list..')
                else:
                    students.append(std_add)                          # adding the student in list
                    print(f'Students named { std_add } added in the list')
                    for added_std in students:
                        print(added_std)

            elif user_input==3:
                print('Searching the students from the list..')
                search_std = input('Enter the name of student you want to search:').lower()
                if search_std in students:
                    print(f'Student named { search_std } found in the list..')
                else:
                    print(f'Student named { search_std } did not found in the list..')

            elif user_input==4:
                print('Removing the student from the list..')
                remove_std = input('Enter the student name you want to remove:').lower()
                if remove_std in students:
                    students.remove(remove_std)
                    for std_remove in students:
                        print(std_remove)
                else:
                    print(f'Student names { remove_std } not exist in our system..')        

        except ValueError:
            print('String are not accepted so,Please! enter only integer..')

        see_again =input('Do want to quit y/n?').lower()
        if see_again !='y':
            break
    print('Thanks! for visiting student management system....')


print('......keep watching.........')
student_manage()
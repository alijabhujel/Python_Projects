# "Project 9"   :   'Question and answer' section

print(' Welcome! to your class test ...')

start = input('Do you want to start your test?')

if start.lower() != 'yes':
   quit()

print('Let start the test!! :)')
score =0
answer =input( "What is the full form of CPU ? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

answer =input( "What is the full form of ALU ? ")
if answer.lower() == "arithmetic logic unit":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

answer =input( "What is the full form of CU? ")
if answer.lower() == "control unit":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

answer =input( "What is the full form of MU ? ")
if answer.lower() == "memory unit":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

Total_score = print('Your score is '+ str(score) + 'marks')
Total_per = print('Your percentage is' + str((score/4)/100) + '%.'  )


    


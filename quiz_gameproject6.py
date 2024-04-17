# Quiz game = project '6'

questions = {"What is the full form of CPU ?":'A',
            "Who is the father of science?":'B',
             "Who is the owner of Facebook?":'D',
             "Who is the cricket captain of Nepal?":'C',
             "Who has created Microsoft?":'B' }

answers = [["A.Central processing unit"],["B.Central processor unit"],["C.Cental program unit"],["D.Cental problem unit"],
           ['A.Pascal'],['B.Einstein'],['C.Elonk'],['D.Tesla'],
           ['A.Maska'],['B.Monak'],['C.Bill Gates'],['D.Mark Zukerberg'],
           ['A.Sandeep Lamchanee'],['B.Gyandra Malla'],['C.Aman Poudel'],['D.Paras Khadka'],
           ['A.Newton'],['B.Bill Gates'],['C.Elon Mask'],['D.Gamma']]


def start_game():
    correct_answer = 0                # intialize
    no_of_questions = 1  # This is indicated to make the questions come with only 4 option not all the options of answers
    attempted =[]         # created empty list to store user typed data
    for keys in questions:
        print(keys)
        for i in answers[no_of_questions-1]:              # nested loop
              print(i)
        attempt = input('Enter A B C or D:\n').upper()
        attempted.append(attempt)                      # stores the user data in a list
        no_of_questions+=1
    correct_answer+=check_answer(questions.get(keys),attempt)     # add the score to each question
    show_score(attempted,correct_answer)        # user data save in it..

def check_answer(answer,attempt):
    if answer == attempt:
        print('Correct Answer!')
        return 1
    else :
        print('Wrong Answer!')
        return 0

def show_score(attempted,correct_answer):
    
    print('Correct answer')                         # it shows all the correct ans of 4 ques at last
    for k in questions:
        print(questions.get(k),end = ' ')                # Questions.get(k) for each question & end ='' for making output in single line
    print('Correct answer')                         # it shows all the correct ans of 4 ques at last
    
    for ans in attempted:                           # correct answer will show at last both of user and correct ans
        print(ans)
    print('You attempted')                          # it shows all you attempt the ques at last and shows ans
   
start_game()
# Project'10'='Email Making
# alijabhujel@gmail.com         alija.in

email= input('Enter your email:')
k,j,d=0,0,0
if(len(email))>=7:
    if email[0].isalpha(): 
        if('@'in email) and email.count('@')==1:
            if email[-4]=='.' or email[-3]=='.':
                for i in email:
                    if i==i.isspace():
                     k=1               # just make condition for no space between the email
                   
                    elif i.isalpha():
                     if i== i.isupper():
                        j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                  

                if k==1 or j==1 or d==1:
                        print('Wrong Email 5 ')
                else:
                    print('Right Email')

            else:
                    print('Wrong Email 4 for .')
        else:
            print('Wrong Email 3  for @')
           
            
    else:
        print('Wrong Email 2 is not alphabetical ')

else:
    print('Wrong Email 1  for long length')
# email= input('Enter your email:')
# k,j,d=0,0,0
# if len(email)>=7:
#     if email[0].isalpha(): 
#         if("@" in email) and email.count("@")==1:
#             if email[-4]=="." or email[-3]==".":
#                 for i in email:
#                     if i==i.isspace():
#                      k=1               # just make condition for no space between the email
                   
#                     elif i.isalpha():
#                      if i==i.isupper():
#                         j=1
#                     elif i.isdigit():
#                         continue
#                     elif i=="_" or i=="." or i=="@":
#                         continue
#                     else:
#                         d=1
                  

#                 if k==1 or j==1 or d==1:
#                         print('Wrong Email 5 ')
#                 else:
#                     print('Right Email')

#             else:
#                     print('Wrong Email 4 for .')
#         else:
#             print('Wrong Email 3  for @')
           
            
#     else:
#         print('Wrong Email 2 is not alphabetical ')

# else:
#     print('Wrong Email 1  for long length')
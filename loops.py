num_of_tries = 0
while num_of_tries != 3:
   username = input('please enter your usenmane: ')
   password = input('please enter your password: ')
   if username == 'm7md' and password == '123':
    print('Welcome !')
    num_of_tries = 0
    exit()
   else:
    print('error')
    num_of_tries +=1 
    print('you have ' + str(3 - num_of_tries) +' left')

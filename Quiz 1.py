print('hello, Welcome to trivia!')

ans = input('Are u ready to play (yes/no): ')
score = 0
total_q = 4

if ans == 'Yes':
    ans = input('1. What is the best supercell game? ')
    if ans == 'Brawl stars':
        score += 1
        print('Good')
    else:
            print('Better luck next time😢😁')


            
    ans = input('2. What is 2 + 8 + 9 -1? ')
    if ans == '18':
        score += 1
        print('Good')
    else:
            print('Better luck next time😢😁')


            
    ans = input('3. is -78>9 ')
    if ans == 'No':
        score += 1
        print('Good')
    else:
            print('Better luck next time😢😁')


            
    ans = input('1. What is 78+2? ')
    if ans == '80':
        score += 1
        print('Good')
    else:
            print('Better luck next time😢😁')


print('Thank you for playing, you got', score, "questions correct.")
mark = (score/total_q) * 100

print("Mark:", str(mark) + '%')
print('Good bye, please come back again')





            
        

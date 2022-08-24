print('Welcome to my computer quiz!')

playing = input('Do you want to play?: ')

score = 0
if playing.lower() != "yes":
    quit()
print("Okay Let's Play! :)")

answer = input("1.What are two things you can never eat for breakfast?: ").lower()

if answer == "lunch and dinner":
    print('Correct😄')
    score += 1
else :
    print('Wrong🤣')


answer = input("2.How can a girl go 25 days without sleep?: ").lower()

if answer == "she sleeps at night":
    print('Correct😄')
    score += 1
else :
    print('Wrong🤣')

answer = input("3.What's greater than God and more evil than the devil. Rich people want it, poor people have it. And if tyou eat it, you'll die?: ").lower()

if answer == "nothing":
    print('Correct😄')
    score += 1
else :
    print('Wrong🤣')

answer = input("4.If you had only one match and entered a dark room containing an oil lamp, some kindling wood, and a newspaper, which would you light first?").lower()

if answer == "the match":
    print('Correct😄')
    score += 1
else :
    print('Wrong🤣')

answer = input("5.What two keys can't open any door?").lower()

if answer == "a monkey and a donkey":
    print('Correct😄')
    score += 1
else :
    print('Wrong🤣')

answer = input("6.What will you actually find at the end of every rainbow?").lower()

if answer == "the letter w":
    print('Correct😄')
    score += 1
else :
    print('Wrong🤣')

print('You got ' + str(score) + ' questions correct')
print('You got ' + str(( score / 6 )* 100) + '%')

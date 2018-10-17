import random

def hello(name):
    print('Howdy!'+ name)
    print('Paul')

hello('Alice')

def getAnswer(answerNumber):
    if answerNumber ==1:
        return 'it is certain'
    elif answerNumber == 2:
        return 'it is decidedly so'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask Later'
    elif answerNumber == 6:
        return 'concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Not good'
    elif answerNumber == 9:
        return 'Very Doubtful'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)


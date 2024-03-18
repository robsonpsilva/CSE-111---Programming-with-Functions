"""
The Rosenberg self-esteem scale is a self-esteem measure developed by the sociologist Morris Rosenberg in 1965. It is still used in social-science research today. To complete the measure, a person completes a survey that contains the following ten statements.

I feel that I am a person of worth, at least on an equal plane with others.
I feel that I have a number of good qualities.
All in all, I am inclined to feel that I am a failure.
I am able to do things as well as most other people.
I feel I do not have much to be proud of.
I take a positive attitude toward myself.
On the whole, I am satisfied with myself.
I wish I could have more respect for myself.
I certainly feel useless at times.
At times I think I am no good at all.

This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
"""

def main():
    print('This program is an implementation of the Rosenberg\
    Self-Esteem Scale. This program will show you ten\
    statements that you could possibly apply to yourself.\
    Please rate how much you agree with each of the\
    statements by responding with one of these four letters:')

    print('D means you strongly disagree with the statement.\n\
          d means you disagree with the statement.\n\
          a means you agree with the statement.\n\
          A means you strongly agree with the statement.')

    questions = ['I feel that I am a person of worth, at least on an equal plane with others.',
                 'I feel that I have a number of good qualities.',
                 'All in all, I am inclined to feel that I am a failure.',
                 'I am able to do things as well as most other people.',
                 'I feel I do not have much to be proud of.',
                 'I take a positive attitude toward myself.',
                 'On the whole, I am satisfied with myself.',
                 'I wish I could have more respect for myself.',
                 'I certainly feel useless at times.',
                 'At times I think I am no good at all.']
    print(15 * '_')
    answers = []
    answer = ''
    option = True
    flag = ''
    while option:
        for question in questions:
            answer = get_imput(question)
            if answer == 'Error':
                print('Data entry error! Please check the data you typed')
                break
            else:
                answers.append(answer)
        if answer != 'Error':
            print(f'Your score is {calculate_steem_messure(answers)}')
            print('A score below 15 may indicate problematic low self-esteem.')
        flag = input('Do you want to quit? Type Y for Yes or everything else for No.')
        if flag.lower() == 'y':
            print('Program end')
            option = False



def get_imput(question):
    while True:
        answer = input(question)
        if answer.strip() in ['D','d', 'a', 'A']:
            return answer
        else:
            return 'Error'

def calculate_steem_messure(answers):
    result = 0
    for i in range(len(answers)):
        if i+1 in [1,2,4,6,7]:
            #Positive questions
            if answers[i] == 'D':
                result += 0
            elif answers[i] == 'd':
                result += 1
            elif answers[i] == 'a':
                result += 2
            elif answers[i] == 'A':
                result += 3
        else:
            #Negative questions
            if answers[i] == 'D':
                result += 3
            elif answers[i] == 'd':
                result += 2
            elif answers[i] == 'a':
                result += 1
            elif answers[i] == 'A':
                result += 0
    return result

# If this file was executed like this:
# > python example.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
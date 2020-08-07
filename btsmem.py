
from btsmemdict import *
import time


SENTINEL = 0
END = 1

def main():

    # Controls the main flow of the quiz

    introduction()
    score_dict = {} # Make a dictionary to record the scores
    end = 0
    for i in range(len(question_list)):
        answer = input(question_list[i] + 'Answer: ')

        # Check if user wants to end the game
        if answer == str(SENTINEL):
            end = END
            break

        # Check if user entered one of the options provided
        while answer not in questionAnswer[i]:
            print("Sorry, " + answer + " is not an option. Try again.")
            answer = input(question_list[i] + 'Answer: ')

        # Get list of member(s) that corresponded with the answer choice
        ans_list = questionAnswer[i][answer]
        for member in ans_list:
            if member not in score_dict:
                score_dict[member] = 1
            else:
                score_dict[member] += 1

    if end != END:
        print(score_dict)
        max_score = max(score_dict.values())
        members_list = []

        # Check all the member(s) that have the highest score at the end of the quiz
        for key in score_dict:
            if score_dict[key] == max_score:
                members_list.append(key)
        if len(members_list) > 1:
            print("The BTS members you are most similar to are: " + ", ".join(members_list))
        else:
            print("The BTS member you are most similar to is: " + members_list[0] + "!")

    credits()


def introduction():
    # Prints introductory messages with time delay
    name = input("What is your name? ")
    print("Welcome to the 'Which BTS Member Are You?' Quiz, " + name + "!")
    time.sleep(2)
    print("You will be given a series of questions to answer. Enter the number of the answer you choose!") # In future, allow question # choice?
    time.sleep(3)
    print("At any time, you can enter " + str(SENTINEL) + " to exit! If you exit, you will not receive a quiz result.")
    time.sleep(2)


def credits():
    print("Credits/Resources consulted while making this quiz: ")
    print("Noisey Questionnaire of Life, BTS concerts, BTS Take BuzzFeed's 'Which Member of BTS Are You?' Quiz, my ARMY brain.")



if __name__ == '__main__':
    main()
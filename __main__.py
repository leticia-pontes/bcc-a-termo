from termo import Termo, Feedback, Result, InvalidAttempt
from termcolor import colored


def to_output(result: Result):
    for c, feedback in result.feedback:
        if feedback == Feedback.RIGHT_PLACE:
            print(colored(c, "green"), end=' ')
        elif feedback == Feedback.WRONG_PLACE:
            print(colored(c, "yellow"), end=' ')
        else:
            print('_', end=' ')
    print()


def main():
    word = 'teste'
    limit = 5
    counter = 0
    termo = Termo(word)
    result = Result(win=False, feedback=None)
    print('Tente adivinhar a palavra')
    while not result.win and counter < limit:
        try:
            guess = input(f'Tentativa: ')
            result = termo.test(guess)
            counter += 1
            to_output(result)
        except InvalidAttempt:
            print('Tente de novo')
    if result.win:
        print('Parabéns')
    else:
        print('Game over')


if __name__ == '__main__':
    main()

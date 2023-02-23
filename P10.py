#33.10 LAB: Print string in reverse
#Ch6 Loops

while True:
    # take input from user
    text = input()

    # check if the user wants to quit
    if text.lower() in ['done', 'd']:
        break

    # reverse the input text
    reversed_text = text[::-1]

    # print the reversed text
    print(reversed_text)
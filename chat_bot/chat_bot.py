""" chatbot.

    steps:
    1. input/listen
    2. process/decide
    3. output/talkback
"""

greet_words = ['hi','hello','yo','hey']
bye_words = ['bye','tata','hasta la vista']


def listen():
    return input("Say something: ")

def decide(command):
    #print(command)
    tokens = command.lower().split(" ")

    for token in tokens:
        if token in greet_words:
            talkback(" he said greetings")
            break
            
        elif token in bye_words:
            talkback("he said bye")
            break

def talkback(response):
    print(response)

while 1:
    command = listen()
    decide(command)
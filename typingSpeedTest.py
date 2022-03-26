import time
string = "This is a typing speed test to figure out how fast one can actually type, some think they are fast, but are you actually? Probably not!"
word_count = len(string.split())
box_border = '-+-'*10

def createbox():
    print(box_border)
    print()
    print('Type the given phrase as fast as humanyly possible and with accuracy:')
    print()

while  1:
    t0 = time.time()
    createbox()
    print(string,'\n')
    inputText = str(input())
    t1 = time.time()
    lengthOfInput = len(inputText.split())
    accuracy = len(set(inputText.split()) & set(string.split()))
    accuracy = (accuracy/word_count)
    timeTaken = (t1 - t0)
    wordsperminute = (lengthOfInput/timeTaken)*60 
    print('Total words typed \t :' ,lengthOfInput)
    print('Time it took to type \t :',round(timeTaken,2),'seconds')
    print('Your accuracy is \t :',round(accuracy,3)*100,'%')
    print('Typing speed is \t :' , round(wordsperminute,2),'words per minute')
    print("Woah, you are so good",end='')
    if input():
        continue
    else:
        print('Thanks for trying to type as fast as me')
        time.sleep(1.5)
        break

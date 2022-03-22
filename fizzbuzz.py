# print numbers from 1 to 100
# when a num is multiple of 3, print fizz instead
# when a num is a multiple of 5, print buzz instead
# when a num is multiple of both, print fizzbuzz

if __name__ == '__main__':
    print("fizzbuzz time!")
    for num in range(1, 101):
        if(num % 3 == 0):
            if(num % 5 == 0):
                print ("fizzbuzz")
            else:
                print ("fizz")
        elif(num % 5 == 0):
            print ("buzz")
        else:
            print( num)
            

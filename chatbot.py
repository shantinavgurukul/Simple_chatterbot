import random

print("***************WELCOME TO CHATBOT GAME****************")

def chatterbot(sentense):
    ques=input("Say Something Here=")
    a=ques.lower()
    # print(a)

    for word in sentense:
        # print(word)
        # break
        if word  == a:
            print(random.choice(response[word]))
    again=input("Do you want play again=")
    if again=='yes':
        chatterbot(sentense)
    else:
        print("no thanks*** nice too meet you")
        
response={"hello":["hi","hey","hello"],"how are you":['i m fine','good',"mast"],"hi":["hii","hey","hello"],"hey":["hi","hey","hello"]}
chatterbot(response)


# a = {"hello":["hi","hey","hello"]}
# for x in a:
    # print(a[x])

















































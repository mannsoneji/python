"""
nested dictionarry:

m = {

    subdictionary1 : {
        key : value;
    },
    subdictionary2 : {
        key : value;
    },
    subdictionary3 : {
        key : value;
    },
    subdictionary4 : {
        key : value;
    },
    .
    .
    .

    }

"""

quiz = {
    1: {
        "que" : "who is prime minister of INDIA ? ",
        "ans" : "narendra modi"
    },
    2: {
        "que" : "who is famouse criceter in INDIA ? ",
        "ans" : "virat kohli"
    }
}

# print(quiz[1]["que"])
# user_ans = input("Enter your ans")
score = 0
for i in range(1,len(quiz)+1):
    print()
    print(f"Q. {i} {quiz[i]["que"]}" )
    user_ans = input("Enter your ans : ")
    if user_ans.lower() == quiz[i]["ans"].lower():
        print("Right ans")
        score += 20
    else:
        print("Wrong ans")
        score-=10
        if score == 0 or score <= 0:
            score = 0

print("Total score = ",score)
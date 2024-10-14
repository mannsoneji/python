import random

team_list = ["CSK","MI","RCB","KKR","RR"]

menu = """
                        Welcome to IPL 2025

"""

print(menu)

for team in team_list:
    print(team,end=" , ")

myteam = input("\nENter Your Team name : ")
print("My team : ",myteam)

opp_team = random.choice(team_list)
if opp_team==myteam:
    opp_team = random.choice(team_list)

print("Opp.  team : ",opp_team)


toss_list = ["H","T"]
print("\nToss Time")
print("Press H for Head")
print("Press T for Tail")

mytoss_choice = input("Enter your choice : ").upper()
actual_toss = random.choice(toss_list)
batball_menu = """
        press 1 for batting
        press 2 for field 
"""
batball_list = ['bat','field']

score_list = [0,1,2,3,4,6,"wicket","no ball","wide"]
myteam_ball = 0
myteam_score = 0
myteam_wicket = 0

if mytoss_choice == actual_toss:
    print(f"{myteam} won the toss")
    print(batball_menu)
    mychoice = int(input("Enter your choice : "))
    if mychoice == 1:
        print(f"{myteam} choose bat first")


        while myteam_ball<6:
            input()
            score = random.choice(score_list)

            if score in [1,2,3,4,6]:
                myteam_score+= score 
                myteam_ball +=1
            elif score == "wicket":
                myteam_wicket += 1
                myteam_ball += 1
            elif score == "no ball" or score == "wide":
                myteam_score += 1

            print(f"Ball {myteam_ball} : {score} : {myteam} : {myteam_score}/{myteam_wicket} 0.{myteam_ball}")
    else:
        print(f"{myteam} choose field first")


else :
    print(f"{opp_team} won the toss and slected {random.choice(batball_list)}")




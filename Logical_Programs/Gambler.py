'''	
    @Author: Srividya
    @Date:  2021-11-18 
    @Title: Gambler
    '''

import random 


try:
    def gambler(wins,bets,loss):
        """
            Description: Finding the wins and bets of
            gambler
            Parameter: wins,bet
            Return: 
            
            """
        for t in range(trails):
            money = stake
        while money > 0 and money < goal:
            bets += 1
            if random.randrange(goal) == 0:
                money == 1
            else:
                money -=1

        if money == goal:
            wins+=1
        else:
            loss +=1 

        print("Count of wins: ",wins)
        print("number of bets: ",bets)
        print("number of loss: ",loss)
        
        winspercent = (wins / trails) * 100
        print("percentage of wins",winspercent)
except Exception as e:
    print(e)

if __name__=='__main__':
    stake = int(input("enter the money:"))
    goal = int(input("enter the goal: "))
    trails = int(input("enter trails: "))
    wins = 0
    bets = 0
    loss = 0
    gambler(wins,bets,loss)
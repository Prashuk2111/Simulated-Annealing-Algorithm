from math import cos, exp, pi
import random

#  Funciton to generate random value of X1 and X2 using step size to determine the neighbourhood
def Random_X_genreator(X,step):
    range = [X - step, X + step]

    # If statement to check for the new value to be within the range [-100,100]
    if range[0] < -100:
        range[0] = -100
    if range[1] > 100:
        range[1] = 100
    return(round(random.uniform(range[0], range[1]),3))

# Sa_annealing function
def Sa_annealing(X1,X2,Tempreture,alpha,step):
    # Intial conditions specfied, X1, X2, temperature, alpha, step
    Start_Tempreture = Tempreture
    Alpha =alpha
    Intial_X1 = X1
    Intial_X2 = X2
    Step_Size = step

    # Cost formula 
    Intial_Solution = -cos(Intial_X1)*cos(Intial_X2)*exp(-(Intial_X1-pi)**2 - (Intial_X2-pi)**2)
    Start_Cost = Intial_Solution

    # Number of iterations are fixed to 1000
    ITERATIONS = 1000
    
    # If the temperature reached below 0.001 the algorithm is completed
    while(Start_Tempreture > 0.001):
        for i in range(ITERATIONS):
            # Generating new X1 and X2
            New_X1 = Random_X_genreator(Intial_X1,Step_Size)
            New_X2 = Random_X_genreator(Intial_X2,Step_Size)
            
            # Calculating cost of new solution
            Cost = -cos(New_X1)*cos(New_X2)*exp(-(New_X1-pi)**2 - (New_X2-pi)**2)
            # Calculating the delta cost to see if new solution is cheap or expensive
            Delta_Cost = Cost - Start_Cost

            # If new cost is less then the old cost then the new solution is accepted 
            if (Delta_Cost <= 0):
                Intial_X1 = New_X1
                Intial_X2 = New_X2
                Start_Cost = Cost
            else:
                
                # If new cost is more than the old cost then new solution is accepted on basis of probability
                Probablity = random.random()
                if(Probablity < (exp(-Delta_Cost/Start_Tempreture))):
                    Intial_X1 = New_X1
                    Intial_X2 = New_X2
                    Start_Cost = Cost
        
        # For geometric
        Start_Tempreture = Start_Tempreture*Alpha
        # For linear
        Start_Tempreture = Start_Tempreture*Alpha


    print(Intial_X1)
    print(Intial_X2)
    print(Start_Cost)

if __name__ == "__main__":
#  For geometric
    Sa_annealing(-100,100,500,0.8,5)
# For linear
    # Sa_annealing(-50,50,500,0.008,5)






        



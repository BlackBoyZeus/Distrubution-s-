import random

def normal(mu, sigma):
    """
    Returns a Normal random variable with mean mu and standard deviation sigma.
    
    Parameters:
    mu (float): Mean of the normal distribution.
    sigma (float): Standard deviation of the normal distribution.
    
    Returns:
    float: Normal random variable.
    """
    return random.normalvariate(mu, sigma)

def simulate_show_jumping_competition(num_riders):
    """
    Simulates a show jumping competition by generating performance scores for riders.
    
    Parameters:
    num_riders (int): Number of riders in the competition.
    """
    scores = [normal(80, 5) for _ in range(num_riders)]
    
    print("Show Jumping Competition Results:")
    print(f"Number of Riders: {num_riders}")
    print("Scores:")
    for i in range(num_riders):
        print(f"Rider {i+1}: {scores[i]:.2f}")

# Example usage
num_riders = 10
simulate_show_jumping_competition(num_riders)

#In this example, we simulate a show jumping competition where riders are assigned performance scores based on a normal distribution. The normal function generates a random value following a normal distribution with the specified mean (mu) and standard deviation (sigma).

#The simulate_show_jumping_competition function takes the number of riders in the competition as a parameter. It generates a performance score for each rider by calling the normal function. The mean and standard deviation values for the normal distribution are set to predetermined values.

#Finally, the number of riders and their corresponding scores are printed as the simulation results.

#To use this example, you can adjust the number of riders and modify the mean and standard deviation values in the simulate_show_jumping_competition function according to your specific equestrian sporting context. The code will simulate the show jumping competition and provide the results as the scores for each rider.

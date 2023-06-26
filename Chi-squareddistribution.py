import random

def chi2(k):
    """
    Returns a Chi-squared random variable with k degrees of freedom.
    
    Parameters:
    k (int): Degrees of freedom.
    
    Returns:
    float: Chi-squared random variable.
    """
    return random.chisquare(k)

def assign_scores(num_rounds):
    """
    Assigns scores to a boxing match based on a chi-squared distribution.
    
    Parameters:
    num_rounds (int): Number of rounds in the boxing match.
    """
    scores = [chi2(2) for _ in range(num_rounds)]
    
    print("Boxing Match Score Assignment:")
    print(f"Number of Rounds: {num_rounds}")
    print("Scores:")
    for i in range(num_rounds):
        print(f"Round {i+1}: {scores[i]:.2f}")

# Example usage
num_rounds = 12
assign_scores(num_rounds)

#In this example, the chi2 function generates a random value following a chi-squared distribution with the specified degrees of freedom (k).

#The assign_scores function takes the number of rounds in the boxing match as a parameter. It generates a score for each round by calling the chi2 function. The degrees of freedom for the chi-squared distribution are set to 2, but you can adjust it based on your requirements.

#Finally, the number of rounds and the assigned scores for each round are printed as the result of the score assignment.

#To use this example, you can modify the number of rounds in the assign_scores function call according to your specific boxing match. The code will simulate the score assignment for each round using the chi-squared distribution and provide the results.

import random

def gamma(alpha, beta):
    """
    Returns a Gamma random variable with shape alpha and scale beta.
    
    Parameters:
    alpha (float): Shape parameter.
    beta (float): Scale parameter.
    
    Returns:
    float: Gamma random variable.
    """
    return random.gammavariate(alpha, beta)

def simulate_boxing_match():
    """
    Simulates the duration of a boxing match based on a Gamma distribution.
    """
    alpha = 2
    beta = 1
    
    duration = gamma(alpha, beta)
    
    print("Boxing Match Simulation Results:")
    print(f"Alpha (Shape Parameter): {alpha}")
    print(f"Beta (Scale Parameter): {beta}")
    print(f"Duration: {duration:.2f} rounds")

# Example usage
simulate_boxing_match()
#In this example, we simulate the duration of a boxing match based on a Gamma distribution. The gamma function generates a random value following a Gamma distribution with the specified shape and scale parameters.

#The simulate_boxing_match function sets the shape parameter (alpha) and scale parameter (beta) to predetermined values. It calls the gamma function to generate a random duration for the boxing match.

#Finally, the duration of the boxing match is printed as simulation results.

#To use this example, you can adjust the shape and scale parameters in the simulate_boxing_match function according to your desired distribution characteristics. The code will simulate the duration of the boxing match and provide the result as the number of rounds.

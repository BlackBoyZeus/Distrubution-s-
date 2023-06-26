import random

def bernoulli(p):
  """Returns a Bernoulli random variable with probability p."""
  return random.random() < p

def simulate_bernoulli_trials(p, n):
  """Simulates n Bernoulli trials with probability p and calculates the relative frequency of success."""
  successes = 0
  for _ in range(n):
    if bernoulli(p):
      successes += 1
  relative_frequency = successes / n
  return relative_frequency

probability = 0.5
num_trials = 1000

relative_frequency = simulate_bernoulli_trials(probability, num_trials)
print("Relative frequency of success:", relative_frequency)

#In this example, the simulate_bernoulli_trials function takes two parameters: p, representing the probability of success in a single trial, and n, representing the number of trials to simulate. It uses the bernoulli function to perform each trial and count the number of successes.

#After simulating the trials, the relative frequency of success is calculated by dividing the number of successes by the total number of trials (n). The result is then printed to the console.

#Note that num_trials is set to 1000 in this example, but you can adjust it to any desired value to increase or decrease the number of trials. Similarly, you can modify the probability variable to represent the desired probability of success in each trial.

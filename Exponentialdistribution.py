import random

def exponential(lambda_):
    """
    Returns an Exponential random variable with average lambda.
    
    Parameters:
    lambda_ (float): Average value or rate parameter.
    
    Returns:
    float: Exponential random variable.
    """
    return random.expovariate(lambda_)

def simulate_queue(arrival_rate, service_rate, num_customers):
    """
    Simulates a queuing system based on an exponential distribution.
    
    Parameters:
    arrival_rate (float): Arrival rate of customers.
    service_rate (float): Service rate of the system.
    num_customers (int): Number of customers to simulate.
    """
    interarrival_times = [exponential(arrival_rate) for _ in range(num_customers)]
    service_times = [exponential(service_rate) for _ in range(num_customers)]
    
    arrival_times = [sum(interarrival_times[:i]) for i in range(1, num_customers+1)]
    departure_times = [arrival_times[i] + service_times[i] for i in range(num_customers)]
    
    waiting_times = [max(0, departure_times[i-1] - arrival_times[i]) for i in range(1, num_customers)]
    
    average_waiting_time = sum(waiting_times) / num_customers
    max_waiting_time = max(waiting_times)
    
    print("Simulation Results:")
    print(f"Arrival Rate: {arrival_rate} customers per unit time")
    print(f"Service Rate: {service_rate} customers per unit time")
    print(f"Number of Customers: {num_customers}")
    print(f"Average Waiting Time: {average_waiting_time:.2f} units of time")
    print(f"Maximum Waiting Time: {max_waiting_time:.2f} units of time")

# Example usage
arrival_rate = 0.8
service_rate = 1.2
num_customers = 100
simulate_queue(arrival_rate, service_rate, num_customers)

#In this example, we simulate a queuing system based on an exponential distribution. The exponential function generates a random value following an exponential distribution with the specified average value or rate parameter.

#The simulate_queue function takes three parameters: arrival_rate, service_rate, and num_customers. It uses the exponential function to generate random interarrival times and service times for the customers in the system. The arrival and departure times are calculated based on the interarrival times and service times. The waiting times are calculated as the difference between the departure time of the previous customer and the arrival time of the current customer.

#Finally, the average waiting time and maximum waiting time are calculated and printed as simulation results.

#To use this example, you can specify the arrival rate, service rate, and number of customers in the simulate_queue function call. The code will simulate the queuing system and provide the average waiting time and maximum waiting time as results.

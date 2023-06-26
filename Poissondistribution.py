import random

def roll_dice(num_dice):
    """
    Simulates rolling a given number of dice.
    
    Parameters:
    num_dice (int): Number of dice to roll.
    
    Returns:
    list: List of dice roll outcomes.
    """
    dice_rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)  # Generates a random number between 1 and 6 (inclusive)
        dice_rolls.append(roll)
    return dice_rolls

def calculate_total(rolls):
    """
    Calculates the total sum of dice roll outcomes.
    
    Parameters:
    rolls (list): List of dice roll outcomes.
    
    Returns:
    int: Total sum of dice rolls.
    """
    return sum(rolls)

def play_dice_game(num_dice):
    """
    Simulates a dice game by rolling the specified number of dice and calculating the total.
    
    Parameters:
    num_dice (int): Number of dice to roll.
    """
    rolls = roll_dice(num_dice)
    total = calculate_total(rolls)
    
    print(f"Rolls: {rolls}")
    print(f"Total: {total}")

# Example usage
num_dice = 3
play_dice_game(num_dice)

#roll_dice: Simulates rolling a given number of dice. It generates random numbers between 1 and 6 (inclusive) to simulate the dice rolls. The function returns a list of the dice roll outcomes.
#calculate_total: Calculates the total sum of the dice roll outcomes by taking the sum of the elements in the input list.
#play_dice_game: Simulates a dice game by rolling the specified number of dice, calculating the total, and printing the results. It calls the roll_dice function to get the dice roll outcomes, and then passes them to the calculate_total function to determine the total sum. Finally, it prints the individual rolls and the total.
#To use this example, you can specify the number of dice to roll (num_dice) in the play_dice_game function call. The code will simulate rolling that number of dice and provide the rolls as well as the total sum of the outcomes.

def main():
    fruit = input("Enter a fruit: ")  # Prompt the user to enter a fruit
    stock = num_in_stock(fruit)  # Get the stock count of the fruit entered by the user
    
    if stock == 0:
        print("This fruit is not in stock.")  # If stock is 0, print the message
    else:
        print("This fruit is in stock! Here is how many:")  # If stock is greater than 0, print the stock count
        print(stock)

# The provided function to check how many of the fruit is in stock
def num_in_stock(fruit):
    """
    This function returns the number of fruit Sophia has in stock.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # This fruit is not in stock.
        return 0

# Ensures that main() is called when the script runs
if __name__ == '__main__':
    main()

def average(a: float, b: float) -> float:
    # Calculate the average of two numbers
    return (a + b) / 2

def main():
    # Testing the average function with different values
    avg_1 = average(0, 10)     # Should return 5.0
    avg_2 = average(8, 10)     # Should return 9.0

    final = average(avg_1, avg_2)  # Average of 5.0 and 9.0 => 7.0

    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)

# Call the main function
if __name__ == '__main__':
    main()

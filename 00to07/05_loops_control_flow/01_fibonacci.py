MAX_TERM_VALUE: int = 10000

def main():
    curr_term = 0  # Fib(0)
    next_term = 1  # Fib(1)

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")
        # Generate the next term
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

# Required line to run the program
if __name__ == '__main__':
    main()








# Let me know if you’d like to add:

# User input for max value?

# Total count of terms?

# Or show the formula for each step like: Fib(4) = 3 = 1 + 2?

# Happy coding, Javeria! 💻🌸








# You said:
# matlab h kiya or kiya ho raha h isme


# ChatGPT said:
# Sure, let me break it down for you and explain what’s happening in the Fibonacci Sequence program! 🌟

# Fibonacci Sequence Overview:
# The Fibonacci sequence is a series of numbers where:

# Fib(0) = 0

# Fib(1) = 1

# For each subsequent term, the sum of the previous two terms gives the next term in the sequence:

# 𝐹
# 𝑖
# 𝑏
# (
# 𝑛
# )
# =
# 𝐹
# 𝑖
# 𝑏
# (
# 𝑛
# −
# 1
# )
# +
# 𝐹
# 𝑖
# 𝑏
# (
# 𝑛
# −
# 2
# )
# Fib(n)=Fib(n−1)+Fib(n−2)
# Let's understand the code step by step:
# python
# Copy
# Edit
# MAX_TERM_VALUE: int = 10000
# This is a constant (we define it with a fixed value of 10000). It’s the limit, meaning we only want to print Fibonacci numbers less than or equal to 10,000.

# python
# Copy
# Edit
# def main():
#     curr_term = 0  # Fib(0)
#     next_term = 1  # Fib(1)
# Here we initialize the first two terms of the Fibonacci sequence:

# curr_term = 0 → This is Fib(0).

# next_term = 1 → This is Fib(1).

# python
# Copy
# Edit
#     while curr_term <= MAX_TERM_VALUE:
# This is the loop that continues as long as the current Fibonacci term (curr_term) is less than or equal to MAX_TERM_VALUE (10,000). So, the program will keep printing Fibonacci terms until the term exceeds 10,000.

# python
# Copy
# Edit
#         print(curr_term, end=" ")
# This prints the current Fibonacci term (curr_term).

# The end=" " part ensures that the numbers are printed on the same line, separated by spaces instead of printing them on new lines.

# python
# Copy
# Edit
#         term_after_next = curr_term + next_term
# This line calculates the next term in the Fibonacci sequence by adding curr_term (current term) and next_term (the next term).

# For example, if curr_term = 0 and next_term = 1, then term_after_next = 0 + 1 = 1.

# python
# Copy
# Edit
#         curr_term = next_term
#         next_term = term_after_next
# Updating the terms:

# curr_term becomes next_term (moving one step forward).

# next_term becomes term_after_next (which we just calculated).

# This prepares for the next Fibonacci number in the next iteration.

# python
# Copy
# Edit
# if __name__ == '__main__':
#     main()
# This runs the main() function when the program is executed.

# Example Walkthrough:
# Let’s see how it works with actual numbers:

# First Iteration:
# curr_term = 0 (Fib(0))

# next_term = 1 (Fib(1))

# term_after_next = 0 + 1 = 1 → This is Fib(2)

# So the new terms are:

# curr_term = 1 (Fib(1))

# next_term = 1 (Fib(2))

# Output: 0

# Second Iteration:
# curr_term = 1 (Fib(1))

# next_term = 1 (Fib(2))

# term_after_next = 1 + 1 = 2 → This is Fib(3)

# New terms:

# curr_term = 1 (Fib(2))

# next_term = 2 (Fib(3))

# Output: 0 1

# Third Iteration:
# curr_term = 1 (Fib(2))

# next_term = 2 (Fib(3))

# term_after_next = 1 + 2 = 3 → This is Fib(4)

# New terms:

# curr_term = 2 (Fib(3))

# next_term = 3 (Fib(4))

# Output: 0 1 1

# And so on... until the value exceeds 10,000.
# Final Output:
# The program will print all Fibonacci numbers up to 10,000 in a single line, separated by spaces:

# yaml
# Copy
# Edit
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
# Conclusion:
# The program continuously calculates and prints Fibonacci terms.

# It keeps track of the last two terms (current and next).

# The loop continues until the terms exceed the specified limit (MAX_TERM_VALUE = 10,000).

# This should make things much clearer now! 😊 Let me know if you have any more questions or if you want to modify the program further.











# Search

# Reason




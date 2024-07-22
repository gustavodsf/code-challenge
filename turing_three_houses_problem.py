def count_pythagorean_triplets(n):
    count = 0
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= n:
                count += 1
    return count

# Input
n = int(input("Enter the number of houses: "))

# Calculate and print the number of Pythagorean triplets
result = count_pythagorean_triplets(n)
print(f"The number of sets of three houses that form a special group is: {result}")
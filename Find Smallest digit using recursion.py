def smallest_digit(n):
    if n==0:
        return 0
    return min(n%10, smallest_digit(n//10))
n=int(input("Enter a digit: "))
print(smallest_digit(n))
 
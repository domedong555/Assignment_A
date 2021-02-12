#Write a program that finds all prime numbers up to n for input n. Example Output:
def prime_Number(number):
    prime_list = []
    if number>1:
        for value in range(2, number + 1):
            if value > 1:
                for i in range(2, value):
                    if (value % i) == 0:
                        break
                else:
                    prime_list.append(value)
    else:
        print("This number is not prime number")
    print(number," => ",end="")
    print(str(prime_list))


n = int(input("Enter number to process : "))
prime_Number(n)
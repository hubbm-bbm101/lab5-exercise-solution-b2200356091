def odd_fonk(number):
    return sum([t for t in range(1,number+1) if t %2 != 0])
def even_fonk(number):
    even = [t for t in range(1,number+1) if t %2 == 0]
    return sum(even) / len(even)
def main():
    n = int(input("enter your number: "))
    print("sum of odd numbers: {}".format(odd_fonk(n)))
    print("Average of even numbers: {}".format(even_fonk(n)))

main()

def sumF(n):
    if n == 1:
        return 1
    else:
        return n + sumF(n - 1)
        
        
def main():

    result = sumF(5)
    print(result)
main()

        
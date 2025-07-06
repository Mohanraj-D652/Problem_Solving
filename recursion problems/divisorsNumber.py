def div(n):
    if n == 0:
        return 0
    if 12 % n == 0:
        print(n)
    
    return div(n-1)

def main():
    div(12)
main()

    
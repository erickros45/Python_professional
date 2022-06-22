def primo(num: int):
    result1 = [x for x in range(2,num+1) if num % x == 0]
    result2 = len(result1) == 1
    if result2 == True:
        print("Es primo")
    else:
        print("No es primo")


def run():
    print(primo(7))

if __name__=="__main__":
    run()
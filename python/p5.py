from itertools import product, chain

if __name__ == "__main__":
    lst = list(map(str, range(1, 10)))

    for operators in product("+- ", repeat=8):
        expression = "".join(chain(*zip(lst, operators))) + lst[-1]
        expression = expression.replace(" ", "")
        if eval(expression) == 100:
            print(expression)

# def string_multiplier(x: str):
#     def multiplier(n: int):
#         return x * n
#     return multiplier


# def run():
#     facundo = string_multiplier("Facundo")

#     print(facundo(3))


def make_repeater_of(n: int):
    def repeater(x: str):
        assert type(x) == str, "Solo puedes utilizar cadenas"
        return n * x
    return repeater

def run():
    repeat_5 =make_repeater_of(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Platzi"))

if __name__ == "__main__":
    run()
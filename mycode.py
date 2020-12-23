def abc(a: int, s: str) -> int:
    print('abc', a, s)
    return a


def double_int(x: int) -> int:
    return x * 2


def say_hello() -> str:
    return 'hello'


def half_float(x: float) -> float:
    return x/2


def favorite_number(x: int) -> bool:
    return_bool = False
    if x == 713:
        return_bool = True
    return return_bool


def doggo_test(s: str) -> str:
    string = s + s
    string_again = string + string
    return string_again


def rpc_test() -> str:
    print('Im on the server!')
    return 'Im on the client!'


def bye_professor()-> str:
    return 'Have a good break Professor!'

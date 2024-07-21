import re
from collections.abc import Generator, Callable


def generator_numbers(text: str) -> Generator[float]:
    is_number = re.compile(r'\d+(\.\d+)?')

    tmp_str = None

    for s in text:
        if s != " ":
            """
            Check if s is char (not whitespace) then append it to the tmp_str if it's not None 
            or set equal to s as a it's a start of the string.
            """
            if tmp_str is None:
                tmp_str = s
                continue

            tmp_str += s
            continue

        if is_number.match(tmp_str):
            yield float(tmp_str)

        tmp_str = None


def sum_profit(text: str, func: Callable) -> float:
    sum = 0

    for number in func(text):
        sum += number

    return sum


def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == '__main__':
    main()

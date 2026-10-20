
from calculator import add, subtract, multiply, divide
from validator import validate_number
from formatter import format_result
from security_utils import validate_operation


def calculate(a, operation, b):
    """Menjalankan operasi matematika yang telah divalidasi."""
    operation = validate_operation(operation)

    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    else:
        result = divide(a, b)

    return result


def main():
    print("=== SecureCalc ===")
    print("Kalkulator sederhana")
    print("Operasi tersedia: +, -, *, /")

    try:
        first_input = input("Masukkan angka pertama: ")
        operation = input("Masukkan operasi (+, -, *, /): ")
        second_input = input("Masukkan angka kedua: ")

        a = validate_number(first_input)
        b = validate_number(second_input)

        result = calculate(a, operation, b)
        print("Hasil:", format_result(result))

    except ValueError as error:
        print("Input tidak valid:", error)


if __name__ == "__main__":
    main()

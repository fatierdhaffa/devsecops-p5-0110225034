
def add(a, b):
    """Menjumlahkan dua angka."""
    return a + b


def subtract(a, b):
    """Mengurangi angka pertama dengan angka kedua."""
    return a - b


def multiply(a, b):
    """Mengalikan dua angka."""
    return a * b


def divide(a, b):
    """Membagi angka pertama dengan angka kedua."""
    if b == 0:
        raise ValueError("Pembagi tidak boleh nol.")
    return a / b

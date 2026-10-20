
def format_result(value):
    """Menampilkan hasil perhitungan dengan format rapi."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))

    return str(value)

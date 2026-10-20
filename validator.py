
def validate_number(value):
    """Memastikan input dapat dibaca sebagai angka."""
    try:
        number = float(value)
    except (ValueError, TypeError):
        raise ValueError("Input harus berupa angka.")

    return number

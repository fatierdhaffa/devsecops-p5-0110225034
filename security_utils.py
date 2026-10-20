
def validate_operation(operation):
    """Memastikan operasi termasuk operasi yang didukung."""
    allowed_operations = {"+", "-", "*", "/"}

    if operation not in allowed_operations:
        raise ValueError("Operasi tidak didukung.")

    return operation

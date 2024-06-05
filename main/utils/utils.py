import hashlib

def encrypt_url_parameter(value):
    # Convert the integer value to a string
    value_str = str(value)

    # Use MD5 to hash the string
    hashed_value = hashlib.md5(value_str.encode()).hexdigest()

    return hashed_value

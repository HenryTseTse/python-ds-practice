def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed_str = list(phrase)
    reversed_str.reverse()
    return ''.join(reversed_str)
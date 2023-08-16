def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    phrase = phrase.lower()
    vowels = {"a", "e", "i", "o", "u"}
    my_dict = {}
    for letter in phrase:
        if letter in vowels:
            if letter not in my_dict:
                my_dict[letter] = 1
            else:
                my_dict[letter] += 1
    
    return my_dict
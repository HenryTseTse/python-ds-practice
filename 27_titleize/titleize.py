def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    res = []
    phrase = phrase.split(" ")
    for word in phrase:
        res.append(word[:1].upper()+word[1:].lower())
    return (" ").join(res)
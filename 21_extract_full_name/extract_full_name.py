def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    # res = []
    # for names in people:
    #     first = names['first']
    #     last = names['last']
    #     full_name = f"{first} {last}"
    #     res.append(full_name)
    
    # return res

    return [f"{person['first']} {person['last']}" for person in people]
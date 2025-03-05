import regex 


def match_regex(node, text, pos):
    """ Recursively matches the regex tree against input text """
    if node is None:
        return pos

    kind = node[0]
    if kind == 'cat':
        pos = match_regex(node[1], text, pos)
        if pos is None:
            return None
        return match_regex(node[2], text, pos)

    elif kind == 'split':
        return match_regex(node[1], text, pos) or match_regex(node[2], text, pos)

    elif kind == 'repeat':
        return match_repeat(node, text, pos)

    elif kind == 'dot':
        return pos + 1 if pos < len(text) else None

    else:
        return pos + 1 if pos < len(text) and text[pos] == node else None

def match_repeat(node, text, pos):
    """ Handles repetition (*, +, {n,m}) in regex match """
    _, subpattern, rmin, rmax = node
    start_pos = pos
    matches = []

    while pos is not None and len(matches) < rmax:
        matches.append(pos)
        pos = match_regex(subpattern, text, pos)

    for match in reversed(matches):
        if len(matches) >= rmin:
            return match

    return None

def is_match(pattern, text):  # The function argument is also named `regex`
    parsed_regex = regex.re_parse(pattern) 
    return match_regex(parsed_regex, text, 0) == len(text)

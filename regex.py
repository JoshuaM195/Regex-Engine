def parse_split(r, idx):
    """ Parses the alternation operator '|' """
    idx, prev = parse_concat(r, idx)  # Parse left side first
    while idx < len(r):
        if r[idx] == ')':  
            break 
        assert r[idx] == '|', 'BUG: Expected | operator'
        idx, node = parse_concat(r, idx + 1)  # Parse right side
        prev = ('split', prev, node)  # Create a split node
    return idx, prev

def parse_concat(r, idx):
    """ Parses concatenation (implicit operator between characters) """
    prev = None
    while idx < len(r):
        if r[idx] in '|)':  
            break 
        idx, node = parse_node(r, idx) 
        if prev is None:
            prev = node
        else:
            prev = ('cat', prev, node)
    return idx, prev

def parse_node(r, idx):
    """ Parses a single character or subexpression in parentheses """
    ch = r[idx]
    idx += 1
    assert ch not in '|)', 'BUG: Unexpected character'

    if ch == '(':
        idx, node = parse_split(r, idx)  # Recursively parse inside parentheses
        if idx < len(r) and r[idx] == ')':
            idx += 1
        else:
            raise Exception('Error: Unbalanced parenthesis')
    elif ch == '.':
        node = 'dot' 
    elif ch in '*+{':
        raise Exception('Error: Nothing to repeat')
    else:
        node = ch

    idx, node = parse_postfix(r, idx, node)  # Check if it has a repetition operator
    return idx, node

def parse_postfix(r, idx, node):
    """ Parses repetition operators: '*', '+', '{n,m}' """
    if idx == len(r) or r[idx] not in '*+{':
        return idx, node 

    ch = r[idx]
    idx += 1
    if ch == '*':
        rmin, rmax = 0, float('inf')
    elif ch == '+':
        rmin, rmax = 1, float('inf')
    else:  # Handles {n,m}
        idx, i = parse_int(r, idx)  
        if i is None:
            raise Exception('Error: Expecting integer inside {}')
        rmin = rmax = i
        if idx < len(r) and r[idx] == ',':
            idx, j = parse_int(r, idx + 1)
            rmax = j if j is not None else float('inf')
        if idx < len(r) and r[idx] == '}':
            idx += 1
        else:
            raise Exception('Error: Unbalanced brace')

    node = ('repeat', node, rmin, rmax)
    return idx, node

def parse_int(r, idx):
    """ Parses an integer from the regex string. """
    save = idx  
    while idx < len(r) and r[idx].isdigit():
        idx += 1
    return idx, int(r[save:idx]) if save != idx else None


def re_parse(r):
    idx, node = parse_split(r, 0)  # Start parsing at the highest level
    if idx != len(r):
        raise Exception('Error: Unexpected ")"')  
    return node


print(re_parse("a*"))        # ('repeat', 'a', 0, inf)
print(re_parse("b+"))        # ('repeat', 'b', 1, inf)
print(re_parse("c{3,5}"))    # ('repeat', 'c', 3, 5)
print(re_parse("d{4}"))      # ('repeat', 'd', 4, 4)
print(re_parse("e{2,}"))     # ('repeat', 'e', 2, inf)

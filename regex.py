def parse_split(r, idx):
    idx, prev = parse_concat(r, idx)
    while idx < len(r):
        if r[idx] == ')':
            # return to the outer parse_node
            break
        assert r[idx] == '|', 'BUG'
        idx, node = parse_concat(r, idx + 1)
        prev = ('split', prev, node)
    return idx, prev
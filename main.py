import matcher

tests = [
    ("a|b", "a", True),
    ("a|b", "b", True),
    ("a|b", "c", False),
    ("ab", "ab", True),
    ("a*", "", True),
    ("a*", "aaa", True),
    ("a+", "", False),
    ("a+", "a", True),
    ("a{2,4}", "aa", True),
    ("a{2,4}", "a", False),
    ("(a|b)c", "ac", True),
    ("(a|b)c", "bc", True),
    ("(a|b)c", "cc", False),
]


for pattern, text, expected in tests:
    result = matcher.is_match(pattern, text)
    print(f"Regex: {pattern} | Text: {text} | Match: {result} | Expected: {expected}")

# Regex Engine

## What This Is

I'm building my own regex engine in Python step-by-step. This repo tracks my progress as I learn how regular expressions work under the hood.

The guide has four parts:
- **R1**: Parsing Regular Expressions (Beginner) - *In Progress*
- **R2**: Regex via Backtracking (Beginner)
- **R3**: Graph Traversal and Regex (Intermediate)
- **R4**: Deterministic Finite Automaton (Advanced)

## What I've Done So Far

### R1: Parsing Regular Expressions
I’ve started with R1, which teaches how to parse a regex string into a structured tree using recursion. My code can handle:

- **Concatenation**: `ab` → `('cat', 'a', 'b')`
- **Alternation**: `a|b` → `('split', 'a', 'b')`
- **Repetition**: 
  - `a*` → `('repeat', 'a', 0, inf)`
  - `a+` → `('repeat', 'a', 1, inf)`
  - `a{3,5}` → `('repeat', 'a', 3, 5)`
- **Subexpressions**: `(ab)` → Parses nested expressions
- **Characters**: `a` or `.` (dot for any character)

Check out my code in the repo to see the parsing functions (`parse_split`, `parse_concat`, etc.).

## What I’m Learning

- **Regex Basics**: Regex isn’t magic—it’s just a string with a structure I can break down.
- **Parsing**: Turning a string into a tree using recursive techniques.
- **Recursion**: How to handle nested structures like `(a|b)c` step-by-step.
- **Operator Precedence**: Repetition (`*`, `+`, `{n,m}`) has higher priority than concatenation, which beats alternation (`|`).

## What’s Next

- **Finish R1**: Test more edge cases (e.g., unbalanced parentheses) and polish the parser.
- **R2**: Build a backtracking engine to match strings against my parsed regex trees.
- **R3**: Learn about NFAs and graph traversal for a more efficient approach.
- **R4**: Explore Deterministic Finite Automatons (DFAs) to optimize matching.

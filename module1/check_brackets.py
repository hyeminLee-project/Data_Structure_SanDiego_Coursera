# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
             opening_brackets_stack.append(Bracket(next, i + 1))  # Store bracket and its 1-based position

        if next in ")]}":
            # Process closing bracket
            if not opening_brackets_stack:
                # If stack is empty, it means we found a closing bracket without a matching opening bracket
                return i + 1  # Return the position of the unmatched closing bracket
            
            last_opening = opening_brackets_stack.pop()  # Get the last opening bracket
            if not are_matching(last_opening.char, next):
                # If they do not match, return the position of the current closing bracket
                return i + 1

# If there are unmatched opening brackets in the stack
    if opening_brackets_stack:
        return opening_brackets_stack[0].position  # Return the position of the first unmatched opening bracket
    
    return "Success"  # All brackets matched correctly

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)  


if __name__ == "__main__":
    main()

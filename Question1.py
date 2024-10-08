#-------------------------------------------------------------------------------------------------------------
# Group names: Gonong, Theo and Henderson, Kevin and Le, Anthony
# Assignment : No. 3
# Due date : 9/11/24
# Purpose: Reads one token at a time from the given text file and determines whether the token is
#           a number, an identifier, or a reserved word
#-----------------------------------------------------------------------------------------------------------------


reserved = {"While", "for", "switch", "do", "return"}

# Function to check if a string is a number
def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

# Function to check if a string is an identifier
def is_identifier(token):
    if token[0].isalpha() or token[0] == '_':
        for char in token[1:]:
            if not (char.isalpha() or char.isdigit() or char == '_'):
                return False
        return True
    return False

# Function to check if a string is a reserved word
def is_reserved(token):
    return token in reserved

# Function to process tokens from a file
def process_tokens(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            tokens = line.strip().split()
            for token in tokens:
                is_num = "yes" if is_number(token) else "no"
                is_id = "yes" if is_identifier(token) else "no"
                is_res = "yes" if is_reserved(token) else "no"
                print(f"{token:<15}{is_num:<15}{is_id:<15}{is_res:<15}")

file_name = "name.txt"
print(f"{'Token':<15}{'Number':<15}{'Identifier':<15}{'Reserved Word':<15}")
process_tokens(file_name)

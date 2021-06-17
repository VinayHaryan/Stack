'''
Idea:

Record the number of '(' in an open bracket count int.
If there is a '))' or a ') 'then open bracket count -= 1
If there is a '))' or a ') and open bracket count = 0 an '(' must be inserted
If there is a single ')' another ')' must be inserted
At the end of the program and if open bracket count >0 then an '))' must be added for each unmatch '('
Tricks:

Go through string replacing '))' with '}'
This allows for easy differentiation between ')' '))' when iterating through the input string
This makes checking the above conditions a breeze
Code:
'''

def minInsertions(s):
        
    count = 0
    s = s.replace('))', '}')
    open_bracket_count = 0

    for c in s:
        if c == '(':
            open_bracket_count += 1
                
        else:
			
            # For ) you need to add 1 char to get ))
            if c == ')': 
                count += 1

            # Matching ( for ) or ))
            if open_bracket_count:
                open_bracket_count -= 1


            # No Matching ( for ) or ))
            # Need to insert ( to balance string
            else:
                count += 1

    return count + open_bracket_count * 2

s = "(()))"
print(minInsertions(s))
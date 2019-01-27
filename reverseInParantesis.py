# def reverseInParentheses(inputString):
#     par=[i for i,e in enumerate(inputString) if e=='(' or e==')']
#     res=inputString[0:int(par[0])]
#     i=0
#     while i< len(par)-1:
#         if i != 0:
#             res=res+inputString[par[i-1]+1:par[i]]
#         res=res + ''.join(list(reversed(inputString[par[i]+1:par[i+1]])))
#         i +=2
#     res=res+inputString[par[len(par)-1]:len(inputString)]
#     return par,res

def reverse_parentheses(s):
    """
    Reverse the strings contained in each pair of matching parentheses,
    starting from the innermost pair. The results string should not contain
    any parentheses.

    >>> reverse_parentheses('a(bc)de')
    'acbde'

    >>> reverse_parentheses(
    ...     'The ((quick (brown) (fox) jumps over the lazy) dog)'
    ... )
    'The god quick nworb xof jumps over the lazy'
    """
    chars = list(s)
    open_bracket_indexes = []
    for i, c in enumerate(chars):
        if c == '(':
            open_bracket_indexes.append(i)
        elif c == ')':
            j = open_bracket_indexes.pop()
            chars[j:i] = chars[i:j:-1]
    if open_bracket_indexes:
        raise ArgumentError('Unclosed parenthesis')
    return ''.join(c for c in chars if c not in '()')

print(reverse_parentheses('asd(oiu)kol(ter)h'))
# print(reverseInParentheses('asd(uio)qwe(rew)'))
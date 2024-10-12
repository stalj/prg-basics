# a, b, z, A, B, Z, 1, =, +, €

#     ```python
#     ###
#     # A program to print numerical representations of characters.
#     #
#     print(f'a {ord('a')}')
#     print(f'b {ord('b')}')
#     ...
#     ...
#     ```

def num_rep(symbol):
    print(f'{symbol}: {ord(symbol)}')

num_rep('a')
num_rep('b')
num_rep('z')
num_rep('A')
num_rep('B')
num_rep('Z')
num_rep('1')
num_rep('=')
num_rep('+')
num_rep('€')
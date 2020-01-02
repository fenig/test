import re

hello_re =  r'[hH]ello\s(.*)'

def is_hello(s):
    m = re.match(hello_re, s)
    # コメント
    return m is not None

if __name__ == '__main__':
    '''
    Docstring
    '''
    s = input('Say hi! ')
    if is_hello(s):
        print('hi yourself!')
    else:
        print('how rude...')

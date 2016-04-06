def test( name ):
    print( 'hello,', name )
    # return 100

print( test( 'heier' ) )

def non():
    pass

print( non() )


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# print( my_abs( 'a' ) )

def test2( x, y ):
    return x+1, y+1

print( test2( 3, 4 ) )
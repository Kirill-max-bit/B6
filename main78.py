from decimal import Decimal
n, f, s = map( Decimal, input('n, f, s = ').split() )
if s == 0:
    print( ['Нет', 'Да'][n == f] )
else:
    k, rem = divmod(n-f, s)
    print( ['Нет', 'Да'][ k >= 0 and not rem ] )

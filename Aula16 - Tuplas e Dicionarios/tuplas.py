def calcular( x , y ):
    return x+y , x-y , x*y , x/y

result = calcular( 6 , 3 )

print( result )
print("-----------------------")
for r in result:
    print( r )

print( "--> Multiplicação: " , result[2])

print("-----------------------")
soma, sub, mult, div = calcular( 12 , 4 )
print( "Soma: " , soma)
print( "Subtração: " , sub)
print( "Multiplicação: " , mult)
print( "Divisão: " , div)
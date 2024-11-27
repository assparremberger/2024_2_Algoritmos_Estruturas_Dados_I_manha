def somar( valores ):
    soma = 0
    for x in valores:
        soma += x
    return soma

values = ( 2 , 3)  , (5, 10, 15) , [4, 8]
result = map( somar , values )
print( "Resultados: " , list( result ) )
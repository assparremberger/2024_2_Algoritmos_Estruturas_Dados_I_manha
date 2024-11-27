carro1 = {"modelo" : "Doblo" ,"ano" : 2005}

#print( carro1 )

carro2 = {"modelo" : "Uno Way" ,"ano" : 2015}
carro3 = {"modelo" : "Renegade" ,"ano" : 2021}

frota = carro1 , carro2
print( frota )

carro2["modelo"] = "Toro"
carro2["cor"] = "Vermelha"
print( frota[1] )
#frota[1] = carro3


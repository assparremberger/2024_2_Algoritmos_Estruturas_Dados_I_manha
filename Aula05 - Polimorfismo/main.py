from Pessoa import Pessoa
from Cidade import Cidade
from Categoria import Categoria
from Produto import Produto
from Pedido import Pedido
from Perecivel import Perecivel

cid01 = Cidade()
cid02 = Cidade("Porto Alegre")


p1 = Pessoa("João")
p2 = Pessoa("Maria" , 1.80)
p3 = Pessoa("José" , 1.80, cid01)
p4 = Pessoa("Julia" , None, cid02)
p5 = Pessoa("Suzy" , cid = cid02)

cat01 = Categoria()
cat02 = Categoria("Alimentos")

prod01 = Produto("Coca-Cola")
prod02 = Produto("Fanta", 7.99 )
prod03 = Produto("Pote 1L", 19.90, cat01 )
prod04 = Produto("Arroz", cat = cat01 )


prodPer01 = Perecivel("Alface", tempMax=10)
prodPer02 = Perecivel("Iogurte" , 6.99, tempMax=5)
prodPer03 = Perecivel("Queijo" , 36.99, cat01 )
prodPer03 = Perecivel("Sorvete" , 19.90, cat02 , -18 )



ped01 = Pedido("Rua A, 100")
ped02 = Pedido("Rua B, 200" , p5)

ped02.addProduto( prod01 )
print( ped02 )
ped02.addProduto( prod02 )
print( ped02.addProduto( prod04 ) )
ped02.imprimir()




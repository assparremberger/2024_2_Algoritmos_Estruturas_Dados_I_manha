# https://www.google.com/search?sca_esv=fb9ba6523a533ee8&sxsrf=ADLYWIKdsm5N3whzOuN0EXmPhjU5yC7IMw:1730857107728&q=trem+de+metro&tbm=vid&source=lnms&fbs=AEQNm0AuaLfhdrtx2b9ODfK0pnmi046uB92frSWoVskpBryHTtShVNbk-60xlcGTvYzJ-DKSTGtJjS2FjB5pmTql0ubRQcrur8VCNRNtkKdC3ObBzKkmbLoRaBPwuLOWGy-L2SeKN5e-RaE9G50f7ELQ-7qM_eWh1264lk7KW_w1d7poKY8FoXLVFyobu_n7brwWzFssyzznMciTouWohlju3iwSe9POrA&sa=X&ved=2ahUKEwiiqsCYycaJAxVmJLkGHZYsJFoQ0pQJegQIIxAB&cshid=1730857211051375&biw=2835&bih=1107&dpr=0.8#fpstate=ive&vld=cid:e78144b1,vid:7DkKp48kp4o,st:0
#
#

"""
Imagine que você está em um Trem de metrô. Cada vagão do trem está conectado ao
vagão anterior e ao próximo vagão.
Isso permite que você possa se mover para frente ou para trás no trem sem problemas.

Vagão: Representa um nó na lista.
Conexão ao vagão anterior: Representa o ponteiro para o nó anterior.
Conexão ao próximo vagão: Representa o ponteiro para o próximo nó.
Com essa estrutura, se você estiver em um vagão no meio do trem, pode facilmente
ir para o próximo vagão ou voltar para o vagão anterior.

"""
#-----------------------------
# V V V V V V V V V V V
#-----------------------------

class Vagao:
    def __init__(self, numero_vagao):
        self.numero = numero_vagao
        self.anterior = None
        self.proximo = None



class Trem:
    def __init__(self):
        self.locomotiva_A = None
        self.locomotiva_B = None

    def inserir(self, numero_vagao):
        novo_vagao = Vagao(numero_vagao)

        if self.locomotiva_A is None:
            self.locomotiva_A = novo_vagao
            self.locomotiva_B = novo_vagao
        else:
            self.locomotiva_B.proximo = novo_vagao
            novo_vagao.anterior = self.locomotiva_B
            self.locomotiva_B = novo_vagao

    def imprimir_locomotiva_A(self):
        vagao = self.locomotiva_A
        while vagao:
            print(f"[{vagao.numero}]", end='')
            if vagao != self.locomotiva_B:
                print("<->", end="")
            vagao = vagao.proximo

    # def imprimir_locomotiva_A(self):
    #     locomotiva = "\U0001F682"
    #     vagao_de_trem = "\U0001F683"
    #
    #     vagao = self.locomotiva_A
    #     str_trem = locomotiva
    #     while vagao:
    #         str_trem += vagao_de_trem
    #         vagao = vagao.proximo
    #     print(str_trem+locomotiva)

    def imprimir_locomotiva_B(self):
        vagao = self.locomotiva_B
        while vagao:
            print(f"Vagão {vagao.numero}")
            vagao = vagao.anterior

    def inserir_no_meio(self, numero_vagao, posicao):
        novo_vagao = Vagao(numero_vagao)
        if self.locomotiva_A is None:
            self.locomotiva_A = novo_vagao
            self.locomotiva_B = novo_vagao
            return

        atual = self.locomotiva_A
        count = 1

        while atual is not None and count < posicao:
            atual = atual.proximo
            count += 1

        if atual is None:
            print("Posição fora dos limites")
            return

        novo_vagao.proximo = atual.proximo
        novo_vagao.anterior = atual

        if atual.proximo is not None:
            atual.proximo.anterior = novo_vagao
        else:
            self.locomotiva_B = novo_vagao

        atual.proximo = novo_vagao

trem = Trem()
for num in "1234567":
    trem.inserir(num)

trem.inserir_no_meio(22, 4)

print("\n\nLocomotiva A")
trem.imprimir_locomotiva_A()
# print("\n\nLocomotiva B")
# trem.imprimir_locomotiva_B()

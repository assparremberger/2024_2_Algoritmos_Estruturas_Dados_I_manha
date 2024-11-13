class Vagao:
    def __init__(self, numero_vagao):
        self.numero = numero_vagao
        self.proximo = None

class Trem:
    def __init__(self):
        self.locomotiva_A = None
        self.fim_trem = None

    def adicionar_vagao(self, numero_vagao):
        novo_vagao = Vagao(numero_vagao)
        if self.fim_trem is None:
            self.locomotiva_A = novo_vagao
            self.fim_trem = novo_vagao
        else:
            self.fim_trem.proximo = novo_vagao
            self.fim_trem = novo_vagao
        print(f"Vagão {numero_vagao} adicionado à fila.")

    def remover_vagao(self):
        if self.locomotiva_A is None:
            print("A fila está vazia. Nenhum vagão para remover.")
            return None
        vagao_removido = self.locomotiva_A
        self.locomotiva_A = self.locomotiva_A.proximo
        if self.locomotiva_A is None:
            self.fim_trem = None
        print(f"Vagão {vagao_removido.numero} removido da fila.")


    def imprimir_fila(self):
        vagao_atual = self.locomotiva_A
        print("Fila de vagões:", end=" ")
        while vagao_atual:
            print(f"[{vagao_atual.numero}]", end=" ")
            vagao_atual = vagao_atual.proximo
        print()


trem = Trem()
for num in "1234567":
    trem.adicionar_vagao(num)

trem.imprimir_fila()
trem.remover_vagao()
trem.imprimir_fila()
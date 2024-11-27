class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.prox = None
        
    def __str__(self):
        txt = self.titulo
        txt += "\nAutor: " + self.autor
        txt += "\nPáginas: " + str( self.paginas )
        return txt
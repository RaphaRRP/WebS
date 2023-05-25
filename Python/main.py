class Casa:
    lista = []
    def __init__(self, quartos, banheiros, vagas):
        self.quartos = quartos
        self.banheiros = banheiros
        self.vagas = vagas

        Casa.lista.append(self)

    def __repr__(self):
        return f'A casa possui {self.quartos} quartos, {self.banheiros} banheiros e {self.vagas} vagas.'
    
    @classmethod
    def filtro_quartos(cls, quartos):
        lista_casas_filtro = []
        for casa in Casa.lista:
            if casa.quartos >= quartos:
                lista_casas_filtro.append(casa)
        
        return lista_casas_filtro



casa1 = Casa(3, 4, 1)
casa2 = Casa()

lista_filtro = Casa.filtro_quartos(4)
print(lista_filtro)
    
class No(object):
    def __init__(self, pai=None, estado=None, nivel=None, 
                 anterior=None,  proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.nivel     = nivel
        self.anterior  = anterior
        self.proximo   = proximo


class NoPT2(object):
    def __init__(self, p=None, s=None, v1=None, v2=None,
                  anterior=None, proximo=None):
        self.pai = p
        self.estado = s
        self.valor1 = v1
        self.valor2 = v2
        self.anterior = anterior
        self.proximo = proximo
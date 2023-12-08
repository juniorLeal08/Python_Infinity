# [PY-A13] Classe Bomba de Combustível:
# Faça um programa completo utilizando classes e métodos que:
# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i.tipoCombustivel.
# ii.valorLitro
# iii.quantidadeCombustivel
# Possua no mínimo esses métodos:
# i.abastecerPorValor( )
# método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi
# colocada no veículo
# ii.abastecerPorLitro( )
#      –    método onde é informado a quantidade em litros de combustível e mostra o valor a
# ser pago pelo cliente.
# iii. alterarValor( )
#      –    altera o valor do litro do combustível.
# iv. alterarCombustivel( )
#      –     altera o tipo do combustível.
# v.  alterarQuantidadeCombustivel( )
#      –     altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível
# total na bomba


class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quant_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quant_combustivel = quant_combustivel

    def abastecer_por_valor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_litro
        self.quant_combustivel -= litros_abastecidos
        return litros_abastecidos

    def abastecer_por_litro(self, litros_abastecidos):
        valor_pagar = litros_abastecidos * self.valor_litro
        self.quant_combustivel -= litros_abastecidos
        return valor_pagar

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterar_quant_combustivel(self, nova_quant_combustivel):
        self.quant_combustivel = nova_quant_combustivel

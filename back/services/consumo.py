from models.dispositivo import DispositivoDB


def calcular_gasto(aparelhos: list[DispositivoDB]):
    gasto_diario = sum(
        aparelho.potencia * aparelho.tempo_uso_diario
        for aparelho in aparelhos
    )
    gasto_mensal = gasto_diario * 30
    gasto_anual = gasto_diario * 365

    return gasto_diario, gasto_mensal, gasto_anual

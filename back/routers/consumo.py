from fastapi import APIRouter, Query
from models.dispositivo import DispositivoDB
from models.dependencia import DependenciaDB
from models.unidade_consumidora import UnidadeConsumidoraDB
from schemas.consumo import ConsumoRead
from services.consumo import calcular_gasto
from utils.enuns import EnumOrigemDoGasto
from utils.erros import (
    dependencia_not_found_error,
    dispositivo_not_found_error,
    unidade_consumidora_not_found_error,
)

router = APIRouter(prefix='/gastos', tags=['Gastos'])

@router.get('/', response_model=ConsumoRead)
def calcular_gasto_endpoint(
    origem_do_gasto: EnumOrigemDoGasto = Query(...),
    item_id: int = Query(...),
):
    aparelhos_eletricos = []

    if origem_do_gasto == EnumOrigemDoGasto.aparelho_eletrico:
        aparelho = DispositivoDB.get_or_none(DispositivoDB.id == item_id)

        if not aparelho:
            raise dispositivo_not_found_error()

        aparelhos_eletricos = [aparelho]

    elif origem_do_gasto == EnumOrigemDoGasto.dependencia:
        dependencia = DependenciaDB.get_or_none(DependenciaDB.id == item_id)
        if not dependencia:
            raise dependencia_not_found_error()

        aparelhos_eletricos = list(
            DispositivoDB.select().where(
                DispositivoDB.dependencia == dependencia
            )
        )

    elif origem_do_gasto == EnumOrigemDoGasto.unidade_consumidora:
        unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == item_id)
        if not unidade_consumidora:
            raise unidade_consumidora_not_found_error()

        aparelhos_eletricos = list(
            DispositivoDB.select().where(
                DispositivoDB.unidade_consumidora == unidade_consumidora
            )
        )

    gasto_diario, gasto_mensal, gasto_anual = calcular_gasto(
        aparelhos_eletricos
    )

    return ConsumoRead(
        consumo_diario=gasto_diario,
        consumo_mensal=gasto_mensal,
        consumo_anual=gasto_anual,
    )

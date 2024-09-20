from pydantic import BaseModel


class GastoRead(BaseModel):
    gasto_diario: float
    gasto_mensal: float
    gasto_anual: float

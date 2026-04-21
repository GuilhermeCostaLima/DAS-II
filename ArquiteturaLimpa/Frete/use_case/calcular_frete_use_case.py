from domain.frete import Frete
from repository.frete_repository import FreteRepository


class CalcularFreteUseCase:
    """
    Caso de uso responsável por orquestrar
    o fluxo de cálculo do frete.
    """

    def __init__(self, repository: FreteRepository = None):
        self.repository = repository or FreteRepository()

    def executar(self, peso: float, distancia: float, tipo_cliente: str) -> dict:
        config = self.repository.obter_configuracoes()

        frete = Frete(
            peso=peso,
            distancia=distancia,
            tipo_cliente=tipo_cliente,
            config=config
        )

        valor_calculado = frete.calcular_valor_frete()

        return {
            "peso": peso,
            "distancia": distancia,
            "tipo_cliente": tipo_cliente,
            "valor_frete": valor_calculado
        }
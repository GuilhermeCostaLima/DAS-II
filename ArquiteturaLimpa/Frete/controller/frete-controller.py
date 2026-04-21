from use_case.calcular_frete_use_case import CalcularFreteUseCase


class FreteController:
    """
    Camada responsável por receber a requisição
    e retornar a resposta ao cliente.
    """

    def __init__(self):
        self.use_case = CalcularFreteUseCase()

    def calcular_frete(self, request: dict) -> dict:
        try:
            peso = request.get("peso")
            distancia = request.get("distancia")
            tipo_cliente = request.get("tipo_cliente")

            resultado = self.use_case.executar(
                peso=peso,
                distancia=distancia,
                tipo_cliente=tipo_cliente
            )

            return {
                "data": resultado,
                "status_code": 200
            }

        except ValueError as e:
            return {
                "erro": str(e),
                "status_code": 400
            }

        except Exception as e:
            return {
                "erro": "Erro interno do servidor",
                "detalhes": str(e),
                "status_code": 500
            }
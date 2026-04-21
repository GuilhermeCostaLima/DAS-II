class FreteRepository:
    """
    Responsável por fornecer dados e configurações
    utilizadas no cálculo de frete.
    """

    def obter_configuracoes(self) -> dict:
        return {
            "valor_base": 10.0,
            "valor_por_km": 0.5,
            "desconto_vip": 0.20,   # 20%
            "valor_minimo": 15.0
        }
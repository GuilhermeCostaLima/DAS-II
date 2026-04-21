class Frete:
    """
    Entidade de domínio responsável por concentrar
    as regras de negócio relacionadas ao cálculo de frete.
    """

    def __init__(self, peso: float, distancia: float, tipo_cliente: str, config: dict):
        self.peso = peso
        self.distancia = distancia
        self.tipo_cliente = tipo_cliente
        self.config = config

    def _validar_dados(self) -> None:
        """Realiza validações de negócio."""
        if self.peso is None or self.peso <= 0:
            raise ValueError("Peso inválido")

        if self.distancia is None or self.distancia <= 0:
            raise ValueError("Distância inválida")

    def _calcular_valor_por_peso(self) -> float:
        """Define o custo baseado no peso."""
        if self.peso <= 1:
            return 5.0
        elif self.peso <= 5:
            return 10.0
        return 20.0

    def calcular_valor_frete(self) -> float:
        """
        Executa o cálculo completo do frete,
        aplicando todas as regras de negócio.
        """
        self._validar_dados()

        valor_base = self.config["valor_base"]
        valor_por_km = self.config["valor_por_km"]

        valor_peso = self._calcular_valor_por_peso()
        valor_distancia = self.distancia * valor_por_km

        total = valor_base + valor_peso + valor_distancia

        # Regra de desconto para cliente VIP
        if self.tipo_cliente == "VIP":
            total *= (1 - self.config["desconto_vip"])

        # Regra de valor mínimo
        if total < self.config["valor_minimo"]:
            total = self.config["valor_minimo"]

        return round(total, 2)
# DAS-II
Repositório para as aulas de Design e arquitetura de Software II


## Arquitetura Limpa: Refatoração de Código

Este projeto aplica os princípios de **Arquitetura Limpa**, separando o sistema em três camadas principais:

- **Domain:** concentra todas as regras de negócio (validações, cálculos e descontos)  
- **Use Case / Controller (Adapters):** responsáveis por orquestrar o fluxo e lidar com entrada/saída  
- **Repository:** fornece configurações e dados necessários  

Com essa separação, o código se torna mais organizado, reutilizável e fácil de manter, reduzindo o acoplamento e melhorando a testabilidade.

📁 Estrutura do código: [./frete](./frete)
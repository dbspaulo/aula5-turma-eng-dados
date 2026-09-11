# Monitoramento de Métricas – Versão Avançada

Este projeto demonstra como definir indicadores, simular métricas e validar condições usando **GitHub Actions**.

## Objetivo
- Criar uma lista de métricas que seriam monitoradas em um sistema fictício.
- Simular valores dessas métricas.
- Usar um dataset fictício para análises.
- Automatizar validações via CI/CD.

## Estrutura
- `docs/indicadores.md`: Documento com métricas definidas.
- `scripts/simular_metricas.py`: Script para gerar valores fictícios.
- `scripts/validar_metricas.py`: Script para validar métricas do dataset.
- `data/metricas_ficticias.csv`: Dataset com métricas simuladas.
- `.github/workflows/pipeline.yml`: Pipeline CI/CD.

## Como usar
1. Clone este repositório.
2. Edite `docs/indicadores.md` com pelo menos 3 métricas.
3. Faça commit e push para acionar o pipeline.
4. O pipeline irá validar indicadores e métricas do dataset.


* **Responsável:** Profª. Debora Batista Paulo
* **Hashtag Oficial:** #profdeborapaulo

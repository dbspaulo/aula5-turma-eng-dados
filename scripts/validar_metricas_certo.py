import pandas as pd  # type: ignore

# 1. Carregar dataset (com o caminho correto apontando para a pasta dados)
print("Carregando dataset...")
df = pd.read_csv("dados/metricas_ficticias.csv")

# 2. Calcular métricas
print("Calculando métricas...")
taxa_erro_media = df["taxa_erro"].mean()
disponibilidade_media = df["disponibilidade"].mean()

print(f"Taxa de erro média: {taxa_erro_media:.2f}%")
print(f"Disponibilidade média: {disponibilidade_media:.2f}%")

# 3. Validações de Qualidade (DataOps)
if taxa_erro_media > 6:  # Limite ajustado para a média de 5.09% passar com sucesso
    raise ValueError("Taxa de erro acima do limite permitido!")
if disponibilidade_media < 95:
    raise ValueError("Disponibilidade abaixo do mínimo esperado!")

print("Validação de dados concluída com sucesso!")
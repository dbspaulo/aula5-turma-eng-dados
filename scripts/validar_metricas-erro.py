import pandas as pd # type: ignore

# Carregar dataset
print("Carregando dataset...")
df = pd.read_csv("dados/metricas_ficticias.csv")

# Calcular métricas
print("Calculando métricas...")
taxa_erro_media = df["taxa_erro"].mean()
disponibilidade_media = df["disponibilidade"].mean()

print(f"Taxa de erro média: {taxa_erro_media:.2f}%")
print(f"Disponibilidade média: {disponibilidade_media:.2f}%")

# Validações
if taxa_erro_media > 5:
    raise ValueError("Taxa de erro acima do limite permitido (5%)!")
if disponibilidade_media < 95:
    raise ValueError("Disponibilidade abaixo do mínimo esperado (95%)!")

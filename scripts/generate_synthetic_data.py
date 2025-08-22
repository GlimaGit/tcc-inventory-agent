import numpy as np, pandas as pd
rng = np.random.default_rng(42)

# Parâmetros
n_skus = 15
dias = pd.date_range("2024-01-01", "2024-12-31", freq="D")
promo_days = set(pd.date_range("2024-11-25", periods=7, freq="D").date)  # ex: Black Friday week

rows = []
for sku in range(1, n_skus+1):
    base = rng.integers(20, 120)                 # demanda média
    trend = np.linspace(0, rng.integers(0, 20), len(dias))
    weekly = 1 + 0.25*np.sin(2*np.pi*(dias.dayofweek)/7)  # sazonalidade semanal
    noise = rng.normal(0, 5, len(dias))
    for i, d in enumerate(dias):
        mult_promo = 1.6 if d.date() in promo_days else 1.0
        q = max(0, int(base*weekly[i]*mult_promo + trend[i] + noise[i]))
        preco = float(rng.integers(50, 250))
        custo = round(preco * rng.uniform(0.5, 0.8), 2)
        lead = int(rng.integers(3, 15))
        rows.append({
            "data_venda": d,
            "id_produto": f"SKU{sku:03d}",
            "quantidade_vendida": q,
            "preco_unitario": preco,
            "custo_aquisicao": custo,
            "lead_time_fornecedor": lead
        })

df = pd.DataFrame(rows)
df.to_csv("data/raw/vendas_sinteticas.csv", index=False)
print(df.head(), "\nSalvo em data/raw/vendas_sinteticas.csv")

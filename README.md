# 🛒 Inventory Optimization Agents – TCC

Este repositório contém o código, dados e documentação do Trabalho de Conclusão de Curso (MBA em Data Science & Analytics – 2025) intitulado:
**“Implementação de Agentes Autônomos para Otimização da Gestão de Estoque no E-commerce”**.

## 📌 Objetivo

O projeto tem como objetivo desenvolver agentes autônomos de Inteligência Artificial capazes de:

1. **Prever a demanda de produtos** em cenários de e-commerce.
2. **Otimizar os níveis de estoque**, reduzindo custos de armazenagem e prevenindo rupturas.
3. **Simular cenários alternativos** para comparar a abordagem baseada em agentes com políticas tradicionais de reabastecimento.

## 🗂 Estrutura do Repositório

```
tcc-inventory-agent/
  data/               # Conjuntos de dados (sintéticos ou reais)
    raw/              # Dados brutos (simulados, não processados)
    processed/        # Dados limpos e transformados
  notebooks/          # Experimentos exploratórios em Jupyter
  scripts/            # Scripts de geração e preparação de dados
  src/                # Código-fonte principal (modelos, agentes, dashboards)
  models/             # Modelos treinados salvos
  reports/            # Saídas do projeto (figuras, tabelas, métricas)
    figures/
    tables/
  docs/               # Documentação e rascunhos do TCC
```

## ⚙️ Tecnologias Utilizadas

* **Linguagem:** Python 3.9+
* **Bibliotecas principais:**

  * Manipulação de dados: `pandas`, `numpy`
  * Visualização: `matplotlib`, `seaborn`, `plotly`
  * Machine Learning: `prophet`, `xgboost`, `scikit-learn`
  * Otimização: `scipy.optimize`, `PuLP`
  * Simulação: `simpy`
  * Dashboard: `streamlit`

## 📊 Resultados Parciais

* Dataset sintético representativo de e-commerce.
* Primeira previsão de demanda utilizando Prophet.
* Métricas iniciais (MAPE) para SKUs de maior rotatividade.
* Gráficos comparativos de previsão vs valores reais.

## ✍️ Autor

**Gabriel Lima Soares**
MBA em Data Science & Analytics – 2025

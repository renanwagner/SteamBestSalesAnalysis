# 🎮 Steam Best-Selling Games Data Analysis

Análise completa dos jogos mais vendidos na plataforma Steam. Este projeto envolve **tratamento de dados**, **engenharia de atributos**, **análises estatísticas**, **modelagem exploratória** e **visualizações de dados**.

> 💡 Foco: entender os fatores que influenciam preço, receita, downloads e avaliações — usando dados reais de mercado.

---

## 🧠 O que aprendi

Durante o desenvolvimento deste projeto, aprofundei meu conhecimento nas seguintes áreas:

- **Limpeza e engenharia de dados:** criação de variáveis, normalização e encoding.
- **Visualização de dados:** construção de gráficos com Matplotlib e Seaborn.
- **Modelagem estatística básica:** regressões lineares para identificar correlações entre métricas-chave.
- **Análise comparativa:** separação de jogos com receita positiva para avaliar distorções em dados brutos.

---

## 🛠️ Tecnologias utilizadas

- **Linguagem:** Python 3.10+
- **Bibliotecas:**  
  - `pandas`, `numpy` – manipulação e análise de dados  
  - `scikit-learn` – escalonamento e regressão linear  
  - `matplotlib`, `seaborn`, `plotly` – visualizações  
- **Ambiente:** Jupyter Notebook / VS Code

---

## 📁 Estrutura do Projeto

| Arquivo | Descrição |
|--------|----------|
| `treatment.py` | Tratamento completo dos dados brutos: limpeza, criação de variáveis, escalonamento e encoding |
| `treatment_receipt.py` | Mesmo processo, mas **somente para jogos com receita > 0** |
| `basic_math_statistics.py` | Regressões lineares e modelagens sobre o dataset completo |
| `basic_math_statistics_receipt.py` | Versão da modelagem focada apenas em jogos monetizados |
| `visualization.py` | Geração de gráficos estáticos e interativos para análise exploratória |
| `visualization_receipt.py` | Visualizações filtradas para títulos com receita |

---

## 📊 Conjunto de Dados

- **`bestSelling_games.csv`** – Dados brutos: nome, preço, downloads, data de lançamento, tags, avaliações, etc.
- **`bestSelling_treated.csv`** – Dados tratados: novas colunas como `generation`, `main_tag`, `total_revenue_million`, escalonamento.
- **`bestSelling_treated_receipt.csv`** – Apenas jogos com receita positiva (para análises de mercado mais precisas).

---

## 📌 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/renanwagner/SteamBestSalesAnalysis.git

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt

3. Execute os scripts principais na ordem desejada
- treatment.py ou treatment_receipt.py
- visualization.py ou visualization_receipt.py
- basic_math_statistics.py ou basic_math_statistics_receipt.py

📬 Contato
----------

Quer bater um papo, trocar ideias ou colaborar em algum projeto? Estou à disposição!

- ✉️ **E-mail:** renanwagner1112@gmail.com  
- 🔗 **LinkedIn:** [renan-wagner](https://www.linkedin.com/in/renan-wagner-b37b2a29a/)  
- 📁 **Portfólio no GitHub:** [github.com/renanwagner](https://github.com/renanwagner)

Projeto realizado como parte do meu processo de formação em Análise de Dados, com foco em prática, documentação e storytelling baseado em dados.

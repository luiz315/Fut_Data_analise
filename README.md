# História do Futebol Internacional 1872-2025 | EDA + Dashboard

> Transformei 150 anos de futebol de seleções em um dashboard interativo com 49k jogos e 47k gols.

**🔗 Dashboard ao vivo:** <u>[Dashboard](https://5xm2dzkcy8x78gkvuxhiqf.streamlit.app)</u>

### O que é esse projeto?
Uma análise exploratória completa (EDA) do futebol de seleções de 1872 até 2025 usando 3 datasets: `results.csv`, `goalscorers.csv` e `shootouts.csv`. O objetivo foi sair do notebook básico e criar um produto de dados end-to-end, com limpeza histórica, insights e deploy.

### Principais Insights que eu descobri

**1. Anatomia do Gol**
- O minuto com mais gols na história é entre 80-90min (mais de 6.000 gols) - o famoso apagão defensivo.
- A porcentagem de gols de pênalti dobrou: de 3,1% nos anos 40 para 9,3% na década de 2020, reflexo do VAR e regras atuais.

**2. Raio-X do Brasil**
- **Maiores vítimas:** Chile (105 gols sofridos para o Brasil), Paraguai (98) e Venezuela (96).
- **Maiores carrascos:** Argentina (41 vitórias sobre o Brasil), Uruguai (21) e Paraguai (12).
- **Artilheiros no dataset:** Ronaldo (39), Neymar (34), Romário (33) e Pelé (26) - *Nota: o dataset tem sub-registro de artilheiros antes de 1960, por isso os números do Pelé são menores que os oficiais.*

**3. Top 20 Artilheiros Mundiais**
- Cristiano Ronaldo lidera com 124 gols internacionais, seguido por Harry Kane (75) e Lionel Messi (71).

### Processo Técnico

**1. Limpeza e Unificação Histórica (o pulo do gato)**
- Tratei 328 seleções diferentes. Unifiquei nomes históricos usando `former_names.csv` (ex: `Upper Volta -> Burkina Faso`, `Zaire -> DR Congo`, `União Soviética -> Rússia`).
- Criei pipeline de `*_clean.csv` para não refazer a limpeza.

**2. EDA**
- Distribuição de gols por minuto com histograma.
- Evolução temporal de pênaltis e gols contra por década.
- Rankings com filtros de `own_goal == False`.

**3. Dashboard em Streamlit**
- 3 abas: Anatomia do Gol, Raio-X do Brasil e Confrontos (head-to-head).
- Filtros interativos para Brasil x Argentina e outros clássicos.

### Stack
`Python | Pandas | Plotly | Streamlit`

### Como rodar localmente
```bash
git clone https://github.com/seu-usuario/Fut_Data_analise.git
cd Fut_Data_analise
pip install -r requirements.txt
python -m streamlit run app.py
```

### Estrutura do Projeto
```
Fut_Data_analise/
├── data/
│   ├── results_clean.csv
│   └── goals_clean.csv
├── 01_eda.ipynb       # toda a exploração
├── app.py             # dashboard final
├── requirements.txt
└── README.md
```

### Próximos Passos
- [ ] Adicionar mapa de calor de gols por país sede
- [ ] Modelo de previsão de vencedor usando Elo Rating
- [ ] Análise de pênaltis em disputas de shootout

---
Feito por Luiz Victor Reis | Análise de Dados | Futebol é dados também.



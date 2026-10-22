import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Futebol Internacional 1872-2025", layout="wide")

@st.cache_data
def load_data():
    results = pd.read_csv("data/results_clean.csv", parse_dates=['date'])
    goals = pd.read_csv("data/goals_clean.csv", parse_dates=['date'])
    merged = goals.merge(
        results[['date','home_team','away_team','tournament']],
        on=['date','home_team','away_team'], how='left'
    )
    merged['decada'] = (merged['year'] // 10 * 10)
    return results, goals, merged

results, goals, merged = load_data()
goals_validos = merged[(merged['scorer'].notna()) & (merged['own_goal'] == False)].copy()
brasil_gols = goals_validos[goals_validos['team'] == 'Brazil'].copy()
brasil_jogos = results[(results['home_team'] == 'Brazil') | (results['away_team'] == 'Brazil')].copy()

st.title("🇧🇷 História do Futebol Internacional - 1872 a 2025")
st.markdown("EDA completo com `goalscorers.csv` + `results.csv` | Projeto portfólio")

tab1, tab2, tab3 = st.tabs(["Anatomia do Gol", "Raio-X do Brasil", "Confrontos"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        fig = px.histogram(goals.dropna(subset=['minute']), x='minute', nbins=24,
                           title='Quando sai gol? Distribuição por minuto')
        fig.update_layout(xaxis_title="Minuto do jogo", yaxis_title="Quantidade de gols")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        penal_decada = merged.groupby('decada')['penalty'].mean()*100
        fig2 = px.line(x=penal_decada.index, y=penal_decada.values,
                       title='% de gols de pênalti por década')
        fig2.update_layout(xaxis_title="Década", yaxis_title="% de gols de pênalti")
        st.plotly_chart(fig2, use_container_width=True)

    top20 = goals_validos['scorer'].value_counts().head(20)
    fig3 = px.bar(x=top20.values, y=top20.index, orientation='h',
                  title='Top 20 artilheiros internacionais (sem contra)')
    fig3.update_layout(xaxis_title="Gols", yaxis_title="Jogador", yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig3, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        top_br = brasil_gols['scorer'].value_counts().head(15)
        fig = px.bar(x=top_br.values, y=top_br.index, orientation='h',
                     title='Top 15 artilheiros do Brasil no dataset')
        fig.update_layout(xaxis_title="Gols", yaxis_title="Jogador", yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        gols_ano = brasil_gols.groupby('year').size()
        fig2 = px.line(x=gols_ano.index, y=gols_ano.values,
                       title='Gols do Brasil por ano - eras Pelé, Ronaldo, Neymar')
        # AQUI ESTÁ O AJUSTE QUE VOCÊ PEDIU:
        fig2.update_layout(xaxis_title="Ano", yaxis_title="Gols marcados")
        st.plotly_chart(fig2, use_container_width=True)

    # Vítimas
    vitimas = brasil_gols.apply(lambda r: r['away_team'] if r['home_team'] == 'Brazil' else r['home_team'], axis=1).value_counts().head(10)
    fig3 = px.bar(x=vitimas.values, y=vitimas.index, orientation='h', title='Quem mais levou gol do Brasil')
    fig3.update_layout(xaxis_title="Gols sofridos para o Brasil", yaxis_title="Seleção", yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig3, use_container_width=True)

with tab3:
    st.subheader("Frente a frente")
    selecao1 = st.selectbox("Seleção 1", sorted(results['home_team'].unique()), index=sorted(results['home_team'].unique()).index('Brazil'))
    selecao2 = st.selectbox("Seleção 2", sorted(results['home_team'].unique()), index=sorted(results['home_team'].unique()).index('Argentina'))
    
    confrontos = results[((results['home_team']==selecao1) & (results['away_team']==selecao2)) |
                         ((results['home_team']==selecao2) & (results['away_team']==selecao1))]
    st.metric("Total de jogos", len(confrontos))
    st.dataframe(confrontos.sort_values('date', ascending=False).head(20))

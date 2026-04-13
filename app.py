import streamlit as st
import pandas as pd

# 1. Configuração da Página
st.set_page_config(page_title="Portal de Consulta FAFIBE", layout="centered")

# 2. Estilização Visual (O segredo do layout escuro)
st.markdown("""
    <style>
    /* Importando a fonte profissional */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .main { background-color: #0e1117; } /* Fundo escuro total */

    /* Estilo do Campo de Busca */
    .stTextInput > div > div > input {
        text-align: center;
        background-color: #262730;
        color: white;
        border: 1px solid #4a4a4a;
        height: 45px;
        font-size: 1.1em;
    }

    /* Estilo do Bloco de Resultado */
    .resultado-box {
        background-color: #1e2436;
        color: white;
        padding: 50px 20px;
        border-radius: 5px;
        text-align: center;
        line-height: 1.2; /* Espaçamento mais curto igual ao original */
    }

    /* Títulos dos campos (ex: Nome, CPF) */
    .label-resultado {
        font-weight: 600;
        font-size: 1.1em;
        margin-bottom: 2px;
        display: block;
    }

    /* Dados dos campos (ex: ALISON BELFORT MOTA) */
    .dado-resultado {
        font-weight: 300;
        font-size: 1.0em;
        margin-bottom: 20px;
        display: block;
        color: #d1d1d1;
    }

    .badge-instituicao {
        background-color: #4cd964;
        color: #000;
        padding: 4px 12px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.85em;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho (Logo e Texto)
# Nota: Substitua o link abaixo pela URL da imagem do logo da FAFIBE se tiver
st.markdown("<div style='text-align: center;'><img src='https://www.educamaisbrasil.com.br/fafibe/campus' width='200'></div>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Portal de consulta Pública.</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.9em; color: #666;'>Este é um portal público de consulta para alunos da FAFIBE. Aqui você consulta toda a nossa base de concluintes, registrados em todos os níveis de ensino. Use-o para validar um diploma que esteja em suas mãos.</p>", unsafe_allow_html=True)

# 4. Campo de Entrada
cpf_digitado = st.text_input("Digite o CPF do aluno", placeholder="000.000.000-00")

# 5. Lógica de Busca e Exibição do Layout
try:
    df = pd.read_csv('dados.csv')
    
    if cpf_digitado:
        # Busca ignorando pontos e traços se necessário (opcional)
        resultado = df[df['CPF'] == cpf_digitado]
        
        if not resultado.empty:
            res = resultado.iloc[0]
            
            # O Bloco Escuro da sua imagem
           st.markdown(f"""
    <div class="resultado-box">
        <span class="badge-instituicao">FAFIBE – Faculdade de Filosofia, Ciências e Letras de Boa Esperança</span>
        <br><br><br>
        <span class="label-resultado">Nome</span>
        <span class="dado-resultado">{res['Nome']}</span>
        
        <span class="label-resultado">Número da Matrícula</span>
        <span class="dado-resultado">{res['Matricula']}</span>
        
        <span class="label-resultado">CPF</span>
        <span class="dado-resultado">{res['CPF']}</span>
        
        <span class="label-resultado">Data de nascimento</span>
        <span class="dado-resultado">{res['Data_Nascimento']}</span>
        
        <span class="label-resultado">Curso</span>
        <span class="dado-resultado">{res['Curso']}</span>
        
        <span class="label-resultado">Data de Ingresso</span>
        <span class="dado-resultado">{res['Data_Ingresso']}</span>
        
        <div style="background-color: #ffc107; color: black; display: inline-block; padding: 2px 10px; border-radius: 3px; font-weight: bold; font-size: 0.8em;">Curso superior</div>
    </div>
""", unsafe_allow_html=True)
        else:
            st.error("CPF não encontrado na base de dados da instituição.")
except Exception as e:
    st.error("Erro ao carregar banco de dados. Verifique o arquivo dados.csv.")

import streamlit as st
import pandas as pd

# 1. Configuração da Página
st.set_page_config(page_title="Portal de Consulta FAFIBE", layout="centered")

# 2. Estilização CSS Profissional
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    
    .main { background-color: #0e1117; }
    
    /* Centralizar o campo de busca e estilizar */
    .stTextInput > div > div > input {
        text-align: center;
        background-color: #262730;
        color: white;
        border: 1px solid #3d3d3d;
        height: 45px;
        border-radius: 8px;
    }

    /* Bloco de Resultado idêntico ao oficial */
    .resultado-box {
        background-color: #1e2436;
        color: white;
        padding: 40px 20px;
        border-radius: 4px;
        text-align: center;
        line-height: 1.1;
        margin-top: 20px;
    }

    .label-resultado {
        font-weight: 600;
        font-size: 1.1em;
        margin-bottom: 5px;
        display: block;
    }

    .dado-resultado {
        font-weight: 300;
        font-size: 1.0em;
        margin-bottom: 25px;
        display: block;
        color: #e0e0e0;
    }

    .badge-instituicao {
        background-color: #4cd964;
        color: #000;
        padding: 5px 15px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8em;
        text-transform: uppercase;
    }

    .badge-superior {
        background-color: #ffc107;
        color: black;
        display: inline-block;
        padding: 3px 12px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8em;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho com a Logo enviada
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        # Certifique-se de que a imagem no GitHub se chama logo_fafibe.png
        st.image("logo_fafibe.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center; color: #1565C0;'>FAFIBE</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; margin-top: -10px; font-weight: 400;'>Portal de consulta Pública.</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.85em; color: #888; padding: 0 20px;'>Este é um portal público de consulta para alunos da FAFIBE. Aqui você consulta toda a nossa base de concluintes. Use-o para validar um diploma que esteja em suas mãos.</p>", unsafe_allow_html=True)

# 4. Área de Busca
cpf_digitado = st.text_input("Digite o CPF do aluno", placeholder="Ex: 000.000.000-00")

# 5. Lógica de Exibição
if cpf_digitado:
    try:
        df = pd.read_csv('dados.csv')
        resultado = df[df['CPF'] == cpf_digitado]
        
        if not resultado.empty:
            res = resultado.iloc[0]
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
                    
                    <span class="label-resultado">Data de conclusão</span>
                    <span class="dado-resultado">{res['Data_Conclusao']}</span>
                    
                    <span class="label-resultado">Informações da Expedição do Diploma</span>
                    <span class="dado-resultado">{res['Status_Diploma']}</span>
                    
                    <div class="badge-superior">Curso superior</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Documento não localizado em nossa base de dados.")
    except Exception as e:
        st.error("Erro técnico ao acessar a base de dados.")

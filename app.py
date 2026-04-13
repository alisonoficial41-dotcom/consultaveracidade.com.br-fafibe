import streamlit as st
import pandas as pd

# 1. Configuração da Página
st.set_page_config(page_title="Portal de Consulta FAFIBE", layout="centered")

# 2. Estilização Visual (O segredo do layout escuro)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stTextInput > div > div > input { text-align: center; border-radius: 5px; }
    .resultado-box {
        background-color: #1e2436;
        color: white;
        padding: 40px;
        border-radius: 10px;
        text-align: center;
        line-height: 1.8;
        font-family: 'sans-serif';
    }
    .badge-instituicao {
        background-color: #4cd964;
        color: white;
        padding: 5px 15px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.8em;
    }
    .curso-superior {
        background-color: #ffc107;
        color: black;
        display: inline-block;
        padding: 2px 10px;
        border-radius: 3px;
        font-weight: bold;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho (Logo e Texto)
# Nota: Substitua o link abaixo pela URL da imagem do logo da FAFIBE se tiver
st.markdown("<div style='text-align: center;'><img src='https://via.placeholder.com/200x80?text=NOVA+FAFIBE' width='200'></div>", unsafe_allow_html=True)
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
                    <br><br>
                    <strong>Nome</strong><br>{res['Nome']}<br><br>
                    <strong>Número da Matrícula</strong><br>{res['Matricula']}<br><br>
                    <strong>CPF</strong><br>{res['CPF']}<br><br>
                    <strong>Data de nascimento</strong><br>{res['Data_Nascimento']}<br><br>
                    <strong>Curso</strong><br>{res['Curso']}<br><br>
                    <strong>Data de Ingresso</strong><br>{res['Data_Ingresso']}<br><br>
                    <strong>Data de conclusão</strong><br>{res['Data_Conclusao']}<br><br>
                    <strong>Informações da Expedição do Diploma</strong><br>{res['Status_Diploma']}<br><br>
                    <div class="curso-superior">Curso superior</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("CPF não encontrado na base de dados da instituição.")
except Exception as e:
    st.error("Erro ao carregar banco de dados. Verifique o arquivo dados.csv.")
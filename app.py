import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Omni-Solver: Nexus Estelar & IA",
    page_icon="🛸",
    layout="wide"
)

# Estilos CSS com forçagem total para a barra de chat
st.markdown("""
    <style>
    /* Fundo geral da aplicação */
    .stApp {
        background-color: #030008;
        color: #ffffff;
    }
    
    /* Estilo da Barra Lateral (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #080314;
        border-right: 1px solid rgba(168, 85, 247, 0.2);
    }

    /* Estilo uniforme para os botões na barra lateral */
    [data-testid="stSidebar"] .stButton > button {
        background: linear-gradient(135deg, #2e1065 0%, #3b0764 50%, #1e1b4b 100%) !important;
        color: #ffffff !important;
        border: 1px solid rgba(168, 85, 247, 0.5) !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), 0 0 10px rgba(147, 51, 234, 0.2) !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }

    /* Efeito ao passar o rato por cima dos botões */
    [data-testid="stSidebar"] .stButton > button:hover {
        background: linear-gradient(135deg, #3b0764 0%, #581c87 50%, #312e81 100%) !important;
        border-color: #c084fc !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6), 0 0 15px rgba(192, 132, 252, 0.4) !important;
    }

    /* Caixa de estado ativo com o fundo cósmico e letra branca */
    .ativo-cosmos {
        background: linear-gradient(135deg, #1e1b4b 0%, #311042 100%);
        border: 1px solid rgba(168, 85, 247, 0.4);
        padding: 12px;
        border-radius: 12px;
        color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
        margin-top: 10px;
    }

    /* --- FORÇAGEM ABSOLUTA PARA A BARRA DE CHAT INPUT (FUNDO DO UNIVERSO) --- */
    [data-testid="stChatInput"] {
        max-width: 730px !important;
        margin: 0 auto !important;
    }

    /* Anula qualquer fundo branco que o Streamlit force nos contentores internos */
    [data-testid="stChatInput"], 
    [data-testid="stChatInput"] > div, 
    [data-testid="stChatInput"] div[data-baseweb="base-input"],
    [data-testid="stChatInput"] textarea {
        background-color: transparent !important;
    }

    /* Aplica o gradiente cósmico no contentor principal da barra */
    [data-testid="stChatInput"] > div {
        background: linear-gradient(135deg, #060112 0%, #14072b 45%, #0b112c 80%, #03000a 100%) !important;
        border: 1px solid rgba(168, 85, 247, 0.6) !important;
        border-radius: 14px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7), 0 0 15px rgba(147, 51, 234, 0.35) !important;
    }

    /* Letras a branco puro na caixa de texto */
    [data-testid="stChatInput"] textarea {
        color: #ffffff !important;
        font-size: 15px !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    /* Texto de introdução (placeholder) mais claro */
    [data-testid="stChatInput"] textarea::placeholder {
        color: rgba(255, 255, 255, 0.7) !important;
        opacity: 1 !important;
    }

    /* Botão de envio da barra de chat */
    [data-testid="stChatInput"] button {
        background: rgba(168, 85, 247, 0.3) !important;
        border: 1px solid rgba(168, 85, 247, 0.5) !important;
        color: #ffffff !important;
        border-radius: 10px !important;
    }

    [data-testid="stChatInput"] button svg {
        fill: #ffffff !important;
    }

    [data-testid="stChatInput"] button:hover {
        background: rgba(168, 85, 247, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (CONTROLO DA NAVE) ---
with st.sidebar:
    st.markdown("### **Controlo da Nave**")
    st.markdown("<p style='font-size: 13px; color: #d8b4fe;'>Frequência de Raciocínio Ativa:</p>", unsafe_allow_html=True)
    
    if st.button("✨ Investigação Científica & IA", use_container_width=True):
        st.session_state['freq'] = "Investigação Científica & IA"
    if st.button("🤖 Robótica & Sistemas de Elite", use_container_width=True):
        st.session_state['freq'] = "Robótica & Sistemas de Elite"
    if st.button("🛸 Exploração Cósmica", use_container_width=True):
        st.session_state['freq'] = "Exploração Cósmica"
        
    freq_atual = st.session_state.get('freq', 'Investigação Científica & IA')
    st.markdown(f"""
        <div class="ativo-cosmos">
            <span style='font-size: 12px; color: #4ade80; font-weight: bold;'>Ativo:</span><br>
            <span style='font-size: 13px; color: #ffffff;'>✨ {freq_atual}</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### **Portal de Tripulante**")
    st.markdown("<p style='font-size: 13px; color: #d8b4fe;'>Desbloqueia energia ilimitada para a tua missão.</p>", unsafe_allow_html=True)
    
    if st.button("⭐ Subscrever Passe Estelar (2€/mês)", use_container_width=True):
        st.success("A redirecionar para o checkout seguro da Stripe...")

# --- CORPO PRINCIPAL ---
st.markdown("# Omni-Solver: Nexus Estelar & IA")
st.markdown("*✨ Explora a fronteira do conhecimento humano, robótica e inteligência profunda através do cosmos.*")
st.markdown("")

with st.chat_message("user", avatar="🪐"):
    st.write("Qual é o maior problema de todas as pessoas e empresas agora?")

with st.chat_message("assistant", avatar="🛸"):
    st.write("Processado com sucesso pelo Omni-Solver Engine. Recebi a tua mensagem: 'Qual é o maior problema de todas as pessoas e empresas agora?'.")

prompt = st.chat_input("Transmite a tua diretiva para o cosmos... 🛸")

if prompt:
    with st.chat_message("user", avatar="🪐"):
        st.write(prompt)
    with st.chat_message("assistant", avatar="🛸"):
        st.write(f"Processado com sucesso pelo Omni-Solver Engine. Recebi a tua mensagem: '{prompt}'.")
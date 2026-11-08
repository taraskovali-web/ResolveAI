import streamlit as st

# 1. Configuração da página
st.set_page_config(
    page_title="Omni-Solver: Nexus Estelar & IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Injeção de CSS para forçar a atmosfera cósmica e a estética roxa
st.markdown("""
    <style>
    /* Fundo geral universo (espaço profundo) */
    .stApp {
        background: radial-gradient(circle at 50% 20%, #110d29 0%, #05050d 100%) !important;
        color: #ffffff !important;
    }
    
    /* Barra Lateral Cósmica */
    section[data-testid="stSidebar"] {
        background-color: #0a0814 !important;
        border-right: 1px solid #1e1b4b !important;
    }
    
    /* Textos da Barra Lateral */
    section[data-testid="stSidebar"] h3 {
        color: #c084fc !important;
        font-size: 16px !important;
        font-weight: 700 !important;
    }
    section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span {
        color: #cbd5e1 !important;
    }
    
    /* Botões da Sidebar (Frequências de Raciocínio) */
    div[data-testid="stSidebar"] div.stButton > button {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%) !important;
        color: #e0e7ff !important;
        border: 1px solid #4338ca !important;
        border-radius: 8px !important;
        padding: 8px 14px !important;
        font-weight: 500 !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4) !important;
    }
    div[data-testid="stSidebar"] div.stButton > button:hover {
        background: linear-gradient(135deg, #312e81 0%, #4338ca 100%) !important;
        border-color: #6366f1 !important;
        color: #ffffff !important;
    }

    /* Caixa do Estado Ativo */
    .caixa-ativo {
        background: #1e1b4b !important;
        border: 1px solid #6366f1 !important;
        padding: 10px 14px !important;
        border-radius: 8px !important;
        font-size: 13px !important;
        color: #e0e7ff !important;
        margin-top: 10px !important;
        margin-bottom: 20px !important;
    }

    /* BOTÃO DO PASSE ESTELAR (ROXO VIBRANTE / STRIPE) */
    div[data-testid="stSidebar"] div.stLinkButton > a {
        background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%) !important;
        color: #ffffff !important;
        border: 1px solid #a855f7 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        text-align: center !important;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.5) !important;
    }
    div[data-testid="stSidebar"] div.stLinkButton > a:hover {
        background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%) !important;
        border-color: #c084fc !important;
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.7) !important;
    }

    /* Títulos do Painel Principal em Roxo Cósmico */
    h1 {
        color: #c084fc !important;
        font-weight: 800 !important;
    }
    
    /* Campo de Chat */
    .stChatInput input {
        color: #ffffff !important;
        background-color: #0f172a !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Gestão de Estado
if "frequencia_ativa" not in st.session_state:
    st.session_state.frequencia_ativa = "✨ Investigação Científica & IA"

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- BARRA LATERAL ---
with st.sidebar:
    st.markdown("### **Controlo da Nave**")
    st.markdown("<p style='font-size: 13px;'>Frequência de Raciocínio Ativa:</p>", unsafe_allow_html=True)
    
    # Botões de seleção de frequência
    if st.button("✨ Investigação Científica & IA", use_container_width=True):
        st.session_state.frequencia_ativa = "✨ Investigação Científica & IA"
    
    if st.button("🤖 Robótica & Sistemas de Elite", use_container_width=True):
        st.session_state.frequencia_ativa = "🤖 Robótica & Sistemas de Elite"
        
    if st.button("🌌 Exploração Cósmica", use_container_width=True):
        st.session_state.frequencia_ativa = "🌌 Exploração Cósmica"
        
    # Caixa do Ativo
    st.markdown(
        f"<div class='caixa-ativo'><b>Ativo:</b> {st.session_state.frequencia_ativa}</div>", 
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # --- PORTAL DE TRIPULANTE ---
    st.markdown("### **Portal de Tripulante**")
    st.markdown("<p style='font-size: 13px;'>Desbloqueia energia ilimitada para a tua missão.</p>", unsafe_allow_html=True)
    
    # Botão de subscrição Stripe com o teu link oficial
    st.link_button(
        "⭐ Subscrever Passe Estelar (2€/mês)", 
        "https://buy.stripe.com/cNidR9epr307gqneTFdZ600", 
        use_container_width=True
    )

# --- CONTEÚDO PRINCIPAL ---
st.markdown("# Omni-Solver: Nexus Estelar & IA")
st.markdown("✨ *Explora a fronteira do conhecimento humano, robótica e inteligência profunda através do cosmos.*")

st.markdown("---")

# Exibir histórico de chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caixa de chat principal
if prompt := st.chat_input("Transmite a tua diretiva para o cosmos..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    resposta = f"[{st.session_state.frequencia_ativa}] A processar a diretiva: '{prompt}' através da rede neural estelar..."
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)
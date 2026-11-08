import streamlit as st

# 1. Configuração da página
st.set_page_config(
    page_title="Omni-Solver: Nexus Estelar & IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilização visual exata baseada na tua referência
st.markdown("""
    <style>
    /* Fundo geral e da barra lateral */
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1f2937;
    }
    section[data-testid="stSidebar"] h3 {
        color: #f3f4f6 !important;
        font-size: 16px !important;
        margin-bottom: 0px !important;
    }
    section[data-testid="stSidebar"] p {
        color: #9ca3af !important;
    }
    
    /* Estilo dos botões da barra lateral (Frequências de Raciocínio) */
    div.stButton > button {
        background-color: #2e1065 !important;
        color: #ffffff !important;
        border: 1px solid #7c3aed !important;
        border-radius: 8px !important;
        font-weight: 500;
        text-align: left !important;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #3b0764 !important;
        border-color: #9333ea !important;
        color: #ffffff !important;
    }

    /* ESTILO DO BOTÃO DO PASSE ESTELAR (Stripe Link Button) */
    div.stLinkButton > a {
        background-color: #7c3aed !important;
        color: #ffffff !important;
        border: 1px solid #9333ea !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        text-align: center !important;
        box-shadow: 0px 4px 12px rgba(124, 58, 237, 0.4);
        transition: all 0.3s ease;
    }
    div.stLinkButton > a:hover {
        background-color: #6d28d9 !important;
        border-color: #a855f7 !important;
        color: #ffffff !important;
    }
    
    /* Caixa de chat contrastada e legível */
    .stChatInput input {
        color: #ffffff !important;
        background-color: #1a2234 !important;
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
    st.markdown("<p style='font-size: 13px; margin-bottom: 8px;'>Frequência de Raciocínio Ativa:</p>", unsafe_allow_html=True)
    
    # Botões de seleção de frequência
    if st.button("✨ Investigação Científica & IA", use_container_width=True):
        st.session_state.frequencia_ativa = "✨ Investigação Científica & IA"
    
    if st.button("🤖 Robótica & Sistemas de Elite", use_container_width=True):
        st.session_state.frequencia_ativa = "🤖 Robótica & Sistemas de Elite"
        
    if st.button("🌌 Exploração Cósmica", use_container_width=True):
        st.session_state.frequencia_ativa = "🌌 Exploração Cósmica"
        
    # Caixa de estado ativo
    st.markdown(
        f"<div style='background-color: #2e1065; border: 1px solid #7c3aed; padding: 10px; border-radius: 8px; font-size: 13px; margin-top: 12px; margin-bottom: 20px; color: #f3f4f6;'><b>Ativo:</b> {st.session_state.frequencia_ativa}</div>", 
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # --- PORTAL DE TRIPULANTE ---
    st.markdown("### **Portal de Tripulante**")
    st.markdown("<p style='font-size: 13px; margin-bottom: 12px;'>Desbloqueia energia ilimitada para a tua missão.</p>", unsafe_allow_html=True)
    
    # Botão de subscrição Stripe oficial com o teu link
    st.link_button(
        "⭐ Subscrever Passe Estelar (2€/mês)", 
        "https://buy.stripe.com/cNidR9epr307gqneTFdZ600", 
        use_container_width=True
    )

# --- CONTEÚDO PRINCIPAL ---
st.markdown("# Omni-Solver: Nexus Estelar & IA")
st.markdown("✨ Explora a fronteira do conhecimento humano, robótica e inteligência profunda através do cosmos.")

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
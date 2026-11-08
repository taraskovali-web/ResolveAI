import streamlit as st

# 1. Configuração da página
st.set_page_config(
    page_title="Omni-Solver: Nexus Estelar & IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilização visual (Tema Cosmic / Dark Theme & Ajustes de Visibilidade do Chat)
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1f2937;
    }
    /* Estilização do input de chat para garantir visibilidade perfeita no tema escuro */
    .stChatInput input {
        color: #ffffff !important;
        background-color: #1a2234 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Gestão de Estado para a Frequência de Raciocínio Ativa
if "frequencia_ativa" not in st.session_state:
    st.session_state.frequencia_ativa = "✨ Investigação Científica & IA"

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- BARRA LATERAL ---
with st.sidebar:
    st.markdown("### **Controlo da Nave**")
    st.markdown("<p style='font-size: 13px; color: #9ca3af;'>Frequência de Raciocínio Ativa:</p>", unsafe_allow_html=True)
    
    # Botões de seleção de frequência
    if st.button("✨ Investigação Científica & IA", use_container_width=True):
        st.session_state.frequencia_ativa = "✨ Investigação Científica & IA"
    
    if st.button("🤖 Robótica & Sistemas de Elite", use_container_width=True):
        st.session_state.frequencia_ativa = "🤖 Robótica & Sistemas de Elite"
        
    if st.button("🌌 Exploração Cósmica", use_container_width=True):
        st.session_state.frequencia_ativa = "🌌 Exploração Cósmica"
        
    st.markdown(f"<div style='background-color: #1f2937; padding: 8px; border-radius: 6px; font-size: 12px; margin-top: 10px; margin-bottom: 20px;'><b>Ativo:</b> {st.session_state.frequencia_ativa}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # --- PORTAL DE TRIPULANTE ---
    st.markdown("### **Portal de Tripulante**")
    st.markdown("<p style='font-size: 13px; color: #d8b4fe;'>Desbloqueia energia ilimitada para a tua missão.</p>", unsafe_allow_html=True)
    
    # Botão de subscrição Stripe oficial
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

# Caixa de chat principal alinhada com o requisito visual
if prompt := st.chat_input("Transmite a tua diretiva para o cosmos..."):
    # Adicionar mensagem do utilizador
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta baseada no modo ativo
    resposta = f"[{st.session_state.frequencia_ativa}] A processar a diretiva: '{prompt}' através da rede neural estelar..."
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)
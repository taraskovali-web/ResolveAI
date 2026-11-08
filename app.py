import streamlit as st
import google.generativeai as genai

# Configuração da página e layout espacial de elite
st.set_page_config(
    page_title="Omni-Solver 🌌 Nexus Cósmico", 
    page_icon="🌌", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização Temática Espacial com Título em Gradiente de Galáxia
st.markdown("""
    <style>
    /* Fundo Temático Espacial */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #1a0b2e 0%, #090a0f 60%, #030305 100%);
        color: #ffffff !important;
    }
    
    /* Forçar todo o texto geral e descrições a branco */
    p, span, label, div, .stMarkdown {
        color: #ffffff !important;
    }
    
    /* Painel Lateral com Efeito Glassmorphism */
    [data-testid="stSidebar"] {
        background: rgba(15, 12, 29, 0.85) !important;
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(138, 43, 226, 0.2);
    }
    
    /* Título com Gradiente Estilo Universo/Galáxia (Roxo -> Rosa Nebulosa -> Azul Estelar -> Ciano) */
    h1 {
        background: linear-gradient(90deg, #c084fc 0%, #e879f9 33%, #60a5fa 66%, #22d3ee 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 800 !important;
        letter-spacing: 1px;
    }
    
    h2, h3 {
        color: #c084fc !important;
    }
    
    /* Caixas de Mensagem Estilizadas */
    [data-testid="stChatMessage"] {
        background: rgba(22, 17, 43, 0.7);
        border: 1px solid rgba(147, 51, 234, 0.3);
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(8px);
        margin-bottom: 12px;
        color: #ffffff !important;
    }
    
    /* Caixa de Entrada Futurista */
    .stChatInputContainer {
        border-radius: 16px !important;
        border: 1px solid rgba(139, 92, 246, 0.5) !important;
        box-shadow: 0 0 15px rgba(139, 92, 246, 0.2);
    }
    
    /* Botão da Stripe com Brilho Néon */
    .stLinkButton > a {
        background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%) !important;
        color: #ffffff !important;
        border: none !important;
        box-shadow: 0 0 15px rgba(124, 58, 237, 0.4);
        transition: all 0.3s ease;
    }
    .stLinkButton > a:hover {
        box-shadow: 0 0 25px rgba(124, 58, 237, 0.8);
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho Principal Cósmico
st.title("Omni-Solver: Nexus Estelar & IA")
st.markdown("✨ *Explora a fronteira do conhecimento humano, robótica e inteligência profunda através do cosmos.*")

# Barra Lateral - Controlo de Missão
st.sidebar.markdown("### 🪐 Controlo da Nave")
modo_missao = st.sidebar.selectbox(
    "Frequência de Raciocínio",
    ["✨ Investigação Científica & IA", "🤖 Robótica & Sistemas de Elite", "🌌 Exploração Cósmica"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🛰️ Portal de Tripulante")
st.sidebar.write("Desbloqueia energia ilimitada para a tua missão.")
stripe_url = "https://buy.stripe.com/test_cNidR9epR307gqnETFdZ600"
st.sidebar.link_button("⭐ Subscrever Passe Estelar (2€/mês)", stripe_url)

# Chave de API
api_key = st.secrets.get("GEMINI_API_KEY", None)

if not api_key:
    st.warning("⚠️ Configura a tua `GEMINI_API_KEY` nos Secrets para ligar o núcleo online.")

# Histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    avatar = "👨‍🚀" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.write(message["content"])

# Input do Utilizador
user_prompt = st.chat_input("Transmite a tua diretiva para o cosmos... 🛸")

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user", avatar="👨‍🚀"):
        st.write(user_prompt)

    with st.chat_message("assistant", avatar="🤖"):
        response_text = ""
        
        if api_key:
            try:
                genai.configure(api_key=api_key)
                working_model = None
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        working_model = m.name
                        break
                
                if working_model:
                    model = genai.GenerativeModel(working_model)
                    res = model.generate_content(f"[{modo_missao}]\n{user_prompt}")
                    response_text = res.text
            except Exception:
                pass

        if not response_text:
            response_text = f"[{modo_missao}] Diretiva recebida no Nexus Cósmico: '{user_prompt}'. Sistema operacional a 100%."

        st.write(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
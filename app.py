import streamlit as st
from google import genai

# Configuração da página com tema espacial
st.set_page_config(
    page_title="Omni-Solver 🚀 Espaço IA", 
    page_icon="🌌", 
    layout="centered"
)

# Estilo visual personalizado (Tema Espacial / Dark Cosmic)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #111827 50%, #1f1035 100%);
        color: #f3f4f6;
    }
    .stSidebar {
        background-color: #0f172a;
    }
    h1 {
        color: #38bdf8;
        font-family: 'Helvetica Neue', sans-serif;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
    }
    /* Forçar texto branco e visível durante a digitação */
    .stChatInput textarea {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        background-color: #1e293b !important;
        caret-color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho Espacial
st.title("🚀 Omni-Solver: Central Espacial de IA")
st.markdown("🌌 *Navega pelas fronteiras do conhecimento com um assistente alimentado por inteligência artificial.*")

# Obter a chave de API de forma segura a partir dos Secrets do Streamlit
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    st.error("⚠️ Falta configurar a GEMINI_API_KEY nos Secrets do Streamlit Cloud.")
    st.stop()

# Inicializar o cliente do Google GenAI
client = genai.Client(api_key=api_key)

# Caixa de texto para o utilizador colocar a pergunta
user_prompt = st.chat_input("Qual é a tua missão ou dúvida hoje? 🛸")

if user_prompt:
    with st.chat_message("user", avatar="🌍"):
        st.write(user_prompt)
        
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("✨ A calcular trajetória cósmica..."):
            try:
                # Gerar resposta usando o modelo estável
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=user_prompt,
                )
                st.write(response.text)
            except Exception as e:
                # Fallback automático se houver pico de tráfego
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=user_prompt,
                    )
                    st.write(response.text)
                except Exception as err:
                    st.error(f"Ocorreu um erro na comunicação estelar: {err}")

# Barra lateral com temática e botão da Stripe
st.sidebar.markdown("### 🪐 Portal de Tripulante")
st.sidebar.write("Desbloqueia energia ilimitada e ferramentas avançadas no cosmos.")
st.sidebar.markdown("---")

# Link oficial do Stripe configurado
stripe_url = "https://buy.stripe.com/test_cNidR9epR307gqnETFdZ600"
st.sidebar.link_button("⭐ Subscrever Missão (2€/mês)", stripe_url)
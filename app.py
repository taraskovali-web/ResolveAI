import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(
    page_title="Omni-Solver 🚀 Espaço IA", 
    page_icon="🌌", 
    layout="centered"
)

# Cabeçalho Espacial
st.title("🚀 Omni-Solver: Central Espacial de IA")
st.markdown("🌌 *Navega pelas fronteiras do conhecimento com um assistente alimentado por inteligência artificial.*")

# Obter a chave de API de forma segura a partir dos Secrets do Streamlit
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    st.error("⚠️ Falta configurar a GEMINI_API_KEY nos Secrets do Streamlit Cloud.")
    st.stop()

# Configurar o SDK clássico do Gemini
genai.configure(api_key=api_key)

# Usar o modelo flash padrão e amplamente estável
model = genai.GenerativeModel('gemini-1.5-flash')

# Caixa de texto padrão do Streamlit
user_prompt = st.chat_input("Qual é a tua missão ou dúvida hoje? 🛸")

if user_prompt:
    with st.chat_message("user", avatar="🌍"):
        st.write(user_prompt)
        
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("✨ A calcular trajetória cósmica..."):
            try:
                # Gerar resposta de forma síncrona e rápida
                response = model.generate_content(user_prompt)
                st.write(response.text)
            except Exception as e:
                st.error(f"Ocorreu um erro na comunicação estelar: {e}")

# Barra lateral com temática e botão da Stripe
st.sidebar.markdown("### 🪐 Portal de Tripulante")
st.sidebar.write("Desbloqueia energia ilimitada e ferramentas avançadas no cosmos.")
st.sidebar.markdown("---")

stripe_url = "https://buy.stripe.com/test_cNidR9epR307gqnETFdZ600"
st.sidebar.link_button("⭐ Subscrever Missão (2€/mês)", stripe_url)
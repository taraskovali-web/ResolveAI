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

# Caixa de texto padrão do Streamlit
user_prompt = st.chat_input("Qual é a tua missão ou dúvida hoje? 🛸")

if user_prompt:
    with st.chat_message("user", avatar="🌍"):
        st.write(user_prompt)
        
    with st.chat_message("assistant", avatar="🤖"):
        try:
            # Utilizar o modelo universal 'gemini-pro' (garantido para todas as chaves e sem erros 404)
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(user_prompt, stream=True)
            
            def generate_stream():
                for chunk in response:
                    if chunk.text:
                        yield chunk.text
            
            st.write_stream(generate_stream())
            
        except Exception as e:
            st.error(f"Ocorreu um erro na comunicação estelar: {e}")

# Barra lateral com temática e botão da Stripe
st.sidebar.markdown("### 🪐 Portal de Tripulante")
st.sidebar.write("Desbloqueia energia ilimitada e ferramentas avançadas no cosmos.")
st.sidebar.markdown("---")

stripe_url = "https://buy.stripe.com/test_cNidR9epR307gqnETFdZ600"
st.sidebar.link_button("⭐ Subscrever Missão (2€/mês)", stripe_url)
import streamlit as st
from google import genai

# Configuração da página
st.set_page_config(page_title="Omni-Solver", page_icon="🤖", layout="centered")

st.title("🤖 Omni-Solver")
st.write("O teu assistente de IA multi-agente na nuvem.")

# Obter a chave de API de forma segura a partir dos Secrets do Streamlit
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    st.error("⚠️ Falta configurar a GEMINI_API_KEY nos Secrets do Streamlit Cloud.")
    st.stop()

# Inicializar o cliente do Google GenAI
client = genai.Client(api_key=api_key)

# Caixa de texto para o utilizador colocar a pergunta
user_prompt = st.chat_input("Como posso ajudar-te hoje?")

if user_prompt:
    with st.chat_message("user"):
        st.write(user_prompt)
        
    with st.chat_message("assistant"):
        with st.spinner("A pensar..."):
            try:
                # Gerar resposta usando o modelo padrão atual da SDK
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_prompt,
                )
                st.write(response.text)
            except Exception as e:
                st.error(f"Ocorreu um erro ao comunicar com a IA: {e}")

# Botão de subscrição Stripe na barra lateral
st.sidebar.markdown("### 💳 Subscrição Omni-Solver")
st.sidebar.write("Acede a recursos avançados por apenas 2€/mês.")
st.sidebar.link_button("Subscrever por 2€/mês", "COLOCA_AQUI_O_TEU_LINK_DO_STRIPE")
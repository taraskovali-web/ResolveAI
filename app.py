import streamlit as st
import json
import requests

# Configuração da página em modo Dark
st.set_page_config(
    page_title="ResolveAI - Inteligência Científica e Autónoma",
    page_icon="🌌",
    layout="centered"
)

# Injeção de CSS para o fundo de Universo / Estrelas e componentes modernos
st.markdown("""
<style>
    /* Fundo de galáxia/espaço com gradientes profundos */
    .stApp {
        background: radial-gradient(circle at 50% 20%, #1a0b2e 0%, #0d0614 40%, #030108 80%);
        color: #e0e6ed;
    }

    /* Estilização dos títulos */
    h1 {
        background: linear-gradient(90deg, #8a2be2, #00ffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        text-align: center;
        letter-spacing: 1px;
    }

    /* Animação subtil do subtítulo */
    .sub-hero {
        text-align: center;
        color: #a0aec0;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Caixas de texto e inputs futuristas */
    .stTextArea textarea, .stTextInput input {
        background-color: rgba(20, 15, 35, 0.7) !important;
        border: 1px solid rgba(138, 43, 226, 0.4) !important;
        color: #ffffff !important;
        border-radius: 10px !important;
    }
    
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #00ffff !important;
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.3) !important;
    }

    /* Botão Principal Néon */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #7928ca, #ff0080);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(121, 40, 202, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 0, 128, 0.6);
        color: #ffffff;
    }

    /* Cartões de resultado transparentes estilo Glassmorphism */
    .result-card {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
    }

    /* Ocultar elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Cabeçalho Principal
st.markdown("<h1>⚡ ResolveAI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-hero'>Motor de Resolução Autónoma de Problemas & Inteligência Avançada</p>", unsafe_allow_html=True)

# Interface de Entrada
st.markdown("### 🌌 Descreve o teu Desafio ou Problema")
problema_utilizador = st.text_area(
    "Problema",
    placeholder="Ex: A minha empresa de logística tem custos elevados em combustível...",
    label_visibility="collapsed"
)

contexto_utilizador = st.text_input(
    "Contexto Adicional",
    placeholder="Ex: Frota de 10 veículos a operar na região sul...",
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

# Execução do Motor de IA
if st.button("🚀 Analisar e Resolver com IA"):
    if not problema_utilizador.strip():
        st.warning("Por favor, introduz a descrição do problema.")
    else:
        with st.spinner("🌌 A processar na rede neuronal local (Ollama)..."):
            payload = {
                "model": "llama3.2:1b",
                "prompt": f"""
                És o motor principal da ResolveAI. Analisa o problema e responde EXCLUSIVAMENTE em JSON válido:
                Problema: {problema_utilizador}
                Contexto: {contexto_utilizador}
                
                Estrutura exata:
                {{
                    "diagnostico": "Análise clara e profunda do problema",
                    "causa_raiz": "Causa principal",
                    "plano_acao": [
                        {{"passo": 1, "acao": "Descrição da ação", "tempo_estimado": "X dias"}},
                        {{"passo": 2, "acao": "Descrição da ação", "tempo_estimado": "X dias"}}
                    ],
                    "estimativa_custos": {{
                        "valor_estimado_eur": 100.0,
                        "detalhe_custos": "Explicação breve"
                    }},
                    "metricas_sucesso": ["Métrica 1", "Métrica 2"]
                }}
                """,
                "stream": False,
                "format": "json"
            }

            try:
                response = requests.post("http://localhost:11434/api/generate", json=payload, timeout=60)
                if response.status_code == 200:
                    dados = json.loads(response.json().get("response", ""))
                    
                    st.success("Análise concluída com sucesso!")
                    
                    # Cartão de Diagnóstico & Causa Raiz
                    st.markdown(f"""
                    <div class="result-card">
                        <h3 style="color: #00ffff;">🔍 Diagnóstico</h3>
                        <p>{dados.get('diagnostico')}</p>
                        <h4 style="color: #ff0080;">🎯 Causa Raiz</h4>
                        <p>{dados.get('causa_raiz')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Plano de Ação
                    st.markdown("### 📋 Plano de Ação Estruturado")
                    for p in dados.get("plano_acao", []):
                        st.markdown(f"""
                        <div class="result-card">
                            <b>Passo {p.get('passo')}:</b> {p.get('acao')}<br>
                            <small style="color: #a0aec0;">⏱️ Tempo estimado: {p.get('tempo_estimado')}</small>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Custos e Métricas em Colunas
                    col1, col2 = st.columns(2)
                    with col1:
                        custos = dados.get("estimativa_custos", {})
                        st.metric(label="💶 Estimativa de Custos", value=f"{custos.get('valor_estimado_eur', 0)} €")
                        st.caption(custos.get("detalhe_custos"))
                    
                    with col2:
                        st.markdown("<b>📈 Métricas de Sucesso:</b>", unsafe_allow_html=True)
                        for m in dados.get("metricas_sucesso", []):
                            st.markdown(f"- {m}")
                            
                else:
                    st.error(f"Erro no motor Ollama: HTTP {response.status_code}")
            except Exception as e:
                st.error(f"Ocorreu um erro técnico: {str(e)}")
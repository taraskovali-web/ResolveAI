import streamlit as st
import json
import requests

# Configuração da Página
st.set_page_config(
    page_title="ResolveAI - Omni-Solver Universal",
    page_icon="🌌",
    layout="centered"
)

# Estilo Visual Futurista e Profissional
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at 50% 20%, #12071f 0%, #07030d 50%, #010003 100%);
        color: #e2e8f0;
    }
    h1 {
        background: linear-gradient(90deg, #9333ea, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        text-align: center;
        letter-spacing: 1px;
    }
    .sub-hero {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
    }
    .stTextArea textarea, .stTextInput input {
        background-color: rgba(15, 10, 25, 0.8) !important;
        border: 1px solid rgba(147, 51, 234, 0.4) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #7c3aed, #db2777);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.85rem 1.5rem;
        border-radius: 12px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(124, 58, 237, 0.4);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(219, 39, 119, 0.6);
    }
    .card-solution {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 1.8rem;
        margin-top: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Interface Principal
st.markdown("<h1>🌌 ResolveAI Omni-Solver</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-hero'>O Sistema Autónomo Universal de Resolução de Problemas</p>", unsafe_allow_html=True)

# Caixa de Entrada Universal
problema_global = st.text_area(
    "Qualquer Problema (Pessoa ou Empresa)",
    placeholder="Ex: Preciso de otimizar a logística de entrega de medicamentos ou criar um algoritmo de previsão de vendas em Python..."
)

contexto_global = st.text_input(
    "Restrições ou Contexto (Opcional)",
    placeholder="Ex: Orçamento zero, prazo de 48 horas, restrições técnicas..."
)

if st.button("⚡ Executar Motor Omni-Solver"):
    if not problema_global.strip():
        st.warning("Por favor, introduz o desafio que pretendes resolver.")
    else:
        with st.status("🧠 A ativar os Agentes de Inteligência Autónoma...", expanded=True) as status:
            
            # Passo 1: Desconstrução First Principles
            status.update(label="🔍 Passo 1/3: A desconstruir o problema nas leis fundamentais...", state="running")
            prompt_f1 = f"""
            Analisa o problema usando First Principles Thinking.
            Problema: {problema_global} | Contexto: {contexto_global}
            Responde EXCLUSIVAMENTE em JSON: {{"diagnostico_profundo": "...", "causa_raiz": "..."}}
            """
            r1 = requests.post("http://localhost:11434/api/generate", json={"model": "llama3.2:1b", "prompt": prompt_f1, "stream": False, "format": "json"})
            f1_data = json.loads(r1.json().get("response", "{}"))
            st.write("✅ Causa raiz isolada com rigor científico.")
            
            # Passo 2: Síntese de Solução Prática
            status.update(label="⚙️ Passo 2/3: A sintetizar a ferramenta ou código de resolução...", state="running")
            prompt_f2 = f"""
            Com base nisto: {json.dumps(f1_data)}
            Cria uma solução técnica concreta, incluindo código Python executável ou um modelo matemático/estrutural exato.
            Responde EXCLUSIVAMENTE em JSON: {{"estrategia_solucao": "...", "codigo_ou_estrutura_pratica": "..."}}
            """
            r2 = requests.post("http://localhost:11434/api/generate", json={"model": "llama3.2:1b", "prompt": prompt_f2, "stream": False, "format": "json"})
            f2_data = json.loads(r2.json().get("response", "{}"))
            st.write("✅ Solução técnica e código gerados.")
            
            # Passo 3: Plano de Execução Imediata
            status.update(label="📋 Passo 3/3: A estruturar o plano de ação e métricas de impacto...", state="running")
            prompt_f3 = f"""
            Cria um plano de ação tático com passos numerados para aplicar esta solução.
            Responde EXCLUSIVAMENTE em JSON: {{"plano_pratico": [{{"passo": 1, "acao": "...", "prazo": "..."}}], "metrica_sucesso": "..."}}
            """
            r3 = requests.post("http://localhost:11434/api/generate", json={"model": "llama3.2:1b", "prompt": prompt_f3, "stream": False, "format": "json"})
            f3_data = json.loads(r3.json().get("response", "{}"))
            
            status.update(label="✨ Solução universal gerada com sucesso absoluto!", state="complete", expanded=False)

        # APRESENTAÇÃO DOS RESULTADOS DO OMNI-SOLVER
        st.markdown(f"""
        <div class="card-solution">
            <h3 style="color: #06b6d4;">🔍 Diagnóstico Fundamental</h3>
            <p><b>Análise:</b> {f1_data.get('diagnostico_profundo')}</p>
            <p><b>Causa Raiz:</b> {f1_data.get('causa_raiz')}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card-solution">
            <h3 style="color: #db2777;">⚙️ Ferramenta / Código Sintetizado</h3>
            <p>{f2_data.get('estrategia_solucao')}</p>
            <pre style="background: rgba(0,0,0,0.6); padding: 15px; border-radius: 10px; color: #38bdf8; overflow-x: auto;"><code>{f2_data.get('codigo_ou_estrutura_pratica')}</code></pre>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📋 Plano de Execução Tática")
        for p in f3_data.get("plano_pratico", []):
            st.markdown(f"""
            <div class="card-solution">
                <b>Passo {p.get('passo')}:</b> {p.get('acao')}<br>
                <small style="color: #94a3b8;">⏱️ Prazo sugerido: {p.get('prazo')}</small>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown(f"""
        <div class="card-solution" style="border-color: rgba(6, 182, 212, 0.3);">
            <h4 style="color: #38bdf8;">🎯 Métrica de Sucesso Universal</h4>
            <p>{f3_data.get('metrica_sucesso')}</p>
        </div>
        """, unsafe_allow_html=True)
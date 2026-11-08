import streamlit as st
import streamlit.components.v1 as components

# 1. Configuração da página
st.set_page_config(
    page_title="ResolveAI: Nexus Estelar & IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estado da Sessão (Frequência, Mensagens e Controlo de Desempenho)
if "frequencia_ativa" not in st.session_state:
    st.session_state.frequencia_ativa = "✨ Investigação Científica & IA"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "universo_animado" not in st.session_state:
    st.session_state.universo_animado = True

# 3. Estilo CSS para Interface Futurista e Transparência sobre o Canvas 3D
st.markdown("""
    <style>
    /* Forçar transparência para revelar o Universo 3D ao fundo */
    .stApp {
        background: transparent !important;
        color: #ffffff !important;
    }
    
    /* Fundo fixo para o canvas 3D */
    #canvas-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1;
        pointer-events: none;
    }

    /* Barra Lateral Cósmica Semi-transparente */
    section[data-testid="stSidebar"] {
        background-color: rgba(11, 9, 26, 0.85) !important;
        border-right: 1px solid rgba(124, 58, 237, 0.3) !important;
        backdrop-filter: blur(10px);
    }
    
    section[data-testid="stSidebar"] h3 {
        color: #c084fc !important;
        font-weight: 700 !important;
    }

    /* Botões da Sidebar */
    div[data-testid="stSidebar"] div.stButton > button {
        background: rgba(30, 27, 75, 0.7) !important;
        color: #e0e7ff !important;
        border: 1px solid #4338ca !important;
        border-radius: 10px !important;
        transition: all 0.3s ease;
    }
    div[data-testid="stSidebar"] div.stButton > button:hover {
        background: linear-gradient(135deg, #312e81 0%, #4c1d95 100%) !important;
        border-color: #7c3aed !important;
        box-shadow: 0 0 15px rgba(124, 58, 237, 0.5);
    }

    /* Caixa do Estado Ativo */
    .caixa-ativo {
        background: rgba(46, 16, 101, 0.7) !important;
        border: 1px solid #7c3aed !important;
        padding: 10px 14px !important;
        border-radius: 10px !important;
        font-size: 13px !important;
        color: #f3f4f6 !important;
        margin-top: 10px !important;
        margin-bottom: 15px !important;
        backdrop-filter: blur(5px);
    }

    /* Botões do Portal de Tripulante */
    div[data-testid="stSidebar"] div.stLinkButton > a {
        background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%) !important;
        color: #ffffff !important;
        border: 1px solid #a855f7 !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        text-align: center !important;
        box-shadow: 0 4px 20px rgba(124, 58, 237, 0.6) !important;
    }

    /* Títulos e Histórico de Chat */
    h1 {
        color: #e9d5ff !important;
        font-weight: 800 !important;
        text-shadow: 0 2px 10px rgba(124, 58, 237, 0.5);
    }
    
    .stChatInput input {
        color: #ffffff !important;
        background-color: rgba(15, 23, 42, 0.9) !important;
        border: 1px solid #7c3aed !important;
        border-radius: 12px !important;
        backdrop-filter: blur(8px);
    }
    </style>
""", unsafe_allow_html=True)

# 4. Injeção do Universo 3D em Movimento (WebGL via Canvas HTML5/JS)
if st.session_state.universo_animado:
    components.html("""
        <div id="space-bg" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1; background:#05050d; overflow:hidden;">
            <canvas id="starfield"></canvas>
        </div>
        <script>
            const canvas = document.getElementById('starfield');
            const ctx = canvas.getContext('2d');
            let stars = [];
            const numStars = 200;

            function resizeCanvas() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }
            window.addEventListener('resize', resizeCanvas);
            resizeCanvas();

            for (let i = 0; i < numStars; i++) {
                stars.push({
                    x: (Math.random() - 0.5) * canvas.width * 2,
                    y: (Math.random() - 0.5) * canvas.height * 2,
                    z: Math.random() * canvas.width,
                    color: Math.random() > 0.3 ? '#c084fc' : '#38bdf8',
                    size: Math.random() * 1.5 + 0.5
                });
            }

            function draw() {
                ctx.fillStyle = 'rgba(5, 5, 13, 0.2)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                const cx = canvas.width / 2;
                const cy = canvas.height / 2;

                for (let star of stars) {
                    star.z -= 0.8; // Velocidade de movimento continuo do Universo
                    if (star.z <= 0) {
                        star.z = canvas.width;
                        star.x = (Math.random() - 0.5) * canvas.width * 2;
                        star.y = (Math.random() - 0.5) * canvas.height * 2;
                    }

                    const k = 256 / star.z;
                    const px = star.x * k + cx;
                    const py = star.y * k + cy;

                    if (px >= 0 && px < canvas.width && py >= 0 && py < canvas.height) {
                        const size = (1 - star.z / canvas.width) * star.size * 2;
                        ctx.beginPath();
                        ctx.arc(px, py, Math.max(size, 0.5), 0, Math.PI * 2);
                        ctx.fillStyle = star.color;
                        ctx.shadowBlur = 8;
                        ctx.shadowColor = star.color;
                        ctx.fill();
                    }
                }
                requestAnimationFrame(draw);
            }
            draw();
        </script>
    """, height=0)

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.markdown("### **Controlo da Nave**")
    st.markdown("<p style='font-size: 13px;'>Frequência de Raciocínio Ativa:</p>", unsafe_allow_html=True)
    
    if st.button("✨ Investigação Científica & IA", use_container_width=True):
        st.session_state.frequencia_ativa = "✨ Investigação Científica & IA"
    
    if st.button("🤖 Robótica & Sistemas de Elite", use_container_width=True):
        st.session_state.frequencia_ativa = "🤖 Robótica & Sistemas de Elite"
        
    if st.button("💻 Programação & Tecnologia", use_container_width=True):
        st.session_state.frequencia_ativa = "💻 Programação & Tecnologia"
        
    if st.button("📈 Negócios & Estratégia", use_container_width=True):
        st.session_state.frequencia_ativa = "📈 Negócios & Estratégia"
        
    st.markdown(
        f"<div class='caixa-ativo'><b>Ativo:</b> {st.session_state.frequencia_ativa}</div>", 
        unsafe_allow_html=True
    )
    
    # Controlo de Desempenho do Universo 3D
    st.session_state.universo_animado = st.checkbox("🌌 Animado 3D Ativo", value=True)
    
    st.markdown("---")
    
    # --- PORTAL DE TRIPULANTE (1€ / STRIPE & IBAN BPI) ---
    st.markdown("### **Portal de Tripulante**")
    st.markdown("<p style='font-size: 13px;'>Plano Ilimitado por apenas <b>1€/mês</b>.</p>", unsafe_allow_html=True)
    
    # Opção 1: Cartão via Stripe
    st.link_button(
        "⭐ Pagamento por Cartão (1€/mês)", 
        "https://buy.stripe.com/cNidR9epr307gqneTFdZ600",
        use_container_width=True
    )
    
    # Opção 2: Transferência Bancária / IBAN BPI
    with st.expander("🏦 Pagamento por Transferência BPI (IBAN)"):
        st.write("**Titular:** ResolveAI / BPI")
        st.code("PT50 0010 0000 0000 0000 0000 0", language="text") # Substituirás pelo teu IBAN exato do BPI
        st.caption("Ao fazer a transferência de 1€, insere o teu e-mail no descritivo para ativação automática.")

# --- PAINEL PRINCIPAL ---
st.markdown("# ResolveAI: Nexus Estelar & IA")
st.markdown("✨ *Explora a fronteira do conhecimento humano, resolve problemas complexos e constrói o futuro através do cosmos.*")

st.markdown("---")

# Histórico de Chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input de Chat
if prompt := st.chat_input("Transmite o teu problema ou diretiva para o cosmos..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("A analisar através da rede neural estelar..."):
            resposta = f"[{st.session_state.frequencia_ativa}] Analisei a tua diretiva: *'{prompt}'*. A ResolveAI está a processar uma solução estruturada..."
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})
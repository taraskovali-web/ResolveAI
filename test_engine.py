import json
import requests

class ResolveAIEngine:
    def __init__(self, model_name="llama3.2:1b", ollama_url="http://localhost:11434/api/generate"):
        self.model_name = model_name
        self.ollama_url = ollama_url

    def analyze_problem(self, problem_description, user_context=""):
        system_prompt = """
        És o motor principal da ResolveAI. A tua missão é analisar o problema do utilizador 
        e fornecer um plano de ação prático, rigoroso e quantificável.
        
        DEVES responder EXCLUSIVAMENTE em formato JSON válido com a seguinte estrutura:
        {
            "diagnostico": "Análise clara do problema",
            "causa_raiz": "Qual é a causa principal",
            "plano_acao": [
                {"passo": 1, "acao": "Descrição da ação", "tempo_estimado": "X horas/dias"},
                {"passo": 2, "acao": "Descrição da ação", "tempo_estimado": "X horas/dias"}
            ],
            "estimativa_custos": {
                "valor_estimado_eur": 0.0,
                "detalhe_custos": "Explicação dos custos esperados"
            },
            "metricas_sucesso": ["Como medir se o problema foi resolvido"]
        }
        """

        user_prompt = f"Problema do Utilizador: {problem_description}\nContexto Adicional: {user_context}"

        payload = {
            "model": self.model_name,
            "prompt": f"{system_prompt}\n\n{user_prompt}",
            "stream": False,
            "format": "json"
        }

        try:
            print("A enviar pedido para o Ollama (aguarda alguns segundos)...")
            response = requests.post(self.ollama_url, json=payload, timeout=60)
            if response.status_code == 200:
                raw_text = response.json().get("response", "")
                parsed_json = json.loads(raw_text)
                return {"status": "success", "data": parsed_json}
            else:
                return {"status": "error", "message": f"Erro do Ollama: HTTP {response.status_code}"}
        except Exception as e:
            return {"status": "error", "message": f"Erro na execução da análise: {str(e)}"}

if __name__ == "__main__":
    engine = ResolveAIEngine()
    resultado = engine.analyze_problem(
        problem_description="Tenho uma pequena loja online e estou a perder clientes no momento de pagar.",
        user_context="Utilizo WooCommerce e Stripe."
    )
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
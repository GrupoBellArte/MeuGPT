from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Substitua pela sua chave da API da OpenAI
openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get("prompt", "")

    # Uso correto da nova versão da API OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Certifique-se de que você tem acesso ao GPT-4
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": prompt}
        ]
    )

    return jsonify({"response": response.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import requests
import joblib
import numpy as np

app = Flask(__name__)

# Carregar os modelos
modelo_regressao = joblib.load('modelo_regressao.pkl')  # Modelo de regressão linear
modelo_classificacao = joblib.load('modelo_cluster.pkl')  # Modelo KMeans

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultar', methods=['POST'])
def consultar():
    cep = request.form['cep']
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    # Verificar se a API respondeu corretamente
    if resposta.status_code != 200 or "erro" in resposta.json():
        return render_template('index.html', erro="CEP inválido. Tente novamente.")
    
    endereco = resposta.json()

    # Printando para diagnóstico
    print(f"Dados do CEP {cep}: {endereco}")

    # Ajustar os dados para o modelo
    try:
        # Para KMeans: 3 features
        ibge = endereco.get('ibge', 0)
        gia = endereco.get('gia', 0)
        ddd = endereco.get('ddd', 0)

        # Garantir que os dados são do tipo float (caso não sejam, colocar valor 0)
        dados_ml_kmeans = [
            float(ibge) if isinstance(ibge, (int, float)) else 0,
            float(gia) if isinstance(gia, (int, float)) else 0,
            float(ddd) if isinstance(ddd, (int, float)) else 0
        ]

        if len(dados_ml_kmeans) != modelo_classificacao.n_features_in_:
            raise ValueError(f"O modelo KMeans espera {modelo_classificacao.n_features_in_} features, mas recebeu {len(dados_ml_kmeans)}.")
        
        # Para Regressão Linear: 1 feature
        dados_ml_regressao = [float(endereco.get('ddd', 0))]

        if len(dados_ml_regressao) != modelo_regressao.n_features_in_:
            raise ValueError(f"O modelo de regressão espera {modelo_regressao.n_features_in_} features, mas recebeu {len(dados_ml_regressao)}.")
    
    except ValueError as e:
        return render_template('index.html', erro=f"Erro nos dados para o modelo: {e}")
    except KeyError:
        return render_template('index.html', erro="Algum dado necessário não está presente no CEP informado.")

    # Previsões
    previsao_regressao = modelo_regressao.predict([dados_ml_regressao])[0]
    previsao_classificacao = modelo_classificacao.predict([dados_ml_kmeans])[0]

    # Printar as previsões para diagnóstico
    print(f"Previsão de Regressão: {previsao_regressao}")
    print(f"Previsão de Classificação: {previsao_classificacao}")

    # Classificação de acordo com o modelo KMeans (alterar para o seu critério)
    cls = 'Baixa' if previsao_classificacao == 1 else 'Alta'

    # Formatando a previsão de regressão para exibição, se necessário
    previsao_regressao_formatada = round(previsao_regressao, 2)  # Limita a 2 casas decimais

    # Exemplo de como a previsão de CO2 pode ser formatada ou analisada, dependendo da lógica do modelo
    previsao_co2 = previsao_regressao_formatada  # A previsão de CO2 pode ser baseada na regressão ou classificação

    # Classificação de emissões baseada na previsão de CO2 (alterar conforme o critério)
    emissao_class = "Alta" if previsao_co2 > 1000 else "Baixa"

    return render_template(
        'resultado.html',
        endereco=endereco,
        reg=previsao_regressao_formatada,  # Passando a previsão formatada para o template
        cls=cls,
        co2=previsao_co2,  # Exibindo a previsão de CO2
        emissao_class=emissao_class  # Exibindo a classificação de emissões
    )

if __name__ == '__main__':
    app.run(debug=True)

# IA-GS

Consulta de CEP e Previsões de Emissão de CO2
Este é um projeto desenvolvido utilizando Flask para consultar informações sobre um CEP e realizar previsões sobre a emissão de CO2 com base em modelos de regressão linear e classificação KMeans. O objetivo do aplicativo é fornecer uma previsão do impacto ambiental de uma localidade com base no código de área (DDD) do CEP informado, ajudando na conscientização sobre emissões de gases de efeito estufa.

Funcionalidades
Consulta de CEP: O usuário informa um CEP, e o sistema busca os dados relacionados ao endereço (logradouro, bairro, cidade, etc.) utilizando a API ViaCEP.
Previsões de Emissão de CO2: Com base nos dados do CEP, o sistema faz duas previsões:
Previsão de Emissão de CO2: Um valor estimado em quilogramas por ano, calculado através de um modelo de regressão linear.
Classificação de Emissão de CO2: O modelo classifica a localidade como de Baixa ou Alta emissão de CO2, com base em um modelo KMeans de clusterização.
Tecnologias Utilizadas
Flask: Framework web utilizado para criar a aplicação.
Jinja2: Sistema de templates utilizado pelo Flask para renderizar HTML com dados dinâmicos.
Requests: Biblioteca para fazer requisições HTTP para a API ViaCEP.
Joblib: Biblioteca para carregar e usar os modelos de machine learning (regressão linear e KMeans).
Tailwind CSS: Framework CSS para um design responsivo e moderno da interface do usuário.
Como Funciona
1. Fluxo de Dados
O usuário entra na página inicial e insere um CEP.
O sistema envia uma requisição HTTP para a API ViaCEP para obter os dados de endereço relacionados ao CEP informado.
Se o CEP for válido, os dados de endereço são exibidos na página.
Com os dados do CEP (incluindo o código de área DDD, IBGE e GIA), o sistema faz duas previsões:
A previsão de emissão de CO2 é calculada usando um modelo de regressão linear, que estima a quantidade de CO2 emitido na localidade com base no código de área.
A classificação de emissão de CO2 é feita com o modelo KMeans, que classifica a localidade como tendo emissão baixa ou alta com base nos dados fornecidos.
As previsões são então apresentadas ao usuário, juntamente com uma explicação sobre o que significam os resultados.
2. Modelos de Machine Learning
O sistema utiliza dois modelos de machine learning para realizar as previsões:

Modelo de Regressão Linear: Esse modelo é treinado para prever a emissão de CO2 com base nas características do endereço.
Modelo KMeans: Um modelo de clusterização que classifica as localidades em dois grupos: baixa emissão de CO2 e alta emissão de CO2. Esse modelo utiliza as variáveis relacionadas ao código de área (DDD, IBGE, GIA) para determinar em qual grupo a localidade se encaixa.
3. Fluxo de Operação
O usuário insere o CEP na página inicial.
O Flask faz uma requisição à API ViaCEP para obter os dados do endereço.
O sistema utiliza os dados obtidos (como DDD, IBGE, e GIA) como entrada para os modelos de machine learning.
As previsões são feitas com base no modelo de regressão linear e no modelo KMeans.
As previsões são apresentadas ao usuário, junto com uma explicação sobre o significado de cada valor.
Como Rodar o Projeto
Pré-requisitos
Python 3.x instalado na sua máquina.

Bibliotecas necessárias: Para instalar as dependências do projeto, execute:

bash
Copiar código
pip install -r requirements.txt
As bibliotecas incluem:

Flask
Requests
Joblib
NumPy
Tailwind CSS (para o front-end)
Rodando o Projeto
Clone o repositório ou baixe os arquivos para sua máquina.

No terminal, navegue até a pasta do projeto.

Execute o seguinte comando para rodar o servidor Flask:

bash
Copiar código
python app.py
Abra o navegador e acesse http://127.0.0.1:5000/ para visualizar a página inicial.

Informe o CEP e veja as previsões geradas para a localidade.

Explicação das Previsões
Previsão de Emissão de CO2
A previsão de emissão de CO2 é calculada com base nas características do código de área (DDD) e outras variáveis associadas à localidade. O modelo de regressão linear estima quanto CO2 é emitido por ano, ajudando a entender o impacto ambiental de uma região específica.

Classificação de Emissão de CO2
A classificação de emissão de CO2 ("Baixa" ou "Alta") é determinada com o modelo de KMeans. A localidade é classificada com base em clusters de emissão, o que ajuda a identificar o nível de impacto ambiental.

Baixa: Indica que a localidade tem um nível baixo de emissão de CO2, o que é desejável para o meio ambiente.
Alta: Indica que a localidade tem um nível mais elevado de emissão de CO2, o que pode sugerir que a região tenha uma pegada ambiental maior.
Contribuindo
Se você deseja contribuir para o projeto, fique à vontade para enviar um pull request! Antes de contribuir, por favor, abra uma issue para discutir mudanças significativas.
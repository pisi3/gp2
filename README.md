# Cars Price Predictions

<h4 align="center">
	🚧   Concluído 🚀 🚧
</h4>

## 💻 Sobre o Projeto

Descrição da finalidade do projeto , dos objetivos primários e secundários conclusão das metas atingidas

Tabela de Conteúdos
=================
<!--ts-->
  * [Sobre o projeto](#-sobre-o-projeto)
  * [Funcionalidades](#-funcionalidades)
  * [Layout](#-layout)
  * [Como executar o projeto](#-como-executar-o-projeto)
    * [Pré-requisitos](#pré-requisitos)
    * [Rodando a aplicação web (Streamlit)](#user-content--rodando-a-aplicação-web-frontend)
  * [Tecnologias](#-tecnologias)
  * [Autor(es)](#-autor(es))
  * [Licença](#user-content--licença)
<!--te-->





## 🎨 Layout

## ⚙️ Funcionalidades

- [x] transformat database
- [x] Cabeçalho
- [x] Gráfico BoxPlot
- [x] Gráfico de Dispersão
- [x] Gráfico Treemap
- [x] Análise Exploratória
- [x] Machine Learning
- [x] Comparate Machine Learning



## 🚀 Como executar o projeto

Este projeto foi desenvolvido e executado no servidor Streamlit:  [Web App(streamlit)](https://streamlit.io)



### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Python](https://www.python.org/downloads/) e um editor de código [VSCode](https://code.visualstudio.com/).
Baixe o dataset que será usado no projeto: [Car Price Predictions]( https://www.kaggle.com/datasets/harikrishnareddyb/used-car-price-predictions), salve na pasta do projeto gp2/data e renomeie o arquivo para cars_price.



#### 🧭 Rodando a aplicação web (Frontend)

```bash

# Clone este repositório
$ git clone https://github.com/pisi3/gp2.git

# Acesse a pasta do projeto no seu terminal/cmd
$ cd 

# Recomendamos criar um abiente virtual com mesmo nome da pasta do projeto.
$ python -m venv venv

# Vá para a pasta venv
$ cd venv

# Instale as dependências
$ pip install -r requirements.txt

# Converta o dataset em .parquet
$ cd venv/project/utils/

# Execute o transform_pkl.py
$ cd venv/transform_pkl.py

# Executa a aplicação streamlit
$ streamlit run Home.py

# A aplicação será aberta na porta:Local URL: http://localhost:8501
  Network URL: http://192.168.0.103:8501


```
---
## Video explicativo

<p align = "center">
<img width="600" height=auto src=" ">
</p>

---
## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

#### **WebApp**  ([Streamlit](https://streamlit.io)  +  [Python](https://www.python.org))

-   **[Pandas](https://pandas.pydata.org)**
-   **[Numpy](https://numpy.org)**
-   **[Scikit-Learn](https://scikit-learn.org/stable/)**
-   **[MatplotLib](https://matplotlib.org)**
-   **[Plotly](https://plotly.com)**

---

### Autor(es)

* Silas Ribeiro
* Vitor
* Edniz Leandro
* Igor

---

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).

Feito por  Silas Ribeiro | Vitor | Edniz Leandro | Igor

---

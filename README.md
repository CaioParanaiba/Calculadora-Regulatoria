<p align="center">
  <img src="static/images/logo.jpg" alt="Logo" width="200" style="border-radius: 50%;">
</p>

<h1 align="center"><strong>Calculadora de Impacto Regulatória para Empreendedores</strong></h1>

---

<p align="center">
  <!-- Contribuidores -->
  <a href="https://github.com/CaioParanaiba/Calculadora-Regulatoria/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/CaioParanaiba/Calculadora-Regulatoria" alt="Contributors">
  </a>
  <!-- Última atualização -->
  <a href="https://github.com/CaioParanaiba/Calculadora-Regulatoria">
    <img src="https://img.shields.io/github/last-commit/CaioParanaiba/Calculadora-Regulatoria" alt="Last Update">
  </a>
  <!-- Licença -->
  <a href="https://github.com/CaioParanaiba/Calculadora-Regulatoria/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/CaioParanaiba/Calculadora-Regulatoria.svg" alt="License">
  </a>
  <!-- Versão do Python -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python Version">
  </a>
  <!-- Issues abertas -->
  <a href="https://github.com/CaioParanaiba/Calculadora-Regulatoria/issues">
    <img src="https://img.shields.io/github/issues/CaioParanaiba/Calculadora-Regulatoria" alt="Open Issues">
  </a>
  <!-- Tamanho do repositório -->
  <a href="https://github.com/CaioParanaiba/Calculadora-Regulatoria">
    <img src="https://img.shields.io/github/repo-size/CaioParanaiba/Calculadora-Regulatoria" alt="Repo Size">
  </a>
  <!-- Linguagem principal -->
  <a href="https://github.com/CaioParanaiba/Calculadora-Regulatoria">
    <img src="https://img.shields.io/github/languages/top/CaioParanaiba/Calculadora-Regulatoria" alt="Top Language">
  </a>
</p>


## **🌟 Descrição**

A **Calculadora de Impacto Regulatório** é uma aplicação web moderna, desenvolvida em **Python** com o framework **Flask**, que auxilia o empreendedor a:

- Compreender e calcular os custos associados a regulamentações;
- Garantir eficiência, escalabilidade e confiabilidade com integração ao **AWS RDS** (gerenciamento de banco de dados) e execução em um servidor na nuvem (**AWS EC2**);
- Oferecer uma interface visualmente agradável e intuitiva para empresários e gestores.

---

## **🎯 Objetivos**

✅ **Proporcionar uma solução prática** para calcular custos regulatórios, ajudando empresas a quantificar e visualizar os impactos financeiros.

✅ **Garantir armazenamento seguro e escalável** utilizando **AWS RDS**.

✅ **Fornecer uma interface moderna e responsiva**, com gráficos interativos e funcionalidades intuitivas.

✅ **Simplificar a gestão de dados**, consolidando o banco de dados em uma estrutura eficiente e acessível.

---

## **🚀 Principais Funcionalidades**

### 1️⃣ **Cálculo Personalizado de Custos**
- Automatiza cálculos com base em subcategorias predefinidas e personalizáveis.
- Suporte total para **Subcategorias Personalizadas (SubcategoriasPer)**.

### 2️⃣ **Visualização Interativa de Resultados**
- Gráficos dinâmicos e interativos para análise de custos.
- Relatórios visuais que facilitam a compreensão dos resultados.

### 3️⃣ **Banco de Dados Simplificado**
- Estrutura consolidada com tabelas essenciais:
  - **Subcategoria**: Informações padronizadas de custos.
  - **SubcategoriasPer**: Personalizações realizadas pelo usuário.
  - **Custo**: Registros dos cálculos realizados.
  - **Empresa**: Dados básicos de empresas e projetos.

### 4️⃣ **Interface Melhorada**
- Design moderno com gradientes e funcionalidades interativas.
- Otimização para dispositivos móveis e navegadores.

### 5️⃣ **Execução na Nuvem**
- Hospedagem no **AWS EC2**, garantindo alta disponibilidade.
- Banco de dados gerenciado com **AWS RDS** para maior confiabilidade.

### 6️⃣ **Exportação e Relatórios (Futuro)**
- Planejamento para exportação de relatórios em PDF e integração com ferramentas externas.

---

### **✨ Destaques Visuais**
Para maximizar a interação do usuário, os gráficos interativos e a interface moderna foram projetados para serem altamente responsivos e fáceis de navegar.

<p align="center">
  <img src="static/images/gif1.gif" alt="Demonstração da Aplicação" width="600">
</p>


---
## **📁 Estrutura de Diretórios**

A estrutura de diretórios da aplicação foi planejada para garantir organização e facilitar o desenvolvimento. 

<details>
<summary><strong>👁️ Clique para expandir</strong></summary>

```plaintext
Calculadora-Regulatoria/
│
├── application.py          # Arquivo principal do Flask
├── configure.py            # Configurações do Flask (conexão com RDS, etc.)
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto
│
├── database/               # Gerenciamento de banco de dados
│   ├── models/             # Modelos ORM (ex.: Subcategoria, Empresa)
│   │   └── database.py     # Conexão com o banco (AWS RDS)
│   └── routes/             # Rotas da aplicação
│
├── static/                 # Arquivos estáticos
│   ├── css/                # Estilos CSS
│   │   └── styles.css
│   ├── images/             # Imagens usadas no projeto
│   └── js/                 # Scripts JavaScript
│
├── templates/              # Arquivos HTML renderizados pelo Flask
│   └── ...                 # Ex.: base.html, index.html, resultado.html
│
└── venv/                   # Ambiente virtual Python (não incluído no repositório)
```

</details>

### **📚 Detalhes da Estrutura**
- **`application.py`**: Ponto de entrada do aplicativo Flask.
- **`configure.py`**: Configurações principais, como a conexão com o banco de dados na AWS RDS.
- **`database/`**:
  - **`models/`**: Contém os modelos Peewee que representam o esquema do banco de dados.
  - **`routes/`**: Arquivos responsáveis pelas rotas HTTP da aplicação.
- **`static/`**: Contém arquivos estáticos como estilos CSS, JavaScript e imagens.
- **`templates/`**: Páginas HTML renderizadas dinamicamente pelo Flask.
- **`venv/`**: Ambiente virtual para dependências Python (excluído no repositório).

### **📦 Arquivos Relevantes**
- **`requirements.txt`**: Lista de bibliotecas necessárias para rodar a aplicação.
- **`README.md`**: Documentação do projeto.

---

## **🛠 Tecnologias Utilizadas**

### **Backend**
<p>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python">
  </a>
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  </a>
  <a href="http://docs.peewee-orm.com/en/latest/">
    <img src="https://img.shields.io/badge/Peewee-ORM-green" alt="Peewee">
  </a>
</p>
<p align="center"><em>Frameworks e ferramentas robustas para a construção e conexão do backend com o banco de dados.</em></p>

---

### **Frontend**
<p>
  <a href="https://developer.mozilla.org/pt-BR/docs/Web/HTML">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  </a>
  <a href="https://developer.mozilla.org/pt-BR/docs/Web/CSS">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  </a>
  <a href="https://developer.mozilla.org/pt-BR/docs/Web/JavaScript">
    <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" alt="JavaScript">
  </a>
</p>
<p align="center"><em>Interface responsiva e moderna desenvolvida com tecnologias web padrão.</em></p>

---

### **Banco de Dados**
<p>
  <a href="https://www.postgresql.org/">
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  </a>
</p>
<p align="center"><em>Banco de dados relacional gerenciado na nuvem para garantir escalabilidade e segurança.</em></p>

---

### **Hospedagem**
<p>
  <a href="https://aws.amazon.com/pt/ec2/">
    <img src="https://img.shields.io/badge/AWS_EC2-FF9900?logo=amazon-aws&logoColor=white" alt="AWS EC2">
  </a>
  <a href="https://aws.amazon.com/pt/rds/">
    <img src="https://img.shields.io/badge/AWS_RDS-527FFF?logo=amazon-aws&logoColor=white" alt="AWS RDS">
  </a>
</p>
<p align="center"><em>Execução na nuvem com alta disponibilidade e gerenciamento de banco de dados confiável.</em></p>


---


## 🚀 **Instalação**

### ⚙️ **Pré-requisitos**
- ✅ **Python** 3.10 ou superior
- ✅ Ambiente virtual configurado (`venv`)
- ✅ Acesso ao banco de dados **AWS RDS**

---

### 🛠️ **Passos para Instalação**

1. **Clone o repositório**  
   Baixe o código do projeto no seu computador:
   ```bash
   git clone https://github.com/CaioParanaiba/Calculadora-Regulatoria.git
   cd Calculadora-Regulatoria
   ```

2. **Crie e ative o ambiente virtual**  
   Crie um ambiente virtual para instalar as dependências isoladamente:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**  
   Use o arquivo `requirements.txt` para instalar todas as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o acesso ao banco de dados**  
   Crie um arquivo `.env` na raiz do projeto e adicione sua URL do banco de dados:
   ```env
   DATABASE_URL=postgresql://usuario:senha@rds-endereco:5432/nome_banco
   ```

5. **Execute a aplicação**  
   Inicie o servidor Flask:
   ```bash
   python application.py
   ```

6. **Acesse a aplicação localmente**  
   Abra no navegador:
   ```
   http://localhost:5000
   ```

---

## 🌐 **Acessando a Aplicação Online**
A aplicação está disponível publicamente em:  
🔗 [http://calcreg.com.br](http://calcreg.com.br)

---

## 🤝 **Contribuindo**

Contribuições são super bem-vindas! Siga os passos abaixo para colaborar com o projeto:

1. **Faça um fork do repositório**  
   ```bash
   git clone https://github.com/CaioParanaiba/Calculadora-Regulatoria.git
   ```

2. **Crie um branch para sua feature ou correção**  
   ```bash
   git checkout -b minha-feature
   ```

3. **Envie seu pull request**  
   Após implementar as mudanças, envie um pull request descrevendo suas alterações.

---

## 📬 **Contato**

Entre em contato para dúvidas ou feedback:

- 📧 **E-mail:** [caioparanaiba@discente.ufg.br](mailto:caioparanaiba@discente.ufg.br)
- 💼 **LinkedIn:** [Caio Paranaiba](https://linkedin.com/in/caioparanaiba)
- 🐙 **GitHub:** [CaioParanaiba](https://github.com/CaioParanaiba)

---

## 📝 **Licença**

Este projeto está sob a licença MIT. Para mais detalhes, leia o arquivo [LICENSE](https://github.com/CaioParanaiba/Calculadora-Regulatoria/blob/main/LICENSE).



# 🐍 Automated Data Extractor & Tracker

Este é um script de Web Scraping desenvolvido em Python para extrair oportunidades de emprego de forma automatizada. Ele acessa uma página web, localiza as vagas disponíveis, filtra oportunidades específicas e salva os dados limpos em uma planilha CSV.

## 🚀 Funcionalidades

- **Navegação Automatizada:** Utiliza o Selenium WebDriver para abrir o navegador e carregar as páginas dinamicamente.
- **Mapeamento de Elementos (XPath):** Localiza com precisão os "cartões" de vagas usando a estrutura HTML do site.
- **Filtro Inteligente:** O robô varre os títulos extraídos e seleciona apenas as vagas que contenham a palavra-chave (ex: "Scientist" ou "Cientista").
- **Limpeza de Dados (Regex):** Usa Expressões Regulares para remover espaços em branco excessivos e quebras de linha indesejadas.
- **Exportação (CSV):** Salva os resultados estruturados (Título, Empresa, Link) em um arquivo `.csv` pronto para análise de dados.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Selenium** (Automação web)
- **Regex** (Manipulação de strings)
- **CSV** (Manipulação de arquivos)

## ⚙️ Como executar o projeto

### Pré-requisitos
É necessário ter o [Python](https://www.python.org/) instalado em sua máquina.

### Passo a passo

1. Clone este repositório para o seu computador:
   > git clone https://github.com/SEU_USUARIO/automated-data-extractor.git

2. Entre na pasta do projeto:
   > cd automated-data-extractor

3. Instale a biblioteca do Selenium:
   > pip install selenium

4. Execute o robô:
   > python scraper.py

5. O navegador será aberto automaticamente, a extração será feita e o arquivo `vagas_cientista.csv` será criado na mesma pasta!

## 👨‍💻 Autor

Projeto desenvolvido como parte do aprendizado em automação e Web Scraping com Python.
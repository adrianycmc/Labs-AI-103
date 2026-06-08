# Aplicativo de IA generativa com uso de ferramentas

O objetivo deste laboratório é criar um aplicativo de chat de IA generativa que utiliza ferramentas para buscar informações em documentos PDF locais e na web. O aplicativo irá demonstrar o uso da Assistants API e Vector Stores para fornecer respostas precisas e relevantes às perguntas dos usuários.


## 🛠️ Tecnologias e SDKs

- **Linguagem:** Python
- **SDK:** `openai` (Biblioteca oficial compatível com Azure OpenAI)
- **Outras dependências:** `python-dotenv`, `aiohttp`, `azure-identity`

## 🧠 Conceitos Técnicos Abordados

- **Assistants API:** Uso de modelos com capacidades de ferramentas integradas.
- **RAG (Retrieval-Augmented Generation):** Busca de informações em documentos PDF locais usando vetores.
- **Vector Stores:** Criação e gerenciamento de bases de dados vetoriais para indexação de documentos.
- **Tool Choice:** Seleção inteligente entre busca em arquivos (`file_search`) e busca na web (`web_search`).

## 📁 Estrutura do Projeto

- `apps/tools-app.py`: Aplicativo principal que utiliza ferramentas de busca.
- `brochures/`: Pasta contendo os arquivos PDF para indexação.
- `.env`: Configurações de endpoint, chave e versão da API.

## 🔧 Configuração do Ambiente

### 1. Criar e Ativar Ambiente Virtual
Recomenda-se o uso de um ambiente virtual para isolar as dependências:
```powershell
# Criar o ambiente virtual (Windows)
py -m venv .venv

# Ativar o ambiente (Windows)
.venv\Scripts\Activate.ps1
```

### 2. Instalação das dependências
Execute o comando abaixo para instalar as bibliotecas necessárias:
```powershell
pip install -r requirements.txt
```

### 3. Variáveis de Ambiente
Crie um arquivo `.env` na raiz desta pasta (`02. Aplicativo de IA generativa com uso de ferramentas`) com as seguintes configurações:
```env
AZURE_OPENAI_ENDPOINT=<seu-endpoint-aqui>
AZURE_OPENAI_KEY=<sua-chave-aqui>
MODEL_DEPLOYMENT=<nome-da-sua-implantacao>
API_VERSION_OPENAI=<versao-da-api-aqui>
```

## 🚀 Como Executar

Certifique-se de estar dentro do diretório do laboratório e com o ambiente virtual ativo:

```powershell
python apps/tools-app.py
```

## 🔐 Segurança e Boas Práticas
- O arquivo `.env` contém credenciais sensíveis e deve ser listado no `.gitignore`.
- Utilize APIs modernas (`responses`) quando for necessário manter o histórico da conversa de forma eficiente.

---

O exercício está disponível em: [Crie um aplicativo de chat de IA generativa | Desenvolver soluções de IA generativa no Azure](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/03-foundry-sdk.html#summary)

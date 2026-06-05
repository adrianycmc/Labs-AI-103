# Chat com IA Generativa

Este laboratório demonstra como criar um aplicativo de chat utilizando o Azure OpenAI Service e o SDK da OpenAI para Python. O foco é implementar interações síncronas e assíncronas, além de utilizar o streaming para respostas em tempo real.

## 🛠️ Tecnologias e SDKs

- **Linguagem:** Python
- **SDK:** `openai` (Biblioteca oficial compatível com Azure OpenAI)
- **Outras dependências:** `python-dotenv`, `aiohttp`, `azure-identity`

## 🧠 Conceitos Técnicos Abordados

- **Chat Completions API:** Interface padrão para geração de texto conversacional.
- **Responses API:** Novo namespace recomendado para manter o estado e contexto da conversa simplificado via `previous_response_id`.
- **Streaming:** Processamento e exibição gradual da resposta gerada pelo modelo.
- **Async Programming:** Utilização de `asyncio` e `AsyncAzureOpenAI` para chamadas não bloqueantes.

## 📁 Estrutura do Projeto

- `app/chat-app.py`: Versão síncrona demonstrando Chat Completions, Responses API e Streaming.
- `app/chat-async.py`: Versão assíncrona utilizando `AsyncAzureOpenAI`.
- `requirements.txt`: Lista de pacotes necessários para o ambiente.

## 🔧 Configuração do Ambiente

### 1. Criar e Ativar Ambiente Virtual
Recomenda-se o uso de um ambiente virtual para isolar as dependências:
```powershell
# Criar o ambiente virtual
python -m venv .venv

# Ativar o ambiente (Windows)
.venv\Scripts\Activate.ps1
```

### 2. Instalação das dependências
Execute o comando abaixo para instalar as bibliotecas necessárias:
```powershell
pip install -r requirements.txt
```

### 3. Variáveis de Ambiente
Crie um arquivo `.env` na raiz da pasta `01. Chat com IA generativa` com as seguintes configurações técnicas:
```env
AZURE_OPENAI_ENDPOINT=<seu-endpoint-aqui>
AZURE_OPENAI_KEY=<sua-chave-aqui>
MODEL_DEPLOYMENT=<nome-da-sua-implantacao>
API_VERSION_OPENAI=<versao-da-api-aqui>
```

## 🚀 Como Executar

Certifique-se de estar dentro do diretório do laboratório antes de iniciar:

**Para a versão síncrona:**
```powershell
python app/chat-app.py
```

**Para a versão assíncrona:**
```powershell
python app/chat-async.py
```

## 🔐 Segurança e Boas Práticas
- O arquivo `.env` contém credenciais sensíveis e deve ser listado no `.gitignore`.
- Utilize APIs modernas (`responses`) quando for necessário manter o histórico da conversa de forma eficiente.

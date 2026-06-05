# Laboratórios AI-103 - Microsoft Azure AI Engineer

Este repositório contém os laboratórios práticos do curso **AI-103: Desenvolver aplicativos e agentes de IA no Azure**. Aqui você encontrará exercícios hands-on para aprender a trabalhar com serviços de IA do Azure, incluindo Azure OpenAI, Microsoft Foundry e outras tecnologias de IA generativa.

## 🛠️ Laboratórios Disponíveis

- **[01. Chat com IA generativa](./01.%20Chat%20com%20IA%20generativa/)**: Aprenda a criar um app de chat com Azure OpenAI, explorando Chat Completions, Responses API e Streaming.

## ℹ️ Sobre o Repositório

Este é um repositório de estudos contendo implementações práticas dos laboratórios oficiais da Microsoft para o curso AI-103. Cada pasta representa um laboratório específico com código, documentação e exemplos completos.

## 📋 Pré-requisitos

Antes de começar os exercícios, certifique-se de que você tem:

- Uma [assinatura ativa do Azure](https://azure.microsoft.com/pricing/purchase-options/azure-account)
- [Visual Studio Code](https://code.visualstudio.com/) instalado
- [Python versão **3.13.xx**](https://www.python.org/downloads/release/python-31312/) instalado
- [Git](https://git-scm.com/install/) instalado e configurado
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?view=azure-cli-latest) instalado

## 🚀 Como criar um projeto no Microsoft Foundry

Para executar qualquer um dos laboratórios, você precisará configurar um projeto e uma implantação de modelo no Azure AI Foundry:

### Passo 1: Acesse o Portal do Azure AI Foundry
1. Acesse [ai.azure.com](https://ai.azure.com)
2. Faça login com sua conta Azure

### Passo 2: Crie um novo projeto
1. No portal, clique em **"+ Create project"** ou **"Criar projeto"**
2. Preencha as informações necessárias:
   - **Nome do projeto**: escolha um nome descritivo (ex: `AI-103-Labs`)
   - **Subscription**: selecione sua assinatura Azure
   - **Resource group**: crie um novo ou use um existente
3. Clique em **"Create"** ou **"Criar"**

### Passo 3: Configure o Azure OpenAI (Implantação)
1. No seu projeto, navegue até **"Deployments"** ou **"Implantações"**
2. Clique em **"+ Create deployment"** ou **"Criar implantação"**
3. Selecione um modelo (recomendado: `gpt-4o` ou `gpt-35-turbo`)
4. Defina um nome para a implantação (anote este nome para o arquivo `.env`)
5. Configure as opções de capacidade e clique em **"Deploy"**

### Passo 4: Obtenha as credenciais
1. Vá até a seção **"Project settings"** ou procure por chaves em **"Keys and Endpoint"**
2. Copie os seguintes valores técnicos:
   - **Endpoint**: URL do serviço
   - **API Key**: chave de acesso (`Key 1` ou `Key 2`)
   - **Deployment Name**: o nome que você definiu no Passo 3
   - **API Version**: (ex: `2024-05-01-preview`)

## 🏁 Conclusão e Próximos Passos

Ao concluir esses laboratórios, você terá uma base sólida na construção de soluções de IA generativa utilizando a infraestrutura do Microsoft Azure. Sinta-se à vontade para explorar os outros diretórios de laboratórios à medida que forem adicionados, ou para expandir as implementações atuais com novas funcionalidades (filtros de conteúdo, RAG, etc.).

Se tiver dúvidas durante o processo, consulte a [Documentação Oficial do Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/) ou o portal [Microsoft Learn](https://learn.microsoft.com/pt-br/training/courses/ai-103t00).

---
**Desenvolvido como parte dos estudos para a certificação Microsoft Certified: Azure AI Engineer Associate.**

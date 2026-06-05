import os
from dotenv import load_dotenv
import asyncio
from openai import AsyncAzureOpenAI

async def main(): 

    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        load_dotenv()
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")
        subscription_key = os.getenv("AZURE_OPENAI_KEY")
        api_version_openai = os.getenv("API_VERSION_OPENAI")

        async_client = AsyncAzureOpenAI(
            azure_endpoint=azure_openai_endpoint,
            api_version=api_version_openai,
            api_key=subscription_key
        )
        
        last_response_id = None

        while True:
            input_text = input('\nEnter a prompt (or type "quit" to exit): ')
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
            
            ## Primeiro método de chamada da API, utilizando o namespace responses, que é recomendado para manter o contexto da conversa

            # response = await async_client.responses.create(
            #     model=model_deployment,
            #     instructions="You are a helpful AI assistant that answers questions and provides information.",
            #     input=input_text,
            #     previous_response_id=last_response_id
            # )
            # assistant_text = response.output_text

            # print("Assistant:", assistant_text)
            # last_response_id = response.id

            ##  Segundo método de chamada da API, utilizando o namespace de responses e streaming, para receber a resposta em tempo real, à medida que o modelo a gera

            stream = await async_client.responses.create(
                model=model_deployment,
                instructions="You are a helpful AI assistant that answers questions and provides information.",
                input=input_text,
                previous_response_id=last_response_id,
                stream=True
            )

            async for event in stream:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="")
                elif event.type == "response.completed":
                    last_response_id = event.response.id
            print()
            

    except Exception as ex:
        print(ex)

    finally:
        await async_client.close()


if __name__ == '__main__': 
    asyncio.run(main())
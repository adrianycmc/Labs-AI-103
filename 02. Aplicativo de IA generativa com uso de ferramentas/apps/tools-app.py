import os
from dotenv import load_dotenv
import glob
from openai import AzureOpenAI

def main(): 
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        load_dotenv()
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")
        subscription_key = os.getenv("AZURE_OPENAI_KEY")
        api_version_openai = os.getenv("API_VERSION_OPENAI")

        openai_client = AzureOpenAI(
            azure_endpoint=azure_openai_endpoint,
            api_version=api_version_openai,
            api_key=subscription_key
        )

        print("Creating vector store and uploading files...")

        # Criação do vector store
        vector_store = openai_client.vector_stores.create(
            name="travel-brochures"
        )
        file_streams = [open(f, "rb") for f in glob.glob("02. Aplicativo de IA generativa com uso de ferramentas/brochures/*.pdf")]
        if not file_streams:
            print("No PDF files found in the brochures folder!")
            return
        
        # Upload e indexação dos arquivos usando o recurso de file_batches
        file_batch = openai_client.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store.id,
            files=file_streams
        )
        for f in file_streams:
            f.close()
        print(f"Vector store created with {file_batch.file_counts.completed} files.")

        last_response_id = None

        while True:
            input_text = input('\nEnter a question (or type "quit" to exit): ')
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a question.")
                continue
            
            response = openai_client.responses.create(
                model=model_deployment,
                instructions="""
                You are a travel assistant that provides information on travel services available from Margie's Travel.
                Answer questions about services offered by Margie's Travel using the provided travel brochures.
                Search the web for general information about destinations or current travel advice.
                """,
                input=input_text,
                previous_response_id=last_response_id,
                tools=[
                    {
                        "type": "file_search",
                        "vector_store_ids": [vector_store.id]
                    },
                    {
                        "type": "web_search"
                    }
                ]
                )
            print(response.output_text)
            last_response_id = response.id


    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()
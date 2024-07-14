import mindsdb_sdk
import time, os
from dotenv import load_dotenv


load_dotenv()

GEMINI_API_KEY = os.getenv('API_KEY')


server = mindsdb_sdk.connect()

gemini_handler = server.ml_handlers.google_gemini



def get_gemini_engine():
    ml_engine = 'google_gemini_engine'    
    # create or get ml engine
    try:
        gemini = server.ml_engines.create(
            ml_engine,
            handler=gemini_handler,
            connection_data={
                'google_gemini_api_key' : GEMINI_API_KEY
            }
        )
    except Exception as e:
        if "already exists" in str(e):
                print(f"ML engine {ml_engine} already exists.")
                gemini = server.ml_engines.get(ml_engine)
        else:
            print(f"Error creating ML engine: {e}")

    return gemini


def get_gemini_model(gemini_engine):
    model_name = 'gem_p'
    try:     
        # create model
        model = server.models.create(
            model_name,
            predict='transformed_recipe',
            column='original_recipe', 
            engine=gemini_engine,  # created ml engine
            prompt_template="Extract the 'recipe name' and the 'diet' from the following recipe and then Transform it to cater to the extracted diet. Maintain the essence and flavor profile as much as possible: {{original_recipe}}"
        )
    except Exception as e:
        if "already exists" in str(e):
                print(f"model {model_name} already exists.")
                model = server.models.get(model_name)
        else:
            print(f"Error creating model: {e}")

    model_status = model.get_status()
    while model_status != 'complete':
        print(f"Model {model.name} creation not completed : {model_status}")
        model_status = model.get_status()
        time.sleep(3.5)
    # model generation completed
    return model


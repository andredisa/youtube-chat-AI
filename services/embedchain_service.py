from embedchain  import App

def create_embedchain_app(db_path: str, api_key:str)-> App:
    return App.from_config({
            "llm": {"provider": "openai", "config": {"model": "gpt-4", "temperature": 0.5, "api_key": api_key}},
            "vectordb": {"provider": "chroma", "config": {"dir": db_path}},
            "embedder": {"provider": "openai", "config": {"api_key": api_key}},
        })
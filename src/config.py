from dataclasses import dataclass
import os
from dotenv import load_dotenv

@dataclass
class Config:

    groq_api_key: str

    @classmethod
    def load_config(cls) -> 'Config':

        load_dotenv()

        groq_api_key = os.getenv('GROQ_API_KEY')
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY must be set in .env")
        
        return cls(
            groq_api_key=groq_api_key
        )
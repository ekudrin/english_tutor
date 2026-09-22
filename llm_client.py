import ollama
from config import MODEL_NAME, MAX_TOKENS, TEMPERATURE

class LLMClient:
    def __init__(self):
        self.history = []
    
    def add_user_message(self, message: str):
        self.history.append({"role": "user", "content": message})
        
    def get_bot_response(self) -> str:
        if not self.history: return "Hello! How are you today?"
        messages = [{"role": "system", "content": open('config.py').read().split('SYSTEM_PROMPT = """')[1].split('"""')[0].strip()}] + \
            [{"role": "system", "content": open('config.py').read().split('INSTRUCTIONS_FOR_BOT = """')[1].split('"""')[0].strip()}] + \
                self.history
        
        try:
            response = ollama.chat(
                model=MODEL_NAME,
                messages=messages,
                options={ 'temperature': TEMPERATURE, 'num_predict': MAX_TOKENS } 
                )
            bot_text = response['message']['content'].strip()
            self.history.append({"role": "assistant", "content": bot_text})
            return bot_text
        
        except Exception as e:
            print(f"Error connecting to Ollama: {e}")
            return "Sorry, I am having trouble thinking right now."
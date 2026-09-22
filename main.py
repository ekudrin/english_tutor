from llm_client import LLMClient
from grammar_checker import GrammarChecker
from dialogue_manager import DialogueManager

def main():
    print("Loading tutor...")
    
    client = LLMClient()
    checker = GrammarChecker()
    manager = DialogueManager()

    print("English Tutor is ready! Type '/quit' to exit.\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['/quit', '/exit']:
            print("Goodbye! Keep practicing.")
            break

        client.add_user_message(user_input)
        
        # Проверяем грамматику ДО вызова модели, чтобы не тратить время API
        errors = checker.check(user_input)
        error_report = checker.format_errors(errors)
        if error_report:
            print(error_report)

        bot_reply = client.get_bot_response()
        print(f"Tutor: {bot_reply}")

        # Предлагаем задание уже ПОСЛЕ ответа бота
        if manager.should_suggest_task():
            task = manager.generate_task_or_question()
            print(f"Tutor: {task}")
            client.add_user_message(task) # Добавляем задание в историю, чтобы бот ждал ответа именно на него

if __name__ == "__main__":
    main()
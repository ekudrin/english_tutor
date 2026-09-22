import random

class DialogueManager:
    def __init__(self):
        self.turn_count = 0
        self.suggested_topics = [
            "hobbies", "travel", "food", "movies", "your city", "learning English"
        ]

    def should_suggest_task(self) -> bool:
        self.turn_count += 1
        return self.turn_count % 4 == 0

    def generate_task_or_question(self) -> str:
        tasks = [
            "By the way, can you translate this sentence: 'Я люблю пить кофе по утрам'?",
            "Let's practice prepositions. Fill in the blank: 'I am interested ___ learning Spanish'.",
            "Quick question: What did you do last weekend? Use Past Simple.",
            f"Let's change the topic. Tell me three things you like about {random.choice(self.suggested_topics)}."
        ]
        return random.choice(tasks)
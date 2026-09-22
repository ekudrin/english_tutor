import language_tool_python

class GrammarChecker:
    def __init__(self):
        # Используем английскую базу правил
        self.tool = language_tool_python.LanguageTool('en-US')

    def check(self, text: str) -> list[dict]:
        if not text.strip():
            return []
        
        matches = self.tool.check(text)
        errors = []
        for match in matches:
            errors.append({
                'message': match.message,
                'replacements': match.replacements[:3], # Показываем до 3 вариантов исправления
                'context': text[match.offset:match.offset + match.error_length]
            })
        return errors

    def format_errors(self, errors: list[dict]) -> str:
        if not errors:
            return ""
        
        output = "\n--- Grammar Check ---\n"
        for err in errors:
            repl = ", ".join(err['replacements']) if err['replacements'] else "[no suggestions]"
            output += f"-> '{err['context']}' -> {repl}\nПричина: {err['message']}\n"
        output += "---------------------\n\n"
        return output
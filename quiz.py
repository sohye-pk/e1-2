class Quiz:
    def __init__(self, question, choices, answer, hint=None):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def show_question(self):
        print()
        print(f"{self.question} (0: 힌트 보기)")

        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer

    def show_hint(self):
        if self.hint:
            print(f"힌트: {self.hint}")
        else:
            print("힌트가 없습니다.")
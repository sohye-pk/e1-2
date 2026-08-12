import json

from quiz import Quiz
from quiz_data import DEFAULT_QUIZZES
from quiz_record import QuizRecord


class DataManager:
    FILE_PATH = "state.json"

    def load_data(self):
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)

            quizzes = [
                Quiz(
                    quiz_data["question"],
                    quiz_data["choices"],
                    quiz_data["answer"],
                    quiz_data.get("hint")
                )
                for quiz_data in data["quizzes"]
            ]

            best_score = data.get("best_score", 0)

            history = [
                QuizRecord.from_dict(record)
                for record in data.get("history", [])
            ]

            return quizzes, best_score, history

        except (FileNotFoundError, json.JSONDecodeError, KeyError, TypeError):
            print("저장된 데이터를 불러올 수 없습니다.")
            print("기본 퀴즈 데이터를 사용합니다.")

            return DEFAULT_QUIZZES.copy(), 0, []

    def save_data(self, quizzes, best_score, history):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                    "hint": quiz.hint
                }
                for quiz in quizzes
            ],
            "best_score": best_score,
            "history": [
                record.to_dict()
                for record in history
            ]
        }

        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
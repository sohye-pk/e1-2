from datetime import datetime


class QuizRecord:
    def __init__(self, quiz_count, score, played_at=None):
        self.quiz_count = quiz_count
        self.score = score
        self.played_at = played_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "played_at": self.played_at,
            "quiz_count": self.quiz_count,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["quiz_count"],
            data["score"],
            data["played_at"]
        )
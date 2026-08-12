import random

from quiz import Quiz
from input_handler import InputHandler
from data_manager import DataManager


class QuizGame:
    def __init__(self):
        self.data_manager = DataManager()
        self.quizzes, self.best_score = self.data_manager.load_data()

    def run(self):
        try:
            while True:
                self.show_menu()

                choice = InputHandler.get_number("선택: ", 1, 6)

                if choice is None:
                    break

                if choice == 1:
                    self.play_quiz()

                elif choice == 2:
                    self.add_quiz()

                elif choice == 3:
                    self.show_quizzes()

                elif choice == 4:
                    self.delete_quiz()

                elif choice == 5:
                    self.show_score()

                elif choice == 6:
                    print("프로그램을 종료합니다.")
                    break

        finally:
            self.save_data()

    def show_menu(self):
        print()
        print("========================================")
        print("          나만의 퀴즈 게임")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 퀴즈 삭제")
        print("5. 점수 확인")
        print("6. 종료")
        print("========================================")

    def play_quiz(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        print()
        print("========================================")
        print("             퀴즈 시작")
        print("========================================")
        print(f"현재 등록된 퀴즈: {len(self.quizzes)}개")

        quiz_count = InputHandler.get_number("풀 문제 수: ", 1, len(self.quizzes))

        if quiz_count is None:
            return

        selected_quizzes = random.sample(self.quizzes, quiz_count)

        score = 0

        for index, quiz in enumerate(selected_quizzes, start=1):
            print()
            print(f"[{index}/{quiz_count}]")
            print(f"{quiz.question} (0: 힌트 보기)")

            for choice_index, choice in enumerate(quiz.choices, start=1):
                print(f"{choice_index}. {choice}")

            hint_used = False

            while True:
                answer = InputHandler.get_number("정답: ", 0, len(quiz.choices))

                if answer is None:
                    print("\n퀴즈를 종료합니다.")
                    return

                if answer == 0:
                    quiz.show_hint()
                    hint_used = True
                    continue

                if quiz.check_answer(answer):
                    if hint_used:
                        score += 0.5
                        print("정답입니다! +0.5점")
                    else:
                        score += 1
                        print("정답입니다! +1점")
                else:
                    print("오답입니다.")
                    print(f"정답: {quiz.answer}")

                break

        print()
        print("========================================")
        print("             퀴즈 종료")
        print("========================================")
        print(f"점수: {score} / {quiz_count}")

        if score > self.best_score:
            self.best_score = score
            print("최고 점수를 갱신했습니다!")

        print("========================================")

    def add_quiz(self):
        print()
        print("========================================")
        print("             퀴즈 추가")
        print("========================================")

        question = InputHandler.get_text("문제: ")

        if question is None:
            return

        choice_count = 4

        if choice_count is None:
            return

        choices = []

        for index in range(1, choice_count + 1):
            choice = InputHandler.get_text(f"{index}번 보기: ")

            if choice is None:
                return

            choices.append(choice)

        answer = InputHandler.get_number("정답 번호: ", 1, choice_count)

        if answer is None:
            return

        hint = InputHandler.get_optional_text("힌트(선택): ")

        if hint is None:
            return

        quiz = Quiz(question, choices, answer, hint)
        self.quizzes.append(quiz)

        print("\n퀴즈가 추가되었습니다.")

    def show_quizzes(self):
        print()
        print("========================================")
        print("             퀴즈 목록")
        print("========================================")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            print("========================================")
            return

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

        print("========================================")
        print(f"총 {len(self.quizzes)}개의 퀴즈가 등록되어 있습니다.")

    def delete_quiz(self):
        print("4. 퀴즈 삭제")

    def show_score(self):
        print("5. 점수 확인")

    def save_data(self):
        self.data_manager.save_data(
            self.quizzes,
            self.best_score
        )

    def load_data(self):
        pass
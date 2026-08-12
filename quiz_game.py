import random

from quiz_record import QuizRecord
from input_handler import InputHandler
from data_manager import DataManager


class QuizGame:
    def __init__(self):
        self.data_manager = DataManager()
        self.quizzes, self.best_score, self.history = self.data_manager.load_data()

    def run(self):
        try:
            while True:
                self.show_menu()

                choice = InputHandler.get_number("선택: ", 1, 6)

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

        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")

        except EOFError:
            print("\n입력 스트림이 종료되었습니다.")

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

        selected_quizzes = random.sample(self.quizzes, quiz_count)

        score = 0

        for index, quiz in enumerate(selected_quizzes, start=1):
            print()
            print(f"[{index}/{quiz_count}]")
            quiz.show_question()

            hint_used = False

            while True:
                answer = InputHandler.get_number("정답: ", 0, len(quiz.choices))

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

        record = QuizRecord(quiz_count, score)
        self.history.append(record)

        print("========================================")

    def add_quiz(self):
        print()
        print("========================================")
        print("             퀴즈 추가")
        print("========================================")

        question = InputHandler.get_text("문제: ")

        choice_count = 4
        choices = []

        for index in range(1, choice_count + 1):
            choice = InputHandler.get_text(f"{index}번 보기: ")
            choices.append(choice)

        answer = InputHandler.get_number("정답 번호: ", 1, choice_count)

        hint = InputHandler.get_optional_text("힌트(선택): ")

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
        if not self.quizzes:
            print("\n삭제할 퀴즈가 없습니다.")
            return

        print()
        print("========================================")
        print("             퀴즈 삭제")
        print("========================================")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

        print("========================================")

        quiz_index = InputHandler.get_number(
            "삭제할 퀴즈 번호: ",
            1,
            len(self.quizzes)
        )

        quiz = self.quizzes[quiz_index - 1]

        print()
        print(f"삭제할 퀴즈: {quiz.question}")

        while True:
            confirm = InputHandler.get_text("정말 삭제하시겠습니까? (y/n): ").lower()

            if confirm == "y":
                self.quizzes.pop(quiz_index - 1)
                print("퀴즈가 삭제되었습니다.")
                return

            if confirm == "n":
                print("삭제를 취소했습니다.")
                return

            print("y 또는 n을 입력해주세요.")

    def show_score(self):
        print()
        print("========================================")
        print("             점수 확인")
        print("========================================")
        print(f"최고 점수: {self.best_score}점")

        if not self.history:
            print("\n게임 기록이 없습니다.")
            print("========================================")
            return

        print()
        print("게임 기록")

        for index, record in enumerate(self.history, start=1):
            print(
                f"{index}. {record.played_at} | "
                f"{record.quiz_count}문제 | "
                f"{record.score}점"
            )

        print("========================================")

    def save_data(self):
        self.data_manager.save_data(
            self.quizzes,
            self.best_score,
            self.history
        )
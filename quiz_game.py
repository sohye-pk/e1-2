class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0

    def run(self):
        while True:
            try:
                self.show_menu()
                choice = int(input("선택: ").strip())

                if choice is None:
                    self.save_data()
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
                    self.save_data()
                    print("프로그램을 종료합니다.")
                    break

            except KeyboardInterrupt:
                print("\n프로그램을 종료합니다.")
                self.save_data()
                break

            except EOFError:
                print("\n입력 스트림이 종료되었습니다.")
                self.save_data()
                break

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
        print("1. 퀴즈 풀기")

    def add_quiz(self):
        print("2. 퀴즈 추가")

    def show_quizzes(self):
        print("3. 퀴즈 목록")

    def delete_quiz(self):
        print("4. 퀴즈 삭제")

    def show_score(self):
        print("5. 점수 확인")

    def save_data(self):
        pass

    def load_data(self):
        pass
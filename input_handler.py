class InputHandler:

    @staticmethod
    def get_text(prompt):
        while True:
            value = input(prompt).strip()

            if not value:
                print("입력값을 입력해주세요.")
                continue

            return value

    @staticmethod
    def get_optional_text(prompt):
        return input(prompt).strip()

    @staticmethod
    def get_number(prompt, min_value, max_value):
        while True:
            try:
                value = input(prompt).strip()

                if not value:
                    print("숫자를 입력해주세요.")
                    continue

                value = int(value)

                if value < min_value or value > max_value:
                    print(f"{min_value}-{max_value} 사이의 숫자를 입력해주세요.")
                    continue

                return value

            except ValueError:
                print("숫자만 입력해주세요.")
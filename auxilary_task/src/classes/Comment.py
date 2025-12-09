from typing import Self


class Comment:
    def __init__(
        self,
        text: str,
        autor: str,
    ):
        self.text = self.validate_value(text)
        self.autor = self.validate_value(autor, error_value="Автора не зазначено.")
        self.is_deleted = False
        self.replies: list[Comment] = []

    def __str__(self):
        return (
            "Цей коментар було видалено."
            if self.is_deleted
            else f"{self.autor.capitalize()}: {self.text.capitalize()}"
        )

    def validate_value(
        self, value: str, error_value="Текст коментаря не надано."
    ) -> str:
        if not value:
            raise ValueError(f"{error_value}")

        return value

    def add_reply(self, comment: Self) -> None:
        self.replies.append(comment)

    def remove_reply(self) -> None:
        self.is_deleted = True

    def display(self, level=0) -> None:
        print(f"{' ' * level * 4} {self}")

        if not self.replies:
            return

        for child in self.replies:
            child.display(level=level + 1)

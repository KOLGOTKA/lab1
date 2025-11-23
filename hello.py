
"""
Модуль для приветствия пользователя
"""
import typer

def hello_printer(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Формальное приветствие."),
    antiformal: bool = typer.Option(False, "--antiformal", "-af", help="Неформальное приветствие."),
):
    """
    Здоровается с пользоваетелем, используя повседневный, формальный или неформальный стиль.
    """
    # Формальный стиль
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    # Максимально неформальный стиль
    elif antiformal:
        print(f"Здаров, {name}!")
    # Повседневный стиль
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(hello_printer)

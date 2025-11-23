import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Формальное приветствие."),
    antiformal: bool = typer.Option(False, "--antiformal", "-af", help="Неформальное приветствие."),
):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и специфический стиль.
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
    typer.run(main)

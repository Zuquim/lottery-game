from random import randint


class Ticket:
    def __init__(self, spots: int, total_games: int):
        self.__games = []  # "Jogos"
        self.__spots = 0  # "Quantidade de dezenas"
        self.__total_games = 0  # "Total de jogos"
        self.__result = []  # "Resultado"
        self.set_spots(spots)  # SET "Quantidade de dezenas"
        self.set_total_games(total_games)  # SET "Total de jogos"

    def get_spots(self) -> int:
        return self.__spots

    def set_spots(self, quant: int):
        if 6 <= quant <= 10:
            self.__spots = quant
        else:
            print("Error! Spot quantity must be an integer between 6 and 10.")

    def get_total_games(self) -> int:
        return self.__total_games

    def set_total_games(self, total: int):
        self.__total_games = total

    def get_games(self) -> list[list]:
        return self.__games

    def set_games(self, games: list[list]):
        self.__games = games

    def get_result(self) -> list[int]:
        return self.__result

    def set_result(self, result: list[int]):
        self.__result = result

    def __randomize(self) -> list[int]:
        numbers = []
        while len(numbers) < self.get_spots():
            if (number := randint(1, 60)) not in numbers:
                numbers.append(number)
        numbers.sort()
        return numbers

    def generate_ticket(self):
        self.set_games([self.__randomize() for _ in range(self.get_total_games())])

    def generate_results(self):
        results = []
        while len(results) < 6:
            if (number := randint(1, 60)) not in results:
                results.append(number)
        results.sort()
        self.set_result(results)

    def check_games(self) -> str:
        if not self.get_games():
            print("Error! No games generated yet.")
        elif not self.get_result():
            print("Error! No results generated yet.")
        else:
            table = (
                "<table>\n"
                " <thead><tr><th>Game</th><th>Score</th></tr></thead>\n"
                " <tbody>\n"
                "{games}"
                " </tbody>\n"
                "</table>"
            )
            table_append = ""
            for game in self.get_games():
                score = sum(num in game for num in self.get_result())
                table_append += f"  <tr><td>{game}</td><td>{score}</td></tr>\n"
            return table.format(games=table_append)


if __name__ == "__main__":
    ticket = Ticket(spots=6, total_games=2)
    ticket.generate_ticket()
    ticket.generate_results()
    print(f"Lottery numbers: {ticket.get_result()}")
    print(ticket.check_games())

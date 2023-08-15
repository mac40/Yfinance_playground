from lib import Orchestrator


def main(
    orchestrator: Orchestrator,
) -> None:
    user_input = ""

    while user_input.lower() not in ["exit", "stop", "quit", "break"]:
        user_input = input("What do you want to do?\n")
        if user_input == "help":
            print(
                "list\n"
                "add <stock>\n"
                "remove <stock>\n"
                "plot <stock>\n"
            )
        elif user_input == "list":
            print(op.available_stocks())
        elif user_input[:3].lower() == "add":
            op.add_stock(user_input[4:])
        elif user_input[:6].lower() == "remove":
            op.remove_stock(user_input[7:])
        elif user_input[:4].lower() == "plot":
            period = input("Time period? (1mo, 3mo, 6mo, 1y)\n")
            op.plot_stock(user_input[5:], period=period)
        elif user_input not in ["exit", "stop", "quit", "break"]:
            print("Wrong Input")


if __name__ == "__main__":
    op = Orchestrator()
    # main(orchestrator=op)

    # op.plot_stock("^SPX")
    # op.plot_diffs_stock("^SPX")
    # op.print_adfuller("^SPX")
    # op.print_adfuller("^SPX", diff_level=1)
    # op.print_adfuller("^SPX", diff_level=2)
    # op.plot_acf("^SPX", diff_level=2)
    # op.plot_pacf("^SPX", diff_level=2)
    # op.test_model("^SPX", 2, 2, 1, period="6mo")
    op.predict("^SPX", 2, 2, 1, future=365, period='1y')

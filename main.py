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
    # op.evaluate_hyperparameters("^SPX")
    # op.test_model("^SPX", 10, 0, 1, period='1y')
    # op.plot_prediction("^SPX", 10, 0, 1, future=30, period='1y')

    # op.plot_stock("NVDA")
    # op.plot_diffs_stock("NVDA")
    # op.print_adfuller("NVDA")
    # op.print_adfuller("NVDA", diff_level=1)
    # op.print_adfuller("NVDA", diff_level=2)
    # op.plot_acf("NVDA", diff_level=2)
    # op.plot_pacf("NVDA", diff_level=2)
    # op.evaluate_hyperparameters("NVDA")
    # op.test_model("NVDA", 6, 0, 1, period='3mo', test_size=2)
    # op.plot_prediction("NVDA", 1, 1, 1, future=30, period='1y')

    # op.plot_stock("MSFT")
    # op.plot_diffs_stock("MSFT")
    # op.print_adfuller("MSFT")
    # op.print_adfuller("MSFT", diff_level=1)
    # op.print_adfuller("MSFT", diff_level=2)
    # op.plot_acf("MSFT", diff_level=1)
    # op.plot_pacf("MSFT", diff_level=1)
    # op.evaluate_hyperparameters("MSFT", period="1y")
    # op.test_model("MSFT", 8, 2, 1, period='1y', test_size=14)
    op.plot_prediction("MSFT", 8, 2, 1, future=14, period='1y')

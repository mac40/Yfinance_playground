from lib import Orchestrator


if __name__ == "__main__":
    op = Orchestrator()
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

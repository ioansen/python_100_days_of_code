import sys
import os

bids = {}

def render_start_banner():
    print("Welcome, welcome!\nWelcome to the silent auction program!")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_player():
    player = input("What is your name?:\n")
    bid = int(input("And what would be your bid sir?: RON"))
    
    bids[player] = bid


def announce_winner(bids: dict[str, int]) -> None:
    winner, amount = max(bids.items(), key=lambda kv: kv[1])
    print(f"The winner is {winner} with {amount} RON. Pay up son!")


def main():
    render_start_banner()

    while True:
        add_player()
        if input("Other bidders? yes/no: ").strip().lower() != 'yes':
            break
        clear()

    announce_winner(bids)


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        sys.exit("\n\n👋  Exiting Silent Auction.")
import sys

cypher = lambda t,s: ''.join(chr((ord(c)-97+s)%26+97) if c.islower() else chr((ord(c)-65+s)%26+65) if c.isupper() else c for c in t)
decode = lambda t,s: ''.join(chr((ord(c)-97-s)%26+97) if c.islower() else chr((ord(c)-65-s)%26+65) if c.isupper() else c for c in t)


def render_start_banner():
    print("Welcome, welcome!\nWelcome to CAESAR CIPHER!")

def play_once():
    opt   = input("Type 'encode' to encrypt or 'decode' to decrypt: ").strip().lower()

    action = {'encode': cypher, 'decode': decode}.get(opt)
    if not action:
        print("❌  Invalid choice."); return
    
    text  = input("Your message: ")
    shift = int(input("Shift number: "))
    
    print("Here is the new text:", action(text, shift))



def main() -> None:
    render_start_banner()
    while True:
        play_once()
        if input("Go again? [y/N] ").lower() != "y":
            print("Bye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        sys.exit("\n\n👋  Exiting Caesar Cipher.")
    
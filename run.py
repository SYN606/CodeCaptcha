import argparse
from colorama import Fore, Style
from functions.gen_captcha import generate_captcha

# ASCII Art with Color
ASCII_ART = f"""{Fore.CYAN}

 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓███████▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓████████▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▒░   ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░

{Style.RESET_ALL}"""

# Function to print help menu
def print_help():
    help_text = f"""
{Fore.YELLOW}Usage:{Style.RESET_ALL}
  python run.py --gen-captcha [--hard]   {Fore.GREEN}# Generate a CAPTCHA (use --hard for distortion){Style.RESET_ALL}
  python run.py --solve <image_path>     {Fore.GREEN}# Solve a CAPTCHA from an image{Style.RESET_ALL}
  python run.py --help                   {Fore.GREEN}# Show this help menu{Style.RESET_ALL}
    """
    print(help_text)

def main():
    print(ASCII_ART)  # Print colored ASCII title

    parser = argparse.ArgumentParser(
        description="CodeCaptcha: A simple CAPTCHA generator & solver",
        add_help=False  # Disable default help to use our custom one
    )

    parser.add_argument("--gen-captcha", action="store_true", help="Generate a CAPTCHA")
    parser.add_argument("--hard", action="store_true", help="Make the CAPTCHA harder with distortions")
    parser.add_argument("--solve", type=str, help="Solve a given CAPTCHA image")
    parser.add_argument("--help", action="store_true", help="Show help menu")

    args = parser.parse_args()

    if args.help:
        print_help()
    elif args.gen_captcha:
        generate_captcha(hard=args.hard)
    else:
        print_help()  # Show help if no valid command is given

if __name__ == "__main__":
    main()


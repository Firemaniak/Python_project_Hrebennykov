# User Interface Module

# Styles
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

# Standard colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
BLACK = "\033[30m"
RED = "\033[31m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"

# Bright colors
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Reset
RESET = "\033[0m"


def show_welcome() -> None:

    """
    Display the welcome message and application description.
    """

    print(f"""{CYAN}{BRIGHT_BLACK}
                               ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{BRIGHT_RED}₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪۞{RESET} WELCOME TO KOZAK_PRODUCTION {BRIGHT_RED}۞₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪{RESET}
                        {BRIGHT_BLACK}       ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ {RESET}
{RESET}
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {ITALIC}{BRIGHT_WHITE}In this console application, you can find the perfect movie for any mood or taste.                      ┃
┃                                                                                                         ┃
┃   You can search for movies in several ways:                                                            ┃
┃   1. {UNDERLINE}By keyword search{RESET} {BRIGHT_WHITE}                                                                                 ┃
┃   2. {UNDERLINE}By genre{RESET}      {BRIGHT_WHITE}                                                                                     ┃
┃   3. {UNDERLINE}By release year range{RESET} {BRIGHT_WHITE}                                                                             ┃
┃                                                                                                         ┃
┃   You can also discover what other users are searching for                                              ┃
┃   with our popular search statistics.{RESET}                                                                   ┃
┃                                                                                                         ┃
┃   {YELLOW}--- Enter {RESET}{BRIGHT_BLUE}1{RESET}{YELLOW} to search by keyword   {RESET}                                                                   ┃
┃   {YELLOW}--- Enter {RESET}{BRIGHT_BLUE}2{RESET}{YELLOW} to view all genres  {RESET}                                                                      ┃
┃   {YELLOW}--- Enter {BRIGHT_BLUE}3{RESET}{YELLOW} to search by release year range   {RESET}                                                        ┃
┃   {YELLOW}--- Enter {BRIGHT_BLUE}4{RESET}{YELLOW} to show popular searches    {RESET}                                                              ┃
┃   {YELLOW}--- Enter {BRIGHT_BLUE}0{RESET}{YELLOW} to exit the program{RESET}                                                                       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   """)


def show_menu() -> None:

    """
    Display the main menu with available user options.
    """

    print(f"""{GREEN}
                       {BRIGHT_BLACK}      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{BRIGHT_RED}₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪۞{RESET} MOVIE SEARCH APP {BRIGHT_RED}۞₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪{RESET}
                   {BRIGHT_BLACK}          ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}

{BRIGHT_BLUE}1.{RESET} {BRIGHT_WHITE}Search movies by keyword 
{BRIGHT_BLUE}2.{RESET} {BRIGHT_WHITE}View all genres
{BRIGHT_BLUE}3.{RESET} {BRIGHT_WHITE}Search by genre and year range
{BRIGHT_BLUE}4.{RESET} {BRIGHT_WHITE}View popular searches
{BRIGHT_BLUE}0.{RESET} {BRIGHT_WHITE}Exit (⊃｡•́‿•̀｡)⊃
""")


#-----------------------------------------------------------------------------------------------------------------------

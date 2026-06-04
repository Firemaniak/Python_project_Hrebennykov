import ui_module
from select_options import select_options
from animation import loading_animation

# -----------------------------------------------------------------------------------------------------------------------

def main() -> None:

    """
    Run the movie search console application.
    """

    loading_animation()
    ui_module.show_welcome()

    is_running = True

    while is_running:
        ui_module.show_menu()
        is_running = select_options()

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------


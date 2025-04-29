import os
os.system("title Console Calculator App")
def clear_window():
    os.system("cls")

def print_title(string):
    clear_window()
    print(("-")*50)
    print(f"\t{string}")
    print(("-")*50)
    print("\n")

while (True):
    print_title("Welcome to \"Console Calculator App\"")
    print(
        "",
        "0. Input Resualt",
        "\n",
        "1. Sum",
        "\n",
        "2. Miness"
        "\n",
        "3. Multipile"
        "\n",
        "4. Division"
    )
    print("\n")
    command = input("Please write command num: ")
    match command:

        case "0":
            print_title("Welcome to \"Input Resualt Command\"")
            calculate_str = input("Please import your calculate string: ")
            calculate_resualt = eval(calculate_str, { "__builtins__": None }, {})
            print(f"Your sums resualts is {calculate_resualt}")
            input("")

        case "1":
            print_title("Welcome to \"Sum Command\"")
            sum_resualt = 0
            while (True):
                sum = float(input("Please import your number: "))
                sum_resualt += sum

                exit_str = input("Do you want to continue? (y/n)")
                if exit_str != "y":
                    break

            print(f"Your sums resualts is {sum_resualt}")
            input("")

        case "2":
            print_title("Welcome to \"Miness Command\"")
            miness_resualt = None
            while (True):
                miness = float(input("Please import your number: "))
                if miness_resualt is None:
                    miness_resualt = miness
                    
                else:
                    miness_resualt -= miness

                exit_str = input("Do you want to continue? (y/n)")
                if exit_str != "y":
                    break

            print(f"Your Minesss resualts is {miness_resualt}")
            input("")

        case "3":
            print_title("Welcome to \"Multipile Command\"")
            multipile_resualt = 1
            while (True):
                multipile = float(input("Please import your number: "))
                multipile_resualt *= multipile

                exit_str = input("Do you want to continue? (y/n)")
                if exit_str != "y":
                    break

            print(f"Your Multipile resualts is {multipile_resualt}")
            input("")

        case "4":
            print_title("Welcome to \"Division Command\"")
            division_resualt = None
            while (True):
                division = float(input("Please import your number: "))

                if division_resualt is None:
                    division_resualt = division

                else:
                    division_resualt /= division

                exit_str = input("Do you want to continue? (y/n)")
                if exit_str != "y":
                    break

            print(f"Your Division resualts is {division_resualt}")
            input("")

        case "exit":
            break
        case "cancel":
            break
        case "c":
            break
        case "n":
            break

        case _:
            continue


"""
    @copyright 
        Sobhan-SRZA (mr.sinre)
    
    https://hycom.ir - My team project website

    https://srza.ir - My websie

    https://github.com/Sobhan-SRZA - My github

    https://github.com/Persian-Caesar - My team github
"""
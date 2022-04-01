#!/usr/bin/env python3
# Created by Marc Coffi
# Created in March 2022
# This program calculates the area and perimeter of a icosagon


import math
import colorama
from colorama import Fore, Style

colorama.init()


def main():
    while True:
        print(
            Fore.BLUE + Style.BRIGHT + "This program calculates the area and perimeter of a Icosagon"
        )

        # Ask user to enter a side length and choose unit
        try:
            side_length = int(input("Enter a side length :"))
        except ValueError:
            print("This is not a proper number, please try again\n")
            continue

        print("\nChoose the unit.\n\n0 - Kilometers\n1 - Meters\n2 - Centimeters\n3 - Milimeters\n")

        unit = input("\nEnter the number associated with the unit you want: ")

        # Calculate the area of a Icosagon
        Area = (
            5
            * (side_length**2)
            * (1 + (math.sqrt(5) + (math.sqrt(5 + 2 * (math.sqrt(5))))))
        )

        # Calculate the perimeter of a Icosagon
        Perimeter = side_length * 20

        if unit == "0":
            # Display result to user
            print(
                "The area is {:.2f}km^2, and the perimeter is {:.2f}km".format(
                    Area, Perimeter
                )
            )
            back = input("\nGo back to the start? (y/n) ")
            # Going back to the start or exiting the program
            if back == "y":
                continue
            else:
                print("Goodbye!")
                break
        elif unit == "1":
            # Display result to user
            print(
                "The area is {:.2f}m^2, and the perimeter is {:.2f}m".format(
                    Area, Perimeter
                )
            )
            back = input("\nGo back to the start? (y/n) ")
            # Going back to the start or exiting the program
            if back == "y":
                continue
            else:
                print("Goodbye!")
                break
        elif unit == "2":
            # Display result to user
            print(
                "The area is {:.2f}cm^2, and the perimeter is {:.2f}cm".format(
                    Area, Perimeter
                )
            )
            back = input("\nGo back to the start? (y/n) ")
            # Going back to the start or exiting the program
            if back == "y":
                continue
            else:
                print("Goodbye!")
                break
        elif unit == "3":
            # Display result to user
            print(
                "The area is {:.2f}mm^2, and the perimeter is {:.2f}mm".format(
                    Area, Perimeter
                )
            )
            # Going back to the start or exiting the program
            back = input("\nGo back to the start? (y/n) ")

            if back == "y":
                continue
            else:
                print("Goodbye!")
                break
        # Handling invalid options
        else:
            print("\nInvalid option!\n")
            continue

        print("Press 1 to go back to the start or 0 to leave the program : ")


if __name__ == "__main__":
    main()

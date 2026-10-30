#!/usr/bin/env python3
# Created by: Joyceline
# Created on: Oct 29 2026
# This program asks the user for a year and determines if it is a leap year.


def main():
    # Get user_input from user as a string
    year_user_input_as_string = input("Enter a year: ")

    try:
        user_input_int = int(year_user_input_as_string)

        if user_input_int % 4 == 0:
            if user_input_int % 100 == 0:
                if user_input_int % 400 == 0:
                    print("user_input_int is a leap year")
                else:
                    print("user_input_int is not a leap year")
            else:
                print("user_input_int is a leap year")
        else:
            print("user_input_int is not a leap year")

        # ENDIF
    except:
        print("{} is not a valid integer".format(year_user_input_as_string))


if __name__ == "__main__":
    main()

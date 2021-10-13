#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program calculates the area of a triangle


def calculate_area(base, height):
    # calculate area

    # process
    area = (base * height) / 2

    # output
    print("\nThe area of the triangle is {0} cm².".format(area))


def main():
    # this function get base and height

    # input
    base_as_string = input("Enter base of triangle (cm) : ")
    height_as_string = input("Enter height of triangle (cm) : ")
    try:
        base_from_user = float(base_as_string)
        height_from_user = float(height_as_string)
        # call function
        calculate_area(base_from_user, height_from_user)
    except Exception:
        print("\nInvalid integer entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()

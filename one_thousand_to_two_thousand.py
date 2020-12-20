# Unit4-07?usr/bin/env Python3
# This program was created by Larry nkengbeza
# THis program was created on Decemeber 2020
# This program counts from 1000-2000


def main():

    for counter in range(2002):
        if counter % 5 == 0:
            print(end=' {0} '.format(counter))
        elif counter % 6 == 0:
            print(end=' {0} '.format(counter))
        elif counter % 2 == 0:
            print(end=' {0} '.format(counter))
        elif counter % 17 == 0:
            print(end=' {0} '.format(counter))
        elif counter % 4 == 0:
            print(end=' {0} '.format(counter))


if __name__ == "__main__":
    main()

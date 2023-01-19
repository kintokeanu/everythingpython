def main():
    print("currency converter")
    print("")

    dollars = eval(input("Enter dollars: "))
    shilling = convert_to_ksh(shilling)

    print("that is ", shilling, "ksh")

convert_to_ksh = lambda shilling: shilling * 124.15
main()

def main():
    print("convert usd to ksh")
    print("")

    Dollar = eval(input("Enter USD: "))

    Dollar = convert_to_ksh(Dollar)

    print("that is", Dollar, "Ksh")

convert_to_ksh = lambda Dollar: Dollar * 124.15

    #Dollar = eval(input("Enter Ksh: "))

   # Dollar = convert_to_Dollar(Dollar)

   # print("that is", Dollar, "usd")

#convert_to_Dollar = lambda Dollar: Dollar * 124.15

main()

#ask user for delta-Y or Y-delta conversion

print("")
print("Hello 🙈")
print("")
print("This tool performs DELTA-WYE and WYE-DELTA conversions.")

ask = input("Would you like for me to perform a conversion? Enter Y for yes and N for no. ")

while(ask == "Y"):
    print("")
    print("If you would like a DELTA to WYE conversion, enter 'D'.")
    print("If you would like a WYE to DELTA conversion, enter 'W'.")
    print("")
    conversion = input("Which conversion would you like?: ")

    if(conversion == "D"):
        print("")
        r1 = float(input("Enter the real value of impedance z1: "))
        i1 = float(input("Enter the imaginary value of impedance z1: "))
        z1 = complex(r1,i1)
        print("z1:",z1)
        print("")

        r2 = float(input("Enter the real value of impedance z2: "))
        i2 = float(input("Enter the imaginary value of impedance z2: "))
        z2 = complex(r2,i2)
        print("z2:",z2)
        print("")

        r3 = float(input("Enter the real value of impedance z3: "))
        i3 = float(input("Enter the imaginary value of impedance z3: "))
        z3 = complex(r3,i3)
        print("z3:",z3)

        # add z1+z2+z3 for zd
        zd = z1 + z2 + z3
        print("")
        print("zd =",z1,"+",z2,"+",z3,"=",zd)
        print("")

        za = (z1*z3)/zd
        print("za =", za)

        zb = (z1*z2)/zd
        print("zb =", zb)

        zc = (z2*z3)/zd
        print("zc =", zc)
        print("")
        print("------------------------------------------------------")

    elif(conversion == "W"):
        print("")
        ra = float(input("Enter the real value of impedance za: "))
        ia = float(input("Enter the imaginary value of impedance za: "))
        za = complex(ra,ia)
        print("za:",za)
        print("")

        rb = float(input("Enter the real value of impedance zb: "))
        ib = float(input("Enter the imaginary value of impedance zb: "))
        zb = complex(rb,ib)
        print("zb:",zb)
        print("")

        rc = float(input("Enter the real value of impedance zc: "))
        ic = float(input("Enter the imaginary value of impedance zc: "))
        zc = complex(rc,ic)
        print("zc:",zc)
        print("")

        # calculate numerator
        zd = (za*zb)+(zb*zc)+(zc*za)
        print("zd = ", zd)
        print("")

        z1 = zd/zc
        print("z1 = ", z1)

        z2 = zd/za
        print("z2 = ", z2)

        z3 = zd/zb
        print("z3 = ", z3)
        print("")
        print("------------------------------------------------------")

    else:
        print("")
        print("------------------------------------------------------")
        print("Sorry, that is an invalid answer 😞.")
        print("------------------------------------------------------")
        print("")

    ask = input("Would you like for me to perform another conversion? Enter Y for yes and N for no. ")

if(ask == "N"):
    print("")
    print("Alright!")
    print("Have a good day.")
    print("")






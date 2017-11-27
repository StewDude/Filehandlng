

for ii in range(1,100):
#    if ii % 15 == 0:
#        output = "FizzBuzz"
#    elif ii % 5 == 0:
#        output = "Buzz"
#    elif ii % 3 == 0:
#        output = "Fizz"
#    else:
#        output = str(ii)
    output = ""

    if ii % 3 == 0:
        output = "Fizz"

    if ii % 5 == 0:
        output = output + "Buzz"

    if output == "":
        output = str(ii)

    print(output)
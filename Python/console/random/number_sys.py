

def convert(num, convert_to):
    if convert_to == "oct":
        print(oct(num))
    if convert_to == "bin":
        print(bin(num))
    if convert_to == "hex":
        print(hex(num))
    if convert_to == "all":
        print(" ", oct(num), "- in oct \n", bin(num), "- in bin \n", hex(num), "- in hex")
    
convert(344, "all")
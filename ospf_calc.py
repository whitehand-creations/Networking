
print("-"*35)
print("     OSPF CALCULATOR     ")
print("-"*35)

def ospf_calc():
    reference_bw = int(input("Reference bandwidth: "))
    interface_bw = int(input("Interface bandwidth: "))

    cost = round(reference_bw / interface_bw)
    
    print(f"Cost:{cost}")
    use_again = input("Use again? [Y/N]\nYour choice: ").upper().strip()

    if use_again != "Y":
        exit()


if __name__ == "__main__":
    while True:
        ospf_calc()
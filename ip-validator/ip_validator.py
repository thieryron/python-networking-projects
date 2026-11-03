ip = input("Enter an IP Address: ")

parts = ip.split(".")

if len(parts) != 4:
    print("Invalid")
    exit()

for part in parts:
    if not part.isdigit():
        print("Invalid")
        exit()
    if int(part) > 255:
        print("Invalid")
        exit()
print("Valid")

with open("sample.log", "rb") as f:
    data = f.read()

    print(data[:20])  # Print the first 20 bytes of the log file
    print(len(data))  # Print the total length of the log file
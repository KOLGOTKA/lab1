def hello_printer(name):
    if name:
        print(f"Hello appsec world from {name}")
    else:
        print(f"Hello appsec world from {os.uname().nodename}")

if __name__ == "__main__":
    name = input("Write your name: ")
    hello_printer(name)

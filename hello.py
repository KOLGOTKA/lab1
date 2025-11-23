import os

def hello_printer(*argc):
    if argc:
        print(f"Hello, {','.join(argc)}! Nice to meet you in AppSec world)")
    else:
        print(f"Hello, world! Nice to AppSec you)")
    print(f"I see you're working from {os.uname().nodename} today.")

if __name__ == "__main__":
    hello_printer()

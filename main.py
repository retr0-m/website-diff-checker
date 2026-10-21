
from time import sleep
from curl import fetch
from diff import format_diff, get_diff

IGNORE_PARAMETERS = []
INTERVAL_CHECK=10
URL="https://leadintellectsystem.com"
FILE ="diffs.txt"

initial=fetch(URL).splitlines()

def get_diff_from_initial(color=True):
    current=fetch(URL).splitlines()
    diff = get_diff(initial, current, ignore=IGNORE_PARAMETERS)
    if len(diff[0])==0 and len(diff[1])==0:
        return ""
    else:
        formatted = format_diff(diff, color=color)
        return formatted

def get_diff_from_previous(prev, color=True):
    current=fetch(URL).splitlines()
    diff = get_diff(prev, current, ignore=IGNORE_PARAMETERS)
    if len(diff[0])==0 and len(diff[1])==0:
        return ""
    else:
        formatted = format_diff(diff, color=color)
        return formatted

def timeout(timeout: int):
    chars=[ "-", "\\", "|", "/" ]
    for i in range(timeout):
        sleep(1)
        print(f"\r{chars[i % len(chars)]}\t({timeout - i}){'\t'*5}", end="", flush=True)
    return 

def print_to_file(txt: str, filename: str):
    with open(filename, "a") as f:
        f.write(txt)
        f.write("\n")

def main():
    print("starting")
    while True:
        prev=fetch(URL).splitlines()
        timeout(INTERVAL_CHECK)
        txt=get_diff_from_initial()
        if len(txt)>0 or txt!="":
            print("\n","="*20)
            print("Differences from initial:")
            print("="*20)
            print(txt)
            
            print_to_file("="*20, FILE)
            print_to_file("Differences from previous:", FILE)
            print_to_file(txt, FILE)
        else:
            print("initial: 0 diff\t    |\t", end="", flush=True)
            sleep(0.5)


        txt=get_diff_from_previous(prev)

        if len(txt)>0 or txt!="":
            print("\n","="*20)
            print("Differences from previous:")
            print("="*20)
            print(txt)
            
            print_to_file("="*20, FILE)
            print_to_file("Differences from previous:", FILE)
            print_to_file(txt, FILE)
        else:
            print("previous: 0 diff\t", end="", flush=True)
            sleep(0.5)

if __name__=="__main__":
    main()
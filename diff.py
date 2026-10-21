from colorama import Fore, Back, Style

def remove_ignored_lines(lines: list[str], ignore: list[str]) -> list[str]:
    filtered_lines = []
    for line in lines:
        if not any(ignored in line for ignored in ignore):
            filtered_lines.append(line)
    return filtered_lines

def get_diff(prev, current, ignore=None) -> list[list[str]]:
    adds=[]
    removes=[]

    if ignore is None:
        ignore = []

    for line in current:
        if line not in prev:
            adds.append(line)
    for line in prev:
        if line not in current:
            removes.append(line)

    removes = remove_ignored_lines(removes, ignore)
    adds = remove_ignored_lines(adds, ignore)
    return [removes, adds]

    

def format_diff(diff: list[list], color: bool) -> str:
    removes, adds = diff

    if color:
        s = ""

        s+= f"{Fore.YELLOW}Diff:\n{Style.RESET_ALL}"

        s+= f"{Fore.CYAN}Removed lines:\n{Style.RESET_ALL}"
        for line in removes:
            s += f"{Back.RED}{Fore.WHITE}- {line}{Style.RESET_ALL}\n"


        s+= f"{Fore.CYAN}Added lines:\n{Style.RESET_ALL}"
        for line in adds:
            s += f"{Back.GREEN}{Fore.WHITE}+ {line}{Style.RESET_ALL}\n"
    else:
        s = ""

        s+= f"Diff:\n"

        s+= f"Removed lines:\n"
        for line in removes:
            s += f"- {line}\n"


        s+= f"Added lines:\n"
        for line in adds:
            s += f"+ {line}\n"
    return s


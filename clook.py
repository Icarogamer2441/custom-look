import os

visual = input("type '\\n' to newlines and {dir} to directory: ").replace("\\n", "\n")

while True:
    command = input(visual.replace("{dir}", os.getcwd()))

    if command == "exit":
        break
    elif command.startswith("cd "):
        dir = "".join(command[3:])
        os.chdir(dir)
    else:
        os.system(command)

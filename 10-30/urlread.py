from urllib.request import urlopen

url = "https://raw.githubusercontent.com/halterman/124_F26/refs/heads/main/08-26/second_program.py"
#url = "https://raw.githubusercontent.com/halterman/124_F26/refs/heads/main/LICENSE"

def f() -> None:
    print("Doing evil, scary stuff")


# Open the URL and read the bytes
with urlopen(url) as response:
    raw_data = response.read()
    # Decode the bytes
    file_content = raw_data.decode("utf-8")
    print("Here's the program:")
    print(file_content)
    print("Here's what it does:")
    exec(file_content)

x = eval(input("enter an integer: "))
print(x)

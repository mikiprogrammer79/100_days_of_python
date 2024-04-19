# FileNotFound, KeyError

try:
    file = open("day30/example_data.txt")
    dict = {"key": "value"}
    print(dict["key"])

except FileNotFoundError:
    file = open("day30/example_data.txt", "w")
    file.write("Message")

except KeyError as error_message:
    print(f"Key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file closed")


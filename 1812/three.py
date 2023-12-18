file_writer = open("text.txt", "w", buffering=1)
file_reader = open("text.txt", "r")

file_writer.write("Dneska prsi. \r\n")
file_writer.write("Zitra bude taky. \r\n")


print("1.radek: " + file_reader.readline())
print("2.radek: " + file_reader.readline())
print("3.radek: " + file_reader.readline())


file_writer.close()
file_reader.close()

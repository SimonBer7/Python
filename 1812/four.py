import time

def lock():
    try:
        with open("lock.dat", "r+b") as file:
            value = file.read(1)
            if value == b'\x00':
                file.seek(0)
                file.write(b'\xFF')
                return True
            else:
                print("Running")
                return False
    except FileNotFoundError:
        with open("lock.dat", "wb") as file:
            file.write(b'\x00')
        return True

def set_default_file():
    with open("lock.dat", "r+b") as file:
        file.seek(0)
        file.write(b'\x00')

def main():
    if lock():
        try:
            print("start")
            time.sleep(10)
            print("konec")
        finally:
            set_default_file()

if __name__ == "__main__":
    main()

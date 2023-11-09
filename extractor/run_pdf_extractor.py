from gather import getData
from convert import toCsv

if __name__ == "__main__":
    data = getData("C:/Users/hbabin/Desktop/11.5.5 AICON/test.pdf", text_mode=True)
    for line in data:
        print(line)
    toCsv(data)
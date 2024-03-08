# ===================================================
# Dev file to test algorithms on a single test file
# ===================================================
# For dev testing, run :  ```python run_pdf_extractor.py``` 

from gather import getData
from convert import toCsv

if __name__ == "__main__":
    data = getData("C:/Users/hbabin/Desktop/11.5.5 AICON/test.pdf", text_mode=False)
    for line in data:
        print(line)
    toCsv(data)
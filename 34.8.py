# define the predefined list of strings
frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

try:
    # get the integer input to use as an index
    idx = int(input())

    # retrieve the string element at the specified index and output it
    frameworks_element = frameworks[idx]
    print(frameworks_element)
except IndexError:
    # handle the exception of an incompatible integer input
    print("Error")

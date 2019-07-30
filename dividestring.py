#given a string as abcabcvtabc
#divide this string by another string e.g ab
#output should be ccvtc
if __name__ == "__main__":
    str1 = "abcabcvtabc"
    str2 = "ab"
    if str1.__contains__(str2):
        x = str1.replace(str2,"")
        print(x)
    else:
        print("No String Matched")

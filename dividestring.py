if __name__ == "__main__":
    str1 = "abcabcvtabc"
    str2 = "ab"
    # op should be "de"
    if str1.__contains__(str2):
        x = str1.replace(str2,"")
        print(x)
    else:
        print("No String Matched")

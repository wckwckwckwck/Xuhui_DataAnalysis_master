def RGB_to_HEX(input1, input2, input3):
    str1 = hex(input1)
    str2 = hex(input2)
    str3 = hex(input3)

    str1 = str1[2:]
    str2 = str2[2:]
    str3 = str3[2:]
    str4 = '#' + str(str1 + str2 + str3)
    # while len(str4)<7:
    #     str4+='0'

    return str4

if __name__ == '__main__':
    R=int(input())
    G=int(input())
    B=int(input())
    print(RGB_to_HEX(R,G,B))
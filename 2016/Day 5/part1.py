import hashlib
id = "ojvtpuvg"
result = ["empty"] * 8
integer = 0
while "empty" in result:
    string = id + str(integer)
    hashed = hashlib.md5(string.encode()).hexdigest()
    if (
        hashed[0] == "0"
        and hashed[1] == "0"
        and hashed[2] == "0"
        and hashed[3] == "0"
        and hashed[4] == "0"
        and hashed[5].isdigit()
        and int(hashed[5]) < 8
        and int(hashed[5]) >= 0
        and result[int(hashed[5])] == "empty"
    ):
        result[int(hashed[5])] = hashed[6]
        print(result)

    integer += 1
print(str(result).replace(", ", '')[1:-1])

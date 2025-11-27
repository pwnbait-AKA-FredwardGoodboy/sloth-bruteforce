# Simple 3 character password list generator for bruteforce tool.
# Passwords will generate alphanumerically and include symbols and capital letters.
# Output is plaintext in a file named "pwdlist.txt" in the working directory this script is run.
#
#
# create file
with open("pwdlist.txt", "w") as pwdlist:
    # define characters
    pwd = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+`~")
    # begin nested loops to generate passwords
    # one character password
    for char1 in pwd:
        print (char1)
        print (char1, file=pwdlist)
        # two character password
        for char2 in pwd:
            print (char1,char2, sep="")
            print(char1,char2, sep="", file=pwdlist)
            # three character password
            for char3 in pwd:
                print (char1,char2,char3, sep="")
                print (char1,char2,char3, sep="", file=pwdlist)
                # four character password
                for char4 in pwd:
                    print(char1,char2,char3,char4, sep="")
                    print(char1,char2,char3,char4, sep="", file=pwdlist)
                    # five character password
                    for char5 in pwd:
                        print(char1,char2,char3,char4,char5, sep="")
                        print(char1,char2,char3,char4,char5, sep="", file=pwdlist)
                        # six character password
                        for char6 in pwd:
                            print(char1,char2,char3,char4,char5,char6, sep="")
                            print(char1,char2,char3,char4,char5,char6, sep="", file=pwdlist)
                            # seven character password
                            for char7 in pwd:
                                print(char1,char2,char3,char4,char5,char6,char7, sep="")
                                print(char1,char2,char3,char4,char5,char6,char7, sep="", file=pwdlist)
                                # eight character password
                                for char8 in pwd:
                                    print(char1,char2,char3,char4,char5,char6,char7,char8, sep="")
                                    print(char1,char2,char3,char4,char5,char6,char7,char8, sep="", file=pwdlist)
# exit script
quit()
                                    



def Lexer(file_name):
    next_char = 'x'
    read_char = True
    state = 0
    ids = []
    while (next_char):
        if read_char and len(next_char)>0:
             next_char = file_name.read(1)
             print (next_char)

        if state == 0:
            read_char = True
            if next_char == '\n' or next_char == '\t' or next_char == '\b':
                state == 0
            elif len(next_char) > 0 and ord(next_char) <=ord( 'z') and  ord(next_char) >= ord('a') :
                state = 1
            elif len(next_char) > 0 and ord(next_char) >= ord('0') and ord(next_char) <= ord('9'):
                state = 2
            elif next_char == '.':
                state = 4
            elif next_char == '\"':
                state = 5
            elif next_char == '/':
                state = 8
            elif next_char == '<':
                state = 12
            elif next_char == '>':
                state =15
            elif next_char == '=':
                state = 18
            elif next_char == '':
                break
            else:
                break

        elif state == 1:
            read_char = True

            if len(next_char) > 0 and ord(next_char) <=ord( 'z') and  ord(next_char) >= ord('a') or ord(next_char) >= ord('0') and ord(next_char) <= ord('9') or next_char == "_" :
                state = 1
            else:
                read_char = False
                ids.append("s_id")
                print("id")
                state = 0

        elif state == 2:
            read_char = True

            if len(next_char) > 0 and ord(next_char) >= ord('0') and ord(next_char) <= ord('9'):
                state = 2
            elif next_char == '.':
                state = 3
            else:
                read_char = False
                ids.append("s_no")
                print("number")
                state=0

        elif state == 3:
            read_char = True

            if len(next_char) > 0 and ord(next_char) >= ord('0') and ord(next_char) <= ord('9'):
                state = 3
            else:
                read_char = False
                ids.append("s_no")
                print("number")
                state = 0

        elif state == 4:
            read_char = True
            if len(next_char) > 0 and  next_char == '\n' or next_char == '\t' or next_char == '\b':
                state == 0
            elif ord(next_char) >= ord('0') and ord(next_char) <= ord('9'):
                state = 3
            else:
                return

        elif state == 5:
            read_char = True
            if next_char != '\"' and next_char != '\\':
                state = 5
            elif next_char == "\"":
                ids.append("s_string")
                print("string")
                state = 0
            elif next_char == "\\":
                state = 7

        elif state == 7:
            pass
            ####...................

        elif state == 8:
            read_char = True
            if next_char == "*":
                state = 9
            else:
                read_char = False
                ids.append("s_div")
                print("div")
                state = 0

        elif state == 9:
            read_char = True
            if next_char != "*":
                state = 9
            elif next_char == "*":
                state = 10

        elif state == 10:
            read_char = True
            if next_char == "*":
                state = 10
            elif next_char != "*" and next_char != "/":
                state = 9
            elif next_char == "/":
                ids.append("s_comment")
                print("comment")
                state = 0
            else:
                return

        elif state == 12:
            read_char = True

            if next_char == "=":
                ids.append("s_ge")
                print("ge")
                state = 0
            elif next_char != "=":
                read_char = False
                ids.append("s_g")
                print("g")
                state = 0

        elif state == 15:
            read_char = True
            if next_char == "=":
                ids.append("s_se")
                print("se")
                state = 0
            elif next_char != "=":
                read_char = False
                ids.append("s_s")
                print("s")
                state = 0


        elif state == 18:
            read_char = True
            if next_char == "=":
                read_char = False
                ids.append("s_e")
                print("e")
                state = 0
            else:
                read_char = False
                ids.append("s_Assign")
                print("assign")
                state = 0


    return ids


file = open("test.txt")
print(Lexer(file))


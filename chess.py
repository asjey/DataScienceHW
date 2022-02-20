chess_item = input("enter coordinate (letter number eg:a2 ): ")

if chess_item[0] in ("a" , "c" , "e" , "g") and chess_item[1] in ("1" , "3" , "5", "7"):
    print("black")
elif chess_item[0] in ("a" , "c" , "e" , "g") and chess_item[1] in ("2" , "4" , "6", "8"):
    print("white")
elif chess_item[0] in ("b" , "d" , "f" , "h") :
    if chess_item[1] in ("1" , "3" , "5", "7"):
        print("white")
    else:
        print("black")
else:
    print("enter 8x8 valid chess coordinate")

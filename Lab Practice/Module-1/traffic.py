color=input("Enter the traffic color:")
if color=='red' or color=='Red' or color=='RED':
    print("Stop your vehicle")
elif color=='yellow' or color=='Yellow'or color=='YELLOW':
    print("Stop and then go")
elif color=='green'or color=='Green' or color=='GREEN':
    print("You can go")
else:
    print("Invalid color...")
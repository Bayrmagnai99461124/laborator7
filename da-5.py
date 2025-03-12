tsag_1 = int(input("tamirchin 1-iin tsag(sec):"))
tsag_2 = int(input("tamirchin 2-iin tsag(sec):"))
tsag_3 = int(input("tamirchin 3-iin tsag(sec):"))
niit_tsag = tsag_1 + tsag_2 + tsag_3

minute = niit_tsag // 60
secund = niit_tsag % 60
print(f"niit hugatsaa: {minute:02}:{secund:02}")
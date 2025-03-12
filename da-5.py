tsag_1 = int(input())
tsag_2 = int(input())
tsag_3 = int(input())
niit_tsag = tsag_1 + tsag_2 + tsag_3

minute = niit_tsag // 60
secund = niit_tsag % 60
print(f" {minute:02}:{secund:02}")

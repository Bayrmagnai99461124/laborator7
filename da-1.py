def calculate_score(dugaar):
    if dugaar <= 100:
        bonus = 5
    elif dugaar <= 1000:
        bonus = dugaar * 0.2
    else:
        bonus = dugaar * 0.1
    additional_bonus = 0
    if dugaar % 2 == 0:
        additional_bonus += 1
    if dugaar % 10 == 5:
        additional_bonus += 2
    
    total_bonus = bonus + additional_bonus
    total_score = dugaar + total_bonus
    return bonus, additional_bonus, total_score

dugaar = int(input(" "))
bonus, additional_bonus, total_score = calculate_score(dugaar)

print(f" {bonus + additional_bonus:.2f}")
print(f" {total_score:.2f}")

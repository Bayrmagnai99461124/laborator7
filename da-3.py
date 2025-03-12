def calculate_total_cost(Uzeg, marker, nuntag):
    Uzeg_une = 5.80
    marker_une = 7.20
    nuntag_une = 1.20

    total_cost = (Uzeg * Uzeg_une) + (marker * marker_une) + (nuntag * nuntag_une)
    
    return total_cost

Uzeg = int(input())
marker = int(input())
nuntag = int(input())

total_amount = calculate_total_cost(Uzeg, marker, nuntag)

print(f" {total_amount:.3f} ")

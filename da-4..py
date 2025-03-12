NER = input(" (square, rectangle, circle, triangle):")
if NER == "square":
    side = float(input("Talin urt:"))
    area = side * side 
    print(f"{NER} {round(area, 3)}")
elif NER == "rectangle":
    length = float(input("urt:"))
    width = float(input("urgun:"))
    area = length * width
    print(f"{NER} {round(area, 3)}")
elif NER == "circle":
    radius= float(input("radius:"))
    area = 3.14 * radius * radius
    print(f"{NER} {round(area, 3)}")
elif NER == "triangle":
    base = float(input("Suurin urt:"))
    height = float(input("undur:"))
    area = 0.5 * base * height
    print(f"{NER} {round(area, 3)}")
else:
    print("buruu ug bn!")
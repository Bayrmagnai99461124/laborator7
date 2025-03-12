NER = input(" (square, rectangle, circle, triangle):")
if NER == "square":
    side = float(input())
    area = side * side 
    print(f"{NER} {round(area, 3)}")
elif NER == "rectangle":
    length = float(input())
    width = float(input())
    area = length * width
    print(f"{NER} {round(area, 3)}")
elif NER == "circle":
    radius= float(input())
    area = 3.14 * radius * radius
    print(f"{NER} {round(area, 3)}")
elif NER == "triangle":
    base = float(input())
    height = float(input())
    area = 0.5 * base * height
    print(f"{NER} {round(area, 3)}")

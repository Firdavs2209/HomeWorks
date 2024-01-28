import itertools


def uchburchak(sides):
    max_perimeter = 0
    max_triangle = None


    for x in itertools.combinations(sides, 3):
        a, b, c = x


        if a + b > c and a + c > b and b + c > a:

            perimeter = a + b + c


            if perimeter > max_perimeter:
                max_perimeter = perimeter
                max_triangle =x

    return max_triangle



n = int(input("Tayoqchalar soni (n): "))


sides = [float(input(f"{i + 1}-tayoqcha uzunligi: ")) for i in range(n)]


max_triangle = uchburchak(sides)


if max_triangle:
    print(f"Eng katta perimetrga ega bo'lgan uchburchak: {max_triangle}")
else:
    print(-1)

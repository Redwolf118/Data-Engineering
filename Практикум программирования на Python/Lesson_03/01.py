# Упражнение 1. 
# Дан список из чисел.
# Определите их НОК (наименьшее общее кратное) и НОД (наибольший общий делитель).


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

numbers = [12, 15, 20, 30]
current_gcd = numbers[0]
current_lcm = numbers[0]

for num in numbers[1:]:
    current_gcd = gcd(current_gcd, num)
    current_lcm = lcm(current_lcm, num)

print(f"НОД: {current_gcd}")
print(f"НОК: {current_lcm}")

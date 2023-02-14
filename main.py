def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        divisors = set()
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num//i)
        squared_divisors = [i**2 for i in divisors]
        sum_squares = sum(squared_divisors)
        if (int(sum_squares**0.5))**2 == sum_squares:
            result.append([num, sum_squares])
    return result
    pass

# Mandels first law

k = 0
m = 0
n = 0

value = {
    'AA+AA': 1,
    'AA+Aa': 1,
    'AA+aa': 1,
    'Aa+aa': 2/4,
    'aa+aa': 0,
    'Aa+Aa': 3/4
    }

result = 0

t = k+m+n  # total

# AA+AA
result += ((k / t) * ((k - 1) / (t - 1))) * value['AA+AA']

# AA+Aa
result += ((k / t) * (m / (t - 1))) * value['AA+Aa']

# AA+aa
result += ((k / t) * (n / (t - 1))) * value['AA+aa']

# Aa+AA
result += ((m / t) * (k / (t - 1))) * value['AA+Aa']

# Aa+Aa
result += ((m / t) * ((m - 1) / (t - 1))) * value['Aa+Aa']

# Aa+aa
result += ((m / t) * (n / (t - 1))) * value['Aa+aa']

# aa+AA
result += ((n / t) * (k / (t - 1))) * value['AA+aa']

# aa+Aa
result += ((n / t) * (m / (t - 1))) * value['Aa+aa']

# aa+aa
result += ((n / t) * ((n - 1) / (t - 1))) * value['aa+aa']

print(f'{result:.5f}')

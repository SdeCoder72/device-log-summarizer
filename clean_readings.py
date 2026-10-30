import math

def clean_readings(values):
    cleaned = []
    if values is None:
        return cleaned
    for val in values:
        if val is None or isinstance(val, bool):
            continue 
        try:
            num = float(val)
        except (TypeError, ValueError):
            continue
        if math.isnan(num) or math.isinf(num) or num < 0:
            continue 
        cleaned.append(min(num, 500.0))
    return cleaned

assert clean_readings(["12.5", None, -3, "abc", 700]) == [12.5, 500.0]
assert clean_readings([]) == []
assert clean_readings([None, "x", -1]) == []
assert clean_readings([0, True, "nan", 501]) == [0.0, 500.0]

print("All tests passed successfully!")

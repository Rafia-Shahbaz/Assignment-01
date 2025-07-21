#Takes a mixed list input: e.g. ["100", 3.14, "True", 50, "hello"]
#Use loop, type(), isinstance() to check types
#For numeric: multiply by 2
#For string: convert to uppercase
#For boolean strings: convert to actual bool
#Store results in a dictionary labeled "numeric", "text", or "other"
#Use a set to gather unique types and convert to frozenset
#Define functions: classify_type(), cast_and_operate()
#Use math.sqrt() for numeric inputs
#Use random.randint() to inject a test case
#Use datetime.now() to timestamp the result
import math
import random
from datetime import datetime
def classify_type(item):
    if isinstance(item, (int, float)):
        return "numeric"
    elif isinstance(item, str):
        if item.lower() in ['true', 'false']:
            return "other"
        return "text"
    else:
        return "other"
def cast_and_operate(item):
        if isinstance(item, (int, float)):
            result = item * 2
            sqrt_val = round(math.sqrt(item), 2) if item >= 0 else None
            return {"value": result, "sqrt": sqrt_val}
        elif isinstance(item, str):
            if item.lower() == "true":
                return {"value": True}
            elif item.lower() == "false":
                return {"value": False}
            else:
                return {"value": item.upper()}
        else:
            return {"value": item}
test_value = random.randint(1,100)
mixed_list = ["100", 3.87, "True", 50, "hello", test_value]
processed = {"numeric": [], "text": [], "other": []}
unique_types = set()
for item in mixed_list:
    if isinstance(item, str):
        try:
            item = float(item) if '.' in item else int(item)
        except ValueError:
            pass
    category = classify_type(item)
    result = cast_and_operate(item)
    processed[category].append(result)
    unique_types.add(type(item).__name__)
unique_types_fs = frozenset(unique_types)
print("\n Processed Results: ")
for key, value in processed.items():
    print(f"{key.title()}: ", value)
print("\nUnique types (frozenset): ", unique_types_fs)
print("Timestamp: ", datetime.now()) 
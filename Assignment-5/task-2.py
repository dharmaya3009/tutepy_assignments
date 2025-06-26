org_list = list(range(1,11))
print(f"Original list: {org_list}")

temp_list = org_list[0:5]
print(f"Extracted first five elements: {temp_list}")

temp_list.reverse()
print(f"Reversed extracted elements: {temp_list}")
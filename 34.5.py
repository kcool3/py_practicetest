
#Five input values.
value1 = int(input())
value2 = int(input())
value3 = int(input())
value4 = int(input())
value5 = int(input())

sum_value_int = value1 + value2 + value3 + value4 + value5
sum_value_float = float(sum_value_int)
sum_value_str = str(value1) + str(value2) + str(value3) + str(value4) + str(value5)

print("Integer: {}".format(sum_value_int))
print("Float: {:.1f}".format(sum_value_float))
print("String: {}".format(sum_value_str))
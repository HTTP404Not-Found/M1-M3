# 读取四位数
input_str = input()

# 将输入的字符串转换为整数
num = int(input_str)

# 第一步：以该位数加 7 后，除以 10 取余数取代该位数
num = ((num + 7) % 10) * 1000 + ((num // 10 + 7) % 10) * 100 + ((num // 100 + 7) % 10) * 10 + ((num // 1000 + 7) % 10)

# 第二步：将第一位数的数字与第三位数的数字对调
num = ((num // 1000) * 10 + (num // 100 % 10)) * 100 + ((num // 10 % 10) * 10 + (num % 10))

# 第三步：将第二位数的数字与第四位数的数字对调
num = ((num // 1000) * 1000 + (num % 10) * 10 + (num // 10 % 10)) + ((num // 100 % 10) * 100)

# 将加密后的整数转换为字符串并输出，最后加上换行符
output_str = str(num) + '\n'
print(output_str)

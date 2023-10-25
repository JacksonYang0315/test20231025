print("Program start here")

def caculator():
    weight = input("請輸入體重(公斤)")
    height = input("請輸入身高(公分)")
    height = int(height)/100
    BMI = int(weight)/(height*height)
    return BMI
BMI = caculator()
print("你的BMI為: " + str(BMI))

print("Program ended here")

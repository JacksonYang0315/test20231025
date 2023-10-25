# 這行是定義一個函數，名稱為calculate_bmi，接受兩個參數：weight和height。
def calculate_bmi(weight, height):
    # 這行是計算BMI的公式，體重除以身高的平方。
    bmi = weight / (height/100 * height/100)
    # 這行是返回計算出的BMI值。
    return bmi

# 這行是提示使用者輸入體重。
weight = float(input("請輸入您的體重(kg): "))
# 這行是提示使用者輸入身高。
height = float(input("請輸入您的身高(cm): "))

# 這行是呼叫上面定義的calculate_bmi函數，並將結果儲存到bmi_result變數中。
bmi_result = calculate_bmi(weight, height)

# 這行是輸出計算出的BMI值給使用者看。
print(f"您的BMI是: {bmi_result:.2f}")
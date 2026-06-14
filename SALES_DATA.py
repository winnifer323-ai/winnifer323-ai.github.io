import pandas as pd

# 讀取 Excel
df = pd.read_excel("sales_data.xlsx", header=1, nrows=10)

# 新增營收欄位
df["單日銷售額"] = df["單價"] * df["數量"]

print("========== 訂單資料 ==========")
print(df)

# 總營收
total_revenue = df["單日銷售額"].sum()

print("\n========== 計算結果 ==========")
print(f"總營收為：{total_revenue} 元")

# 熱銷商品排行
print("\n========== 熱銷商品排行 ==========")

top_products = (
    df.groupby("商品名稱")["數量"]
    .sum()
    .sort_values(ascending=False)
)

print(top_products)

# 商品類別營收
print("\n========== 商品類別銷售額 ==========")

category_revenue = (
    df.groupby("商品類別")["單日銷售額"].sum()
    .sort_values(ascending=False)
)

print(category_revenue)

# 最高營收訂單
highest_order = df.loc[df["單日銷售額"].idxmax()]

print("\n========== 最高銷售額訂單 ==========")
print(highest_order)

# 將分析結果存成新的 Excel
df.to_excel("sales_analysis_result.xlsx", index=False)

print("\n分析完成！")
print("已輸出 sales_analysis_result.xlsx")
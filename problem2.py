def find_top_seller(products: dict, sales: dict) -> str:

    sum={}
    for i in products:
        total=products[i]*sales[i]
        sum[i]=total
    
    top = max(sum, key=sum.get)

    return f"{top}: {sum[top]}"

print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))
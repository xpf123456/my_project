
import matplotlib.pyplot as plt

def print_summary(stats, module_count):
    print("🔍 关键字统计：")
    for k, v in stats.items():
        print(f"  {k}: {v} 次")

    print("\n📦 模块调用统计：")
    for m, v in module_count.items():
        print(f"  {m}: {v} 次")

def draw_chart(data_dict, title):
    labels = list(data_dict.keys())
    values = list(data_dict.values())

    plt.figure(figsize=(8, 4))
    plt.bar(labels, values, color='skyblue')
    plt.title(title)
    plt.ylabel("次数")
    plt.grid(True, axis='y')
    plt.show()

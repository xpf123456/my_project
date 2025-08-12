
from analyzer import analyze_log
from reporter import print_summary, draw_chart

if __name__ == "__main__":
    stats, module_count, events = analyze_log()

    print_summary(stats, module_count)
    draw_chart(stats, "关键字出现次数")
    draw_chart(module_count, "模块调用频率")

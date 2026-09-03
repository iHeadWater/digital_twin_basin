"""生成 lab01 的合成演示数据 rainflow_sample.csv。

仅用于演示绘图流程(时间连续、数值规整、无缺测),不是真实水文观测。
可直接运行:  python make_sample.py
依赖:无第三方库(纯标准库)。
"""

import csv
import math
import random
from datetime import date, timedelta

OUT = "rainflow_sample.csv"
START = date(2022, 1, 1)
DAYS = 730  # 约两年


def main() -> None:
    rng = random.Random(42)  # 固定种子,结果可复现

    # 逐日降雨:湿润季(6–9月)多、其它季节少的近似季节随机
    daily = []
    for i in range(DAYS):
        d = START + timedelta(days=i)
        month = d.month
        if 6 <= month <= 9:
            base = 3.0
        elif 11 <= month <= 2:
            base = 0.4
        else:
            base = 1.5
        p = max(0.0, rng.gauss(base, base * 0.9))
        daily.append((d, p))

    # 简单汇流:线性水库退水 + 降雨产流(含 1 日滞后与平滑)
    flow = 0.0
    rows = []
    for d, p in daily:
        flow = 0.92 * flow + 0.35 * p
        q = 2.0 + flow + rng.gauss(0, 0.3)
        rows.append((d.isoformat(), round(p, 2), round(max(0.0, q), 2)))

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "precip_mm", "flow_m3s"])
        w.writerows(rows)

    print(f"已生成 {OUT}: {len(rows)} 行逐日数据({START} 起)")


if __name__ == "__main__":
    main()

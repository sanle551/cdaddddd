"""Print a concise runbook summary for the monitoring spec."""

from __future__ import annotations


COLOR_MAPPING = {
    "央行政策": "蓝色",
    "股市（美股/A股）": "绿色",
    "重大公司动态": "紫色",
    "区块链（土狗）": "橙色",
    "风险/异常提醒": "红色",
}


def main() -> None:
    print("实时金融监控与通知：运行脚本说明")
    print("- 当前为规格与文档仓库，脚本输出关键配置概览。")
    print("- 目标：分钟级监控 + 自动推送通知。")
    print("\n通知颜色映射：")
    for category, color in COLOR_MAPPING.items():
        print(f"- {category}：{color}")


if __name__ == "__main__":
    main()

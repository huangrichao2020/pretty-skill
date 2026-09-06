#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抱团预警体系 · 每日扫描脚本
============================
扫描 5 维度 AI 抱团瓦解预警指标，输出触发动作建议。

用法：
  python daily_scan.py                       # 交互式输入当前指标
  python daily_scan.py --auto                # 从 westock-mcp 拉数据（待接入）
  python daily_scan.py --report 20260905     # 输出指定日期的报告

输出：
  - 控制台：5 维度当前状态 + 触发动作
  - 文件：Desktop/股市情报站/抱团预警日报/scan_YYYYMMDD.json

依赖（按 MEMORY §十五）：
  - 数据源：westock-mcp + iwencai + WebSearch（待接入）
  - 本脚本当前为骨架版，标记「手动输入」或「自动拉取」接口
"""
import argparse
import json
import os
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))

# ===== 5 维度预警指标阈值 =====
THRESHOLDS = {
    'A_pe_percentile': {
        'name': '寒武纪 PE 10年百分位',
        'warn': 75,
        'danger': 80,
        'unit': '%',
    },
    'B_ai_volume_ratio': {
        'name': 'AI 板块成交占比',
        'warn': 45,
        'danger': 50,
        'unit': '%',
    },
    'C_us10y_yield': {
        'name': '美债 10Y 收益率',
        'warn': 4.5,
        'danger': 5.0,
        'unit': '%',
    },
    'D_fed_hike_prob': {
        'name': '9月 FOMC 加息概率',
        'warn': 50,
        'danger': 70,
        'unit': '%',
    },
    'E_a_share_panic': {
        'name': 'AI 龙头单日最大跌幅',
        'warn': -8,
        'danger': -15,
        'unit': '%',
    },
}

# 触发动作矩阵
TRIGGER_ACTIONS = {
    0: '🟢 正常 · 维持当前仓位 · 关注估值',
    1: '🟡 警示 1 项 · AI 仓位减 30% · 关注其他指标',
    2: '🟠 警示 2 项 · AI 仓位减 50% · 转防御 + 启动左侧布局',
    3: '🔴 警示 3 项 · 清仓 AI · 100% 转入红利防御',
    4: '⛔ 警示 4 项 · 全部清仓 · 现金为王',
    5: '🚨 警示 5 项 · 系统性风险 · 立即撤离所有高估值',
}


def evaluate(value, threshold):
    """评估单个指标"""
    if threshold['unit'] == '%':
        # 百分比类（多数越高越坏）
        if abs(value) >= threshold['danger']:
            return 'danger'
        elif abs(value) >= threshold['warn']:
            return 'warn'
        else:
            return 'safe'
    return 'safe'


def scan(indicators):
    """
    扫描 5 维度指标，输出触发动作
    
    indicators: dict, 5 个指标的当前值
    """
    result = {
        'scan_time': datetime.now(CST).strftime('%Y-%m-%d %H:%M:%S CST'),
        'indicators': {},
        'triggered_count': 0,
        'action': '',
    }
    
    for key, threshold in THRESHOLDS.items():
        value = indicators.get(key)
        status = evaluate(value, threshold)
        is_triggered = status in ('warn', 'danger')
        result['indicators'][key] = {
            'name': threshold['name'],
            'value': value,
            'unit': threshold['unit'],
            'warn_threshold': threshold['warn'],
            'danger_threshold': threshold['danger'],
            'status': status,
            'triggered': is_triggered,
        }
        if is_triggered:
            result['triggered_count'] += 1
    
    result['action'] = TRIGGER_ACTIONS[result['triggered_count']]
    return result


def print_report(result):
    """打印报告"""
    print('=' * 60)
    print(f'  抱团预警日报 · {result["scan_time"]}')
    print('=' * 60)
    print()
    print(f'{"指标":<28}{"当前值":>10}{"警戒":>10}{"危险":>10}  状态')
    print('-' * 60)
    
    status_emoji = {'safe': '🟢', 'warn': '🟡', 'danger': '🔴'}
    for k, ind in result['indicators'].items():
        e = status_emoji[ind['status']]
        v_str = f'{ind["value"]}{ind["unit"]}' if ind['value'] is not None else 'N/A'
        w_str = f'{ind["warn_threshold"]}{ind["unit"]}'
        d_str = f'{ind["danger_threshold"]}{ind["unit"]}'
        print(f'{ind["name"]:<26}{v_str:>10}{w_str:>10}{d_str:>10}  {e}')
    
    print('-' * 60)
    print(f'\n触发指标数: {result["triggered_count"]} / 5')
    print(f'建议动作: {result["action"]}')
    print()


def save_report(result, output_dir=None):
    """保存到 JSON"""
    if output_dir is None:
        output_dir = os.path.join(os.path.expanduser('~/Desktop/股市情报站'),
                                  '抱团预警日报')
    os.makedirs(output_dir, exist_ok=True)
    date_str = datetime.now(CST).strftime('%Y%m%d_%H%M%S')
    path = os.path.join(output_dir, f'scan_{date_str}.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f'报告已保存: {path}')
    return path


def interactive_input():
    """交互式输入当前指标"""
    print('请输入当前 5 维度指标值（直接回车跳过 = 使用最新已知值）\n')
    indicators = {}
    examples = {
        'A_pe_percentile': '78',
        'B_ai_volume_ratio': '53',
        'C_us10y_yield': '4.78',
        'D_fed_hike_prob': '60',
        'E_a_share_panic': '-9.99',
    }
    for key, th in THRESHOLDS.items():
        prompt = f'  [{key}] {th["name"]}（{th["unit"]}, 警戒 {th["warn"]}, 危险 {th["danger"]}）\n  当前值 [{examples[key]}]: '
        raw = input(prompt).strip()
        if raw == '':
            raw = examples[key]
        try:
            indicators[key] = float(raw)
        except ValueError:
            indicators[key] = None
    return indicators


def main():
    parser = argparse.ArgumentParser(description='抱团预警体系 · 每日扫描')
    parser.add_argument('--auto', action='store_true', help='自动从数据源拉取（待实现）')
    parser.add_argument('--report', type=str, help='指定日期 YYYYMMDD')
    parser.add_argument('--no-save', action='store_true', help='不保存报告')
    args = parser.parse_args()
    
    if args.auto:
        print('⚠️  --auto 模式待实现：需要接入 westock-mcp + iwencai')
        print('   当前使用交互式输入')
    
    indicators = interactive_input()
    result = scan(indicators)
    print_report(result)
    if not args.no_save:
        save_report(result)


if __name__ == '__main__':
    main()
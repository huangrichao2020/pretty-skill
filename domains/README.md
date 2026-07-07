# domains/ · 一级领域类目

> **pretty-skill 的内容结构** = 一级「领域」类目 + 每个领域下的 cases

## 领域列表

| 领域 | 描述 | Cases | 状态 |
|---|---|---|---|
| [ai-training/](./ai-training/) | AI 培训课程 / 知识沉淀 / 企业内训 | 2 | ✅ 已开放 |

## 即将开放（roadmap v1）

| 领域 | 描述 |
|---|---|
| `business-pitch/` | 商业路演 / 融资 BP / 项目汇报 PPT |
| `tech-product/` | 科技产品介绍 / 功能 demo / 教程 |
| `education/` | K12 / 大学 / 培训课件 |
| `personal-brand/` | 个人 IP / 自媒体 / 简历介绍 |
| `marketing/` | 营销提案 / 品牌发布 / 活动策划 |
| `data-analysis/` | 数据分析报告 / 复盘 / 决策建议 |
| `customer-success/` | 客户成功 / 销售演示 / 案例展示 |
| `academic-research/` | 学术研究 / 论文答辩 / 课题汇报 |

## 添加新领域

```bash
mkdir domains/<your-domain>
# 复制 _template/domain-README.md.template 到新领域 README.md
cp domains/_template/case domains/<your-domain>/<your-case>
# 填内容 + 提 PR
```

详细：[CONTRIBUTING.md](../CONTRIBUTING.md)

## 领域分级规则

- **一级领域** = 一个内容分类（如「培训 / 商业 / 教育」）
- **二级子领域** = 在领域目录内可选添加
- **每个 case** = 一个独立的 PPT / 课件 / 知识沉淀

**不应**有三级结构（保持简单）。
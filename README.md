# Python Daily Exercise

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python Version">
  <img src="https://img.shields.io/github/languages/code-size/your-username/python-daily-exercise" alt="Code Size">
  <img src="https://img.shields.io/github/last-commit/your-username/python-daily-exercise" alt="Last Commit">
  <img src="https://img.shields.io/github/license/your-username/python-daily-exercise" alt="License">
</div>

## 📚 项目介绍

这是一个用于日常Python编程练习的仓库，题目来源于 [freeCodeCamp](https://www.freecodecamp.org/) 的Python课程。通过每日练习来提升Python编程技能，巩固基础知识，掌握高级特性。

## 🎯 练习目标

- 🔧 掌握Python基础语法和数据结构
- 🧠 培养算法思维和问题解决能力
- 🚀 熟悉Python标准库的使用
- 💼 为实际项目开发打下坚实基础

## 📁 项目结构

```
python-daily-exercise/
├── exercises/              # 练习题目目录 (.txt格式)
│   ├── 001_Array Diff.txt
│   ├── 002_String Reverser.txt
│   └── ...                # 更多练习题目文件
├── solutions/             # 解决方案目录 (.py格式)
│   ├── 001_Array Diff.py
│   ├── 002_String Reverser.py
│   └── ...                # 更多解决方案文件
├── tests/                 # 测试案例目录 (.json格式)
│   ├── 001_Array Diff_test_cases.json
│   ├── 002_String Reverser_test_cases.json
│   └── ...                # 更多测试案例文件
├── test_runner.py         # 测试运行器
├── requirements.txt       # 项目依赖
└── README.md             # 项目说明文件
```

## 🚀 开发环境

本项目使用 [GitHub Codespaces](https://github.com/features/codespaces) 进行开发，确保一致的开发环境。

### 本地开发设置

```bash
# 克隆仓库
git clone https://github.com/your-username/python-daily-exercise.git
cd python-daily-exercise

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

### Codespaces 开发

1. 在GitHub上打开此仓库
2. 点击绿色的 "Code" 按钮
3. 选择 "Open with Codespaces"
4. 创建新的Codespace或连接到现有的Codespace

## 📝 文件命名规范

- **题目文件**: `编号_题目名称.txt` (例如：`001_Array Diff.txt`)
- **解决方案文件**: `编号_题目名称.py` (例如：`001_Array Diff.py`)
- **测试案例文件**: `编号_题目名称_test_cases.json` (例如：`001_Array Diff_test_cases.json`)

## 🧪 测试运行

```bash
# 查看所有可用练习
python test_runner.py list

# 查看练习摘要
python test_runner.py summary

# 测试指定练习
python test_runner.py "001_Array Diff"

# 测试所有练习
python test_runner.py all
```

### 测试运行器功能

测试运行器支持以下命令：

```bash
# 显示帮助信息
python test_runner.py

# 列出所有练习
python test_runner.py list

# 显示练习摘要
python test_runner.py summary

# 测试指定练习
python test_runner.py "练习ID_题目名称"

# 测试所有练习
python test_runner.py all
```


## 🛠️ 技术栈

- **Python**: 3.8+
- **测试框架**: 自定义测试运行器
- **开发环境**: GitHub Codespaces
- **版本控制**: Git

## 📚 学习资源

- [freeCodeCamp Python Course](https://www.freecodecamp.org/learn/scientific-computing-with-python/)
- [Python官方文档](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [Python Cheatsheet](https://www.pythoncheatsheet.org/)

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个练习仓库！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- 感谢 [freeCodeCamp](https://www.freecodecamp.org/) 提供优质的免费编程课程
- 感谢所有为Python社区做出贡献的开发者们

---
<div align="center">
  <p>用代码改变世界，从每日练习开始 💻</p>
  <p>⭐ 如果这个仓库对你有帮助，请给个Star支持一下！</p>
</div>
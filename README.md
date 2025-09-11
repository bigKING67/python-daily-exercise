
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
├── exercises/              # 练习题目目录
│   ├── 001_hello_world.py
│   ├── 002_variables.py
│   ├── 003_functions.py
│   └── ...                # 更多练习文件
├── solutions/             # 参考解答目录
│   ├── 001_hello_world_solution.py
│   ├── 002_variables_solution.py
│   └── ...
├── tests/                 # 测试文件目录
│   ├── test_001_hello_world.py
│   └── ...
├── docs/                  # 文档和笔记
│   ├── python_cheatsheet.md
│   └── learning_notes.md
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

## 📝 练习规范

### 文件命名规范
- 练习文件：`编号_主题.py` (例如：`001_hello_world.py`)
- 解答文件：`编号_主题_solution.py` (例如：`001_hello_world_solution.py`)

### 代码规范
- 遵循 [PEP 8](https://pep8.org/) Python编码规范
- 每个文件开头包含题目描述和示例
- 添加必要的注释说明解题思路
- 编写测试用例验证代码正确性

### 示例模板

```python
"""
练习题目：Hello World
难度：入门级

题目描述：
编写一个函数，返回字符串 "Hello, World!"

示例：
hello_world() → "Hello, World!"
"""

def hello_world():
    # 你的代码在这里
    pass

# 测试用例
if __name__ == "__main__":
    result = hello_world()
    assert result == "Hello, World!"
    print("测试通过！")
```

## 🧪 测试运行

```bash
# 运行单个测试
python -m pytest tests/test_001_hello_world.py -v

# 运行所有测试
python -m pytest tests/ -v

# 运行特定练习文件
python exercises/001_hello_world.py
```

## 📈 学习进度跟踪

| 编号 | 主题 | 难度 | 完成状态 | 日期 |
|------|------|------|----------|------|
| 001 | Hello World | ⭐ 入门 | ✅ 已完成 | 2024-01-01 |
| 002 | Variables | ⭐ 入门 | 🔧 进行中 | 2024-01-02 |
| 003 | Functions | ⭐⭐ 初级 | 📅 待开始 | - |

## 🛠️ 技术栈

- **Python**: 3.8+
- **测试框架**: pytest
- **代码格式化**: black, flake8
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


这份README包含了完整的项目介绍、使用指南、开发规范和学习资源，非常适合你的Python日常练习仓库。你可以根据实际情况调整其中的细节，比如用户名、具体的练习内容等。

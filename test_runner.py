# test_runner.py

import json
import importlib
import sys
import os
import glob
import re
from typing import Any, Dict, List, Optional

class DailyExerciseTestRunner:
    def __init__(self, exercises_dir: str = 'exercises', solutions_dir: str = 'solutions', tests_dir: str = 'tests'):
        """初始化每日练习测试运行器"""
        self.exercises_dir = exercises_dir
        self.solutions_dir = solutions_dir
        self.tests_dir = tests_dir
        self.test_files = self.discover_test_files()
    
    def discover_test_files(self) -> Dict[str, Dict[str, str]]:
        """发现所有测试案例文件，并建立完整映射"""
        exercise_mapping = {}
        pattern = os.path.join(self.tests_dir, '*_test_cases.json')
        
        for test_file_path in glob.glob(pattern):
            filename = os.path.basename(test_file_path)
            # 从测试文件名提取练习名称 (去掉 _test_cases.json 后缀)
            exercise_name_with_id = filename.replace('_test_cases.json', '')
            
            # 分离ID和名称
            parts = exercise_name_with_id.split('_', 1)
            if len(parts) == 2:
                exercise_id = parts[0]
                exercise_name = parts[1]
            else:
                exercise_id = ""
                exercise_name = exercise_name_with_id
            
            # 查找对应的题目文件和解决方案文件
            exercise_file = None
            solution_file = None
            
            # 查找题目文件
            exercise_pattern = os.path.join(self.exercises_dir, f"{exercise_id}_{exercise_name}.txt")
            if os.path.exists(exercise_pattern):
                exercise_file = exercise_pattern
            
            # 查找解决方案文件
            solution_pattern = os.path.join(self.solutions_dir, f"{exercise_id}_{exercise_name}.py")
            if os.path.exists(solution_pattern):
                solution_file = solution_pattern
            
            exercise_mapping[exercise_name_with_id] = {
                "test_file": test_file_path,
                "exercise_file": exercise_file,
                "solution_file": solution_file,
                "exercise_id": exercise_id,
                "exercise_name": exercise_name
            }
        
        return exercise_mapping
    
    def load_test_cases(self, exercise_key: str) -> Optional[Dict]:
        """加载指定练习的测试案例"""
        if exercise_key not in self.test_files:
            return None
        
        test_file_path = self.test_files[exercise_key]["test_file"]
        try:
            with open(test_file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"❌ 错误: 无法加载测试文件 {test_file_path}: {e}")
            return None
    
    def get_available_exercises(self) -> List[str]:
        """获取所有可用的练习题目键名"""
        return list(self.test_files.keys())
    
    def show_exercise_info(self, exercise_key: str):
        """显示练习信息"""
        mapping = self.test_files[exercise_key]
        test_data = self.load_test_cases(exercise_key)
        
        if test_data:
            print(f"📋 题目: {test_data.get('exercise_name', exercise_key)}")
            print(f"🆔 ID: {test_data.get('exercise_id', mapping['exercise_id'])}")
            print(f"📝 描述: {test_data.get('description', '无描述')}")
            print(f"👨‍💻 作者: {test_data.get('author', '未知')}")
            
            if mapping['exercise_file'] and os.path.exists(mapping['exercise_file']):
                print(f"📄 题目文件: {os.path.basename(mapping['exercise_file'])}")
            else:
                print("📄 题目文件: 未找到")
                
            if mapping['solution_file'] and os.path.exists(mapping['solution_file']):
                print(f"🔧 解决方案: {os.path.basename(mapping['solution_file'])}")
            else:
                print("🔧 解决方案: 未找到")
    
    def run_single_exercise(self, exercise_key: str, solution_mode: bool = True):
        """
        运行单个练习的测试
        
        Args:
            exercise_key: 练习键名 (如 '001_Array Diff')
            solution_mode: 是否使用解决方案模式 (默认为True，因为我们主要测试解决方案)
        """
        # 加载测试案例
        test_data = self.load_test_cases(exercise_key)
        if not test_data:
            print(f"❌ 错误: 找不到 {exercise_key} 的测试案例文件")
            return False
        
        mapping = self.test_files[exercise_key]
        exercise_name = test_data.get('exercise_name', exercise_key)
        exercise_id = test_data.get('exercise_id', mapping['exercise_id'])
        
        print(f"{'='*80}")
        print(f"🚀 开始测试: {exercise_name} (ID: {exercise_id})")
        print(f"📋 题目描述: {test_data.get('description', '无描述')}")
        print(f"👨‍💻 作者: {test_data.get('author', '未知')}")
        print(f"{'='*80}")
        
        # 确定模块路径 (只测试解决方案)
        if not solution_mode:
            print("⚠️  注意: 此系统主要设计用于测试解决方案文件")
        
        if not mapping['solution_file'] or not os.path.exists(mapping['solution_file']):
            print(f"❌ 错误: 找不到解决方案文件")
            return False
        
        # 从文件路径提取模块名
        solution_file_name = os.path.basename(mapping['solution_file']).replace('.py', '')
        module_path = f"solutions.{solution_file_name.replace(' ', '_')}"
        print(f"🔧 使用解决方案: {os.path.basename(mapping['solution_file'])}")
        
        try:
            # 动态导入模块
            import importlib.util
            spec = importlib.util.spec_from_file_location(solution_file_name, mapping['solution_file'])
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception as e:
            print(f"❌ 错误: 无法导入解决方案模块 {mapping['solution_file']}")
            print(f"错误详情: {e}")
            return False
        
        function_name = test_data['function_name']
        test_cases = test_data['test_cases']
        
        # 检查函数是否存在
        if not hasattr(module, function_name):
            print(f"❌ 错误: 解决方案中没有找到函数 {function_name}")
            return False
        
        func = getattr(module, function_name)
        passed_count = 0
        total_count = len(test_cases)
        
        # 运行每个测试案例
        for i, test_case in enumerate(test_cases, 1):
            print(f"\n📝 测试 {i}/{total_count}")
            print(f"   {test_case['description']}")
            
            try:
                # 调用函数
                result = func(**test_case['input'])
                expected = test_case['expected']
                
                # 比较结果
                if result == expected:
                    print(f"   ✅ Passed")
                    passed_count += 1
                else:
                    print(f"   ❌ Failed")
                    print(f"      输入: {test_case['input']}")
                    print(f"      期望: {expected}")
                    print(f"      实际: {result}")
                    
            except Exception as e:
                print(f"   💥 Execution Error: {e}")
                print(f"      输入: {test_case['input']}")
        
        # 输出总结
        print(f"\n{'='*80}")
        print(f"📊 测试总结 - {exercise_name}:")
        print(f"   总计: {total_count}")
        print(f"   通过: {passed_count}")
        print(f"   失败: {total_count - passed_count}")
        print(f"   通过率: {passed_count/total_count*100:.1f}%")
        print(f"{'='*80}")
        
        return passed_count == total_count
    
    def run_all_exercises(self, solution_mode: bool = True):
        """运行所有练习的测试"""
        print(f"{'#'*90}")
        print(f"🚀 开始批量测试所有练习")
        print(f"{'#'*90}")
        
        exercises = self.get_available_exercises()
        if not exercises:
            print("❌ 没有找到任何练习题目")
            return
        
        results = {}
        for exercise_key in sorted(exercises):  # 按键名排序
            print(f"\n{'-'*50}")
            success = self.run_single_exercise(exercise_key, solution_mode)
            results[exercise_key] = success
            print(f"{'-'*50}")
        
        # 输出总体总结
        print(f"\n{'#'*90}")
        print(f"📊 总体测试总结:")
        print(f"{'#'*90}")
        
        total_exercises = len(exercises)
        passed_exercises = sum(1 for success in results.values() if success)
        
        for exercise_key, success in sorted(results.items()):
            mapping = self.test_files[exercise_key]
            exercise_name = mapping['exercise_name']
            status = "✅ Passed" if success else "❌ Failed"
            print(f"   {exercise_key} ({exercise_name}): {status}")
        
        print(f"\n📈 总体统计:")
        print(f"   总练习数: {total_exercises}")
        print(f"   通过练习: {passed_exercises}")
        print(f"   通过率: {passed_exercises/total_exercises*100:.1f}%")
        print(f"{'#'*90}")
    
    def show_daily_summary(self):
        """显示每日练习摘要"""
        print(f"📅 练习题目摘要")
        print(f"{'='*60}")
        
        exercises = self.get_available_exercises()
        if not exercises:
            print("❌ 没有找到任何练习题目")
            return
        
        for exercise_key in sorted(exercises):
            print(f"\n📌 {exercise_key}:")
            self.show_exercise_info(exercise_key)
            print()

def main():
    """主函数"""
    runner = DailyExerciseTestRunner()
    
    if len(sys.argv) == 1:
        # 显示帮助信息
        print("Python Daily Exercise 测试运行器")
        print("使用方法:")
        print("  python test_runner.py list                    # 列出所有练习")
        print("  python test_runner.py summary                 # 显示练习摘要")
        print("  python test_runner.py <练习ID_名称>          # 测试指定练习")
        print("  python test_runner.py all                     # 测试所有练习")
        print("\n当前可用练习:")
        for exercise_key in runner.get_available_exercises():
            mapping = runner.test_files[exercise_key]
            print(f"  - {exercise_key} ({mapping['exercise_name']})")
        return
    
    command = sys.argv[1]
    
    if command == 'list':
        print("📋 可用练习题目:")
        for exercise_key in runner.get_available_exercises():
            mapping = runner.test_files[exercise_key]
            test_data = runner.load_test_cases(exercise_key)
            if test_data:
                desc = test_data.get('description', '无描述')
                print(f"  - {exercise_key}: {desc}")
    
    elif command == 'summary':
        runner.show_daily_summary()
    
    elif command == 'all':
        runner.run_all_exercises(True)
    
    elif command in runner.get_available_exercises():
        runner.run_single_exercise(command, True)
    
    else:
        print(f"❌ 未知命令或练习: {command}")
        print("使用 'python test_runner.py list' 查看可用练习")

if __name__ == "__main__":
    main()

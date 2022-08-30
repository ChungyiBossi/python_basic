# from python_lesson_package import module_test_a
# module_test_a.print_a()

# from python_lesson_package.module_test_a import print_a
# print_a()


## 需要在 __init__.py 中先處理過後再使用
from python_lesson_package import print_a
print_a()
from student import Student
import os


# -------------------------- Task2 Self study part --------------------------
# self study: Heap, not in course
class MaxHeap:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
        self.heapify_up(len(self.data) - 1)

    def pop(self):
        if len(self.data) == 0:
            return None
        max_val = self.data[0]
        last = self.data.pop()
        if len(self.data) > 0:
            self.data[0] = last
            self.heapify_down(0)
        return max_val

    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.data[index] > self.data[parent]:
            temp = self.data[index]
            self.data[index] = self.data[parent]
            self.data[parent] = temp
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        n = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < n and self.data[left] > self.data[largest]:
                largest = left
            if right < n and self.data[right] > self.data[largest]:
                largest = right
            if largest == index:
                break
            temp = self.data[index]
            self.data[index] = self.data[largest]
            self.data[largest] = temp
            index = largest

    def get_max(self):
        if len(self.data) == 0:
            return None
        return self.data[0]


class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
        self.heapify_up(len(self.data) - 1)

    def pop(self):
        if len(self.data) == 0:
            return None
        min_val = self.data[0]
        last = self.data.pop()
        if len(self.data) > 0:
            self.data[0] = last
            self.heapify_down(0)
        return min_val

    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.data[index] < self.data[parent]:
            temp = self.data[index]
            self.data[index] = self.data[parent]
            self.data[parent] = temp
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        n = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == index:
                break
            temp = self.data[index]
            self.data[index] = self.data[smallest]
            self.data[smallest] = temp
            index = smallest

    def get_min(self):
        if len(self.data) == 0:
            return None
        return self.data[0]


# self study: Merge Sort, not in course
def merge_sort(arr, sort_type='total'):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], sort_type)
    right = merge_sort(arr[mid:], sort_type)
    return merge(left, right, sort_type)


def merge(left, right, sort_type):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if sort_type == 'chinese':
            l_val = left[i].get_chinese()
            r_val = right[j].get_chinese()
        elif sort_type == 'english':
            l_val = left[i].get_english()
            r_val = right[j].get_english()
        elif sort_type == 'math':
            l_val = left[i].get_math()
            r_val = right[j].get_math()
        else:
            l_val = left[i].get_total()
            r_val = right[j].get_total()
        if l_val > r_val:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


#here is the main function
class ScoreManager:
    def __init__(self):
        self.students = []
        self.student_file = 'studentinfo.txt'
        self.score_file = 'scores.txt'
        self.load_data()

    # load data from files
    def load_data(self):
        # read student info
        student_data = []
        if os.path.exists(self.student_file):
            f = open(self.student_file, 'r', encoding='utf-8')
            lines = f.readlines()
            f.close()
            for line in lines:
                clean = line.strip()
                if clean:
                    parts = clean.split(';')
                    # old data compatible, just simple
                    if len(parts) == 2:
                        parts.append("Default")
                    student_data.append(parts)
        # read score
        score_data = []
        if os.path.exists(self.score_file):
            f = open(self.score_file, 'r', encoding='utf-8')
            lines = f.readlines()
            f.close()
            for line in lines:
                clean = line.strip()
                if clean:
                    parts = clean.split(';')
                    if len(parts) == 4:
                        c = int(parts[1])
                        e = int(parts[2])
                        m = int(parts[3])
                        score_data.append([parts[0], c, e, m])
        # combine
        for i in range(len(student_data)):
            sid = student_data[i][0]
            name = student_data[i][1]
            class_name = student_data[i][2]
            c = 0
            e = 0
            m = 0
            for j in range(len(score_data)):
                if score_data[j][0] == sid:
                    c = score_data[j][1]
                    e = score_data[j][2]
                    m = score_data[j][3]
                    break
            stu = Student(sid, name, class_name, c, e, m)
            self.students.append(stu)

    # auto generate Sxxx ID
    def generate_auto_id(self):
        if len(self.students) == 0:
            return "S001"

        # Find max number part from existing Sxxx IDs
        max_num = 0
        for i in range(len(self.students)):
            sid = self.students[i].get_student_id()
            if sid.startswith('S'):
                num_part = sid[1:]
                if num_part.isdigit():
                    current_num = int(num_part)
                    if current_num > max_num:
                        max_num = current_num

        # New ID: S + 3 digits with leading zero
        new_num = max_num + 1
        new_id = "S{:03d}".format(new_num)
        return new_id

    # filter by class
    def filter_by_class(self, class_name):
        if class_name is None:
            return self.students
        filtered = []
        for i in range(len(self.students)):
            if self.students[i].get_class_name() == class_name:
                filtered.append(self.students[i])
        return filtered

    def search_student(self, student_id):
        for i in range(len(self.students)):
            if self.students[i].get_student_id() == student_id:
                return i
        return -1

    def get_student_info(self, index):
        return self.students[index]

    def add_student(self, student_id, name, class_name):
        pos = self.search_student(student_id)
        if pos != -1:
            return False
        stu = Student(student_id, name, class_name)
        self.students.append(stu)
        return True

    def delete_student(self, student_id):
        pos = self.search_student(student_id)
        if pos == -1:
            return False
        self.students.pop(pos)
        return True

    def update_score(self, student_id, chinese, english, math):
        pos = self.search_student(student_id)
        if pos == -1:
            return False
        if not self.students[pos].set_chinese(chinese):
            return False
        if not self.students[pos].set_english(english):
            return False
        if not self.students[pos].set_math(math):
            return False
        return True

    def print_students(self, class_name=None):
        target_students = self.filter_by_class(class_name)
        if len(target_students) == 0:
            print('No student data!')
            return
        print('----------------------------------------------------')
        print("{:<10}{:<10}{:<15}{:<10}{:<10}{:<10}{:<10}".format(
            'ID', 'Class', 'Name', 'Chinese', 'English', 'Math', 'Total'))
        print('----------------------------------------------------')
        for i in range(len(target_students)):
            stu = target_students[i]
            print("{:<10}{:<10}{:<15}{:<10}{:<10}{:<10}{:<10}".format(
                stu.get_student_id(),
                stu.get_class_name(),
                stu.get_name(),
                stu.get_chinese(),
                stu.get_english(),
                stu.get_math(),
                stu.get_total()))
        print('----------------------------------------------------')

    def print_rank(self, class_name=None, sort_type='total'):
        target_students = self.filter_by_class(class_name)
        sorted_students = merge_sort(target_students, sort_type)
        if class_name is None:
            title = 'Entire Grade'
        else:
            title = 'Class {}'.format(class_name)
        if sort_type == 'chinese':
            type_name = 'Chinese'
        elif sort_type == 'english':
            type_name = 'English'
        elif sort_type == 'math':
            type_name = 'Math'
        else:
            type_name = 'Total'

        # 动态构造表头和数据，只显示当前排名的科目成绩
        if sort_type == 'chinese':
            headers = ['Rank', 'ID', 'Class', 'Name', 'Chinese']
            get_score = lambda stu: stu.get_chinese()
        elif sort_type == 'english':
            headers = ['Rank', 'ID', 'Class', 'Name', 'English']
            get_score = lambda stu: stu.get_english()
        elif sort_type == 'math':
            headers = ['Rank', 'ID', 'Class', 'Name', 'Math']
            get_score = lambda stu: stu.get_math()
        else:
            headers = ['Rank', 'ID', 'Class', 'Name', 'Total Score']
            get_score = lambda stu: stu.get_total()

        # 格式化打印：修正列宽度，Class是10，Name是15，总宽度55
        separator = '=' * 55
        print(separator)
        print(' {} Ranking - {} '.format(title, type_name))
        print(separator)
        # 打印表头
        fmt_base = "{:<10}{:<10}{:<10}{:<15}"
        print(fmt_base.format(*headers[:4]), end='')
        print("{:<10}".format(headers[4]))
        print(separator)
        # 打印学生数据
        for i in range(len(sorted_students)):
            stu = sorted_students[i]
            row_base = [
                i + 1,
                stu.get_student_id(),
                stu.get_class_name(),
                stu.get_name()
            ]
            score = get_score(stu)
            print(fmt_base.format(*row_base), end='')
            print("{:<10}".format(score))
        print(separator)

    def get_statistics(self, class_name=None):
        target_students = self.filter_by_class(class_name)
        if len(target_students) == 0:
            return None
        c_max_heap = MaxHeap()
        c_min_heap = MinHeap()
        c_sum = 0
        c_pass = 0
        e_max_heap = MaxHeap()
        e_min_heap = MinHeap()
        e_sum = 0
        e_pass = 0
        m_max_heap = MaxHeap()
        m_min_heap = MinHeap()
        m_sum = 0
        m_pass = 0
        for i in range(len(target_students)):
            stu = target_students[i]
            c = stu.get_chinese()
            c_sum += c
            c_max_heap.push(c)
            c_min_heap.push(c)
            if c >= 60:
                c_pass += 1
            e = stu.get_english()
            e_sum += e
            e_max_heap.push(e)
            e_min_heap.push(e)
            if e >= 60:
                e_pass += 1
            m = stu.get_math()
            m_sum += m
            m_max_heap.push(m)
            m_min_heap.push(m)
            if m >= 60:
                m_pass += 1
        count = len(target_students)
        c_avg = c_sum / count
        e_avg = e_sum / count
        m_avg = m_sum / count
        c_pass_rate = c_pass / count * 100
        e_pass_rate = e_pass / count * 100
        m_pass_rate = m_pass / count * 100
        return {
            'class_name': class_name,
            'chinese': {
                'max': c_max_heap.get_max(),
                'min': c_min_heap.get_min(),
                'avg': c_avg,
                'pass_rate': c_pass_rate
            },
            'english': {
                'max': e_max_heap.get_max(),
                'min': e_min_heap.get_min(),
                'avg': e_avg,
                'pass_rate': e_pass_rate
            },
            'math': {
                'max': m_max_heap.get_max(),
                'min': m_min_heap.get_min(),
                'avg': m_avg,
                'pass_rate': m_pass_rate
            }
        }

    def print_statistics(self, class_name=None):
        stats = self.get_statistics(class_name)
        if stats is None:
            print('No student data!')
            return
        if stats['class_name'] is None:
            title = 'Entire Grade'
        else:
            title = 'Class {}'.format(stats["class_name"])
        print('==================================================')
        print(' {} Statistics '.format(title))
        print('==================================================')
        print("{:<10}{:<10}{:<10}{:<10}{:<15}".format(
            'Subject', 'Max', 'Min', 'Avg', 'Pass Rate(%)'))
        print('==================================================')
        print("{:<10}{:<10}{:<10}{:<10.2f}{:<15.1f}".format(
            'Chinese',
            stats['chinese']['max'],
            stats['chinese']['min'],
            stats['chinese']['avg'],
            stats['chinese']['pass_rate']))
        print("{:<10}{:<10}{:<10}{:<10.2f}{:<15.1f}".format(
            'English',
            stats['english']['max'],
            stats['english']['min'],
            stats['english']['avg'],
            stats['english']['pass_rate']))
        print("{:<10}{:<10}{:<10}{:<10.2f}{:<15.1f}".format(
            'Math',
            stats['math']['max'],
            stats['math']['min'],
            stats['math']['avg'],
            stats['math']['pass_rate']))
        print('==================================================')

    # save data to files
    def save_data(self):
        # save student
        f = open(self.student_file, 'w', encoding='utf-8')
        for i in range(len(self.students)):
            stu = self.students[i]
            line = "{};{};{}".format(stu.get_student_id(), stu.get_name(), stu.get_class_name())
            if i != len(self.students) - 1:
                f.write(line + '\n')
            else:
                f.write(line)
        f.close()
        # save score
        f = open(self.score_file, 'w', encoding='utf-8')
        for i in range(len(self.students)):
            stu = self.students[i]
            line = "{};{};{};{}".format(stu.get_student_id(), stu.get_chinese(), stu.get_english(), stu.get_math())
            if i != len(self.students) - 1:
                f.write(line + '\n')
            else:
                f.write(line)
        f.close()
        print('Data saved!')
import os
class SeatingPlanManager:
    def __init__(self):
        self.record = []
        self.students_num = 0
        self.rows = 0
        self.cols = 0
        self.load_file()
        self.load_setting()

    def load_file(self):
        file_is_exist = os.path.exists('studentinfo.txt')
        if file_is_exist:
            f = open('studentinfo.txt', 'r')
            all_lines = f.readlines()
            f.close()

            self.record = []
            for line in all_lines:
                clean_line = line.strip()
                student_info = clean_line.split(';')
                self.record.append(student_info)
            self.students_num = len(self.record)
        else:
            print("学生文件不存在，将创建新文件")
            self.record = []
            self.students_num = 0

    def load_setting(self):
        file_is_exist = os.path.exists('setting.txt')
        if file_is_exist:
            f = open('setting.txt', 'r')
            setting_line = f.readline()
            f.close()

            clean_line = setting_line.strip()
            setting = clean_line.split(',')
            self.rows = int(setting[0])
            self.cols = int(setting[1])
        else:
            print("设置文件不存在，默认设置为5行7列")
            self.rows = 5
            self.cols = 7
            self.change_setting(self.rows, self.cols)

    def change_setting(self, new_rows, new_cols):
        with open('setting.txt', 'w') as f:
            f.write(f'{new_rows},{new_cols}')
        self.rows = new_rows
        self.cols = new_cols

    def print_record(self):
        print('___________________________________')
        print('')
        for item in self.record:
            print(f'{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}')
        print('___________________________________')

    def search(self, name):
        for index in range(len(self.record)):
            student_item = self.record[index]
            if student_item[0] == name:
                return index
        return 'not found'

    def delete(self, name):
        row = self.search(name)
        if row != 'not found':
            self.record.pop(row)
            self.students_num -= 1
            print('============================')
            print('successfully delete')
            print('============================')
        else:
            print('============================')
            print('not found')
            print('============================')

    def append(self):
        if self.students_num >= (self.rows * self.cols):
            print('the class is full')
        else:
            print('============================')
            name = input('name:')
            height = input('height:')
            gender = input('gender(M/F):')
            shortsighted = input('shortsighted(Y/N):')
            print('============================')
            self.record.append([name, height, gender, shortsighted])
            self.students_num += 1

    def update(self):
        f = open('studentinfo.txt', 'w')
        for i in range(len(self.record)):
            item = self.record[i]
            line_content = f'{item[0]};{item[1]};{item[2]};{item[3]}'
            if i != len(self.record) - 1:
                f.write(line_content + '\n')
            else:
                f.write(line_content)
        f.close()

    def sort(self):
        self.record = sorted(self.record, key=lambda x: (x[1], -ord(x[3])))

    def print_seatingplan(self):
        print('')
        for i in range(0, self.cols):
            if i * self.rows > self.students_num:
                break
            max_seats = i * self.rows + self.rows
            if max_seats > self.students_num:
                max_seats = self.students_num

            line_content = []
            for item in self.record[i * self.rows: max_seats]:
                seat_info = f'{item[0]}({item[3]},{item[1]})'
                line_content.append(seat_info)

            for name in line_content:
                print(f'{name:^20}', end='')
            print()
        print('')

    def main_loop(self):
        while True:
            print('')
            print('code:\n 1.print \n 2.search \n 3.append \n 4.delete \n 5.setting \n 6.sort \n 7.exit')
            print('')
            code = input('input the code:')
            if code == '1':
                self.print_record()
            elif code == '2':
                name = input('input the name:')
                print('===================================')
                res = self.search(name)
                if res == 'not found':
                    print(res)
                else:
                    print(f'the name is in line {res + 1} (start by 1)')
                    print(f'{self.record[res][0]}\t{self.record[res][1]}\t{self.record[res][2]}\t{self.record[res][3]}')
                print('===================================')
            elif code == '4':
                self.print_record()
                name = input('input the name:')
                self.delete(name)
            elif code == '3':
                self.append()
            elif code == '5':
                new_rows = int(input('input the rows:'))
                new_cols = int(input('input the cols:'))
                while (new_rows * new_cols) < self.students_num:
                    print(
                        f'The new setting is too small to accommodate all current students({self.students_num}),please input again')
                    new_rows = int(input('input the rows:'))
                    new_cols = int(input('input the cols:'))
                print(f'cols:{new_cols} rows:{new_rows}')
                y = input('save your changes?(yes/no):')
                while y not in ['yes', 'no']:
                    y = input('please input again?(yes/no):')
                if y == 'yes':
                    self.change_setting(new_rows, new_cols)
                    print('saved')
                else:
                    print('unsaved')
            elif code == '6':
                self.sort()
                self.print_seatingplan()
            elif code == '7':
                x = input('save your changes?(yes/no):')
                while x not in ['yes', 'no']:
                    x = input('please input again?(yes/no):')
                if x == 'yes':
                    self.update()
                    print('saved')
                    break
                else:
                    print('unsaved')
                    break
            else:
                print('input the code again')

SeatingPlanManager().main_loop()
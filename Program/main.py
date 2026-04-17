from student_manager import ScoreManager


# Helper function for safe integer input
def input_int(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print('Invalid input! Please enter a number.')


def main():
    manager = ScoreManager()

    while True:
        print('')
        print('=== Student Score Management System ===')
        print('Menu:')
        print(' 1. Show Students')
        print(' 2. Add Student')
        print(' 3. Delete Student')
        print(' 4. Update Score')
        print(' 5. Score Ranking')
        print(' 6. Score Statistics')
        print(' 7. Save and Exit')
        print('')
        code = input('Enter your choice:')

        if code == '1':
            print('')
            print('Choose display scope:')
            print(' 1. All students')
            print(' 2. Single class students')
            c = input('Enter your choice:')
            if c == '1':
                manager.print_students(None)
            elif c == '2':
                class_name = input('Enter class name:')
                manager.print_students(class_name)
            else:
                print('Invalid input!')

        elif code == '2':
            print('============================')
            sid = input('Enter student ID:')
            name = input('Enter student name:')
            class_name = input('Enter class name(e.g. 1A):')
            print('============================')
            res = manager.add_student(sid, name, class_name)
            if res:
                print('Add success!')
            else:
                print('Student ID already exists!')

        elif code == '3':
            manager.print_students(None)
            sid = input('Enter student ID to delete:')
            pos = manager.search_student(sid)
            if pos == -1:
                print('Student not found!')
                continue
            # Confirm delete to prevent mis-deletion
            stu = manager.get_student_info(pos)
            print(f'You are going to delete: {stu.get_name()} (ID:{stu.get_student_id()})')
            confirm = input('Are you sure? (yes/no):')
            if confirm.lower() == 'yes':
                res = manager.delete_student(sid)
                if res:
                    print('Delete success!')
                else:
                    print('Delete failed!')
            else:
                print('Delete cancelled.')

        elif code == '4':
            manager.print_students(None)
            sid = input('Enter student ID to update:')
            pos = manager.search_student(sid)
            if pos == -1:
                print('Student not found!')
                continue
            print('============================')
            # Input validation
            while True:
                c = input_int('Enter Chinese score:')
                stu = manager.get_student_info(pos)
                if stu.set_chinese(c):
                    break
                else:
                    print('Score must be between 0 and 100!')

            while True:
                e = input_int('Enter English score:')
                stu = manager.get_student_info(pos)
                if stu.set_english(e):
                    break
                else:
                    print('Score must be between 0 and 100!')

            while True:
                m = input_int('Enter Math score:')
                stu = manager.get_student_info(pos)
                if stu.set_math(m):
                    break
                else:
                    print('Score must be between 0 and 100!')

            print('============================')
            res = manager.update_score(sid, c, e, m)
            if res:
                print('Update success!')
            else:
                print('Update failed!')

        elif code == '5':
            print('')
            print('Choose ranking scope:')
            print(' 1. Entire Grade')
            print(' 2. Single Class')
            c_scope = input('Enter your choice:')
            class_name = None
            if c_scope == '2':
                class_name = input('Enter class name:')
            elif c_scope != '1':
                print('Invalid input!')
                continue

            print('')
            print('Choose ranking type:')
            print(' 1. Total Score')
            print(' 2. Chinese Score')
            print(' 3. English Score')
            print(' 4. Math Score')
            c_type = input('Enter your choice:')
            sort_by = 'total'
            if c_type == '2':
                sort_by = 'chinese'
            elif c_type == '3':
                sort_by = 'english'
            elif c_type == '4':
                sort_by = 'math'
            elif c_type != '1':
                print('Invalid input!')
                continue

            manager.print_rank(class_name, sort_by)

        elif code == '6':
            print('')
            print('Choose statistics scope:')
            print(' 1. Entire Grade')
            print(' 2. Single Class')
            c = input('Enter your choice:')
            if c == '1':
                manager.print_statistics(None)
            elif c == '2':
                class_name = input('Enter class name:')
                manager.print_statistics(class_name)
            else:
                print('Invalid input!')

        elif code == '7':
            x = input('Save your changes?(yes/no):')
            while x.lower() not in ['yes', 'no']:
                x = input('Please input again?(yes/no):')
            if x.lower() == 'yes':
                manager.save_data()
                print('Saved!')
                break
            else:
                print('Unsaved changes discarded.')
                break

        else:
            print('Invalid choice, please input again!')


if __name__ == '__main__':
    main()
from student_manager import ScoreManager
# input number check
def input_int(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print('Please enter a valid number!')
#here is the main loop for calling different function
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
            #print out students' information
            print('')
            print('1. All students')
            print('2. Single class students')
            c = input('Enter your choice:')
            if c == '1':
                manager.print_students(None)
            elif c == '2':
                class_name = input('Enter class name:')
                manager.print_students(class_name)
            else:
                print('Wrong input!')
        elif code == '2':
            #add student information
            print('============================')
            # Auto generate ID, no need to input manually
            auto_id = manager.generate_auto_id()
            print('Student ID: {}'.format(auto_id))
            name = input('Enter student name:')
            class_name = input('Enter class name(e.g. 1A):')
            print('============================')
            res = manager.add_student(auto_id, name, class_name)
            if res:
                print('Add success! Student ID: {}'.format(auto_id))
            else:
                print('Student ID exists! (Auto ID may conflict, please check)')
        elif code == '3':
            #use getter to find and delete student information
            manager.print_students(None)
            sid = input('Enter student ID to delete:')
            pos = manager.search_student(sid)
            if pos == -1:
                print('Student not found!')
                continue
            stu = manager.get_student_info(pos)
            print('Will delete: {} (ID:{})'.format(stu.get_name(), stu.get_student_id()))
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
            #change score
            manager.print_students(None)
            sid = input('Enter student ID to update:')
            pos = manager.search_student(sid)
            if pos == -1:
                print('Student not found!')
                continue
            print('============================')
            # input score
            while True:
                c = input_int('Enter Chinese score:')
                stu = manager.get_student_info(pos)
                if stu.set_chinese(c):
                    break
                else:
                    print('Score must be 0-100!')
            while True:
                e = input_int('Enter English score:')
                stu = manager.get_student_info(pos)
                if stu.set_english(e):
                    break
                else:
                    print('Score must be 0-100!')
            while True:
                m = input_int('Enter Math score:')
                stu = manager.get_student_info(pos)
                if stu.set_math(m):
                    break
                else:
                    print('Score must be 0-100!')
            print('============================')
            res = manager.update_score(sid, c, e, m)
            if res:
                print('Update success!')
            else:
                print('Update failed!')
        elif code == '5':
            print('')
            print('1. Entire Grade')
            print('2. Single Class')
            c_scope = input('Enter your choice:')
            class_name = None
            if c_scope == '2':
                class_name = input('Enter class name:')
            elif c_scope != '1':
                print('Wrong input!')
                continue
            print('')
            print('1. Total Score')
            print('2. Chinese Score')
            print('3. English Score')
            print('4. Math Score')
            c_type = input('Enter your choice:')
            sort_type = 'total'
            if c_type == '2':
                sort_type = 'chinese'
            elif c_type == '3':
                sort_type = 'english'
            elif c_type == '4':
                sort_type = 'math'
            elif c_type != '1':
                print('Wrong input!')
                continue
            manager.print_rank(class_name, sort_type)
        elif code == '6':
            print('')
            print('1. Entire Grade')
            print('2. Single Class')
            c = input('Enter your choice:')
            if c == '1':
                manager.print_statistics(None)
            elif c == '2':
                class_name = input('Enter class name:')
                manager.print_statistics(class_name)
            else:
                print('Wrong input!')
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
            print('Wrong choice, input again!')
if __name__ == '__main__':
    main()
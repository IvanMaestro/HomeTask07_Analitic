import function
import menu


def button_click():
    while True:
        menu.show_menu()
        menu.decor_equals()
        choice = menu.control_menu()
        if choice == 1:
            menu.decor_equals()
            function.add_a_note(function.sum_a_note())
            menu.decor_equals()
        if choice == 2:
            menu.decor_equals()
            function.delete_entry()
            menu.decor_equals()
        if choice == 3:
            menu.decor_equals()
            function.import_format_1()
            menu.decor_equals()
        if choice == 4:
            menu.decor_equals()
            function.import_format_2()
            menu.decor_equals()
        if choice == 5:
            menu.decor_equals()
            function.export_format_1()
            menu.decor_equals()
        if choice == 6:
            menu.decor_equals()
            function.export_format_2()
            menu.decor_equals()
        if choice == 7:
            menu.decor_equals()
            function.print_list()
            menu.decor_equals()
        if choice == 8:
            menu.decor_equals()
            function.search_surname()
            menu.decor_equals()
        if choice == 9:
            menu.decor_equals()
            function.exit_program()
            menu.decor_equals()
            break
        function.back_to_menu()
        menu.decor_equals()

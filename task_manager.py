
# these two lines open the two files within the dropbox folder for both the users and the tasks, it is also opened using r+ so that the files may be editted
user_file = open("user.txt", "r+")
task_file = open("tasks.txt", "r+")


def register_user():
    # this funciton is attempting to register a user and writes to the user text file with a new username and password in the correct format so that they are readable by this code
    user_file = open("user.txt", "r+")
    user_file.read()
    user_file.write("\n")
    new_user = input("Enter a new username: ").lower()
    # this while loop tests if the new_user input is already within the userpass dictionary, if not then it breaks the loop but while the username exists the loop will ask for new username
    while True:
        if new_user in userpass:
            new_user = input("\nThis username already exists.\nEnter a new username: ")
        elif new_user not in userpass:
            break;
    user_file.write(new_user)
    user_file.write(", ")
    user_file.write(input("Enter a new password: ").lower())


def adding_task():
    # this imports the current date and time for part of the correct formatting of the task information
    import datetime
    # this task_file is read to go to the end of file and then is written in with the approapriate questions asking for information regarding the new task
    task_file = open("tasks.txt", "r+")
    task_file.read()
    task_file.write("\n")
    task_file.write(input("Enter the username of the person this task is being assigned to: ").lower())
    task_file.write(", ")
    task_file.write(input("Enter the title of the task: "))
    task_file.write(", ")
    task_file.write(input("Enter a description of the task: "))
    task_file.write(", ")
    task_file.write((datetime.datetime.now().strftime("%d %b %Y")))
    task_file.write(", ")
    task_file.write(input("Enter the due day of the task (eg. 01): "))
    task_file.write(" ")
    task_file.write(input("Enter the due month of the task (eg. Jan): ").capitalize())
    task_file.write(" ")
    task_file.write(input("Enter the due year of the task (eg. 2020): "))    
    task_file.write(", No")


def view_all_tasks():
    # this takes the tasks lines and for each line it splits them and outputs them in a specific format that is user friendly to read as an output
    task_file = open("tasks.txt", "r")
    for line in task_file.readlines():
        tasklines = ""
        tasklines += line
        tasklines += "\n"
        # this output part refreshes every line but also prints every line specific so the for loop is useful with the print function here as to print out the tasks in a readable format
        outputtasks = ""
        outputtasks = tasklines.split(", ")
        print("Assigned Task: " + outputtasks[0])
        print("Task Title: " + outputtasks[1])
        print("Task Description: " + outputtasks[2])
        print("Date Assigned: " + outputtasks[3])
        print("Date Due: " + outputtasks[4])
        print("Completed: " + outputtasks[5])

            
def view_my_tasks():
    # this creates an empty string to be added to from the for loop
    personaltasks = ""
    task_file = open("tasks.txt", "r+")
    # this for loop reads the lines of tasks, checks if the logged in user has tasks set for them and if so, prints out the tasks that are set to them in a specific format
    task_reference_number = 0
    for line in task_file.readlines():
        alltasks = []
        alltasks += line.split(", ")
        if username == alltasks[0]:
            personaltasks = ""
            personaltasks += line
            personaltasks += "\n"
            # this output part refreshes every line but also prints every line specific so the for loop is useful with the print function here as to print out the tasks in a readable format
            outputpersonal = ""
            outputpersonal = personaltasks.split(", ")
            task_reference_number += 1
            print("Task Reference Number: " + str(task_reference_number))
            print("Assigned Task: " + outputpersonal[0])
            print("Task Title: " + outputpersonal[1])
            print("Task Description: " + outputpersonal[2])
            print("Date Assigned: " + outputpersonal[3])
            print("Date Due: " + outputpersonal[4])
            print("Completed: " + outputpersonal[5])
    # this if statement is to see if no tasks available for the user
    if personaltasks == "":
        print("\nYou do not have any tasks.\n")

    # this while true continuously runs until -1 is inputted to exit into the main menu
    while True:
        # this if statement ensures that the user trying to edit tasks has atleast one task assigned to them
        if personaltasks != "":
            task_selection = input("Enter a task reference number to edit that task, or -1 to go back to main menu: ")
            if task_selection == "-1":
                break;
            # this section of code counts out a reference number that will be matched to a specific task that is assigned to a user and allows them to edit the task as either completed or to change the user assigned to it
            task_reference_number = 0
            personalselection = ""
            rewriting_task = []
            task_file = open("tasks.txt", "r+")
            for line in task_file.readlines():
                task_for_file = line.replace("\n", "")
                rewriting_task.append([task_for_file])
                alltasks = []
                alltasks += line.split(", ")
                if username == alltasks[0]:
                    task_reference_number += 1
                    if int(task_selection) == task_reference_number:
                        personalselection += line
            personalselection = personalselection.replace("\n", "")
            edittasks = personalselection.split(", ")
        
            # the above code and the below work together to edit the task that the user has selected to change, either by marking it as complete or by changing who the task is assigned to
            choose_edit = input("Would you like to edit who the task is assigned to(1) or mark the task as completed(2)? ")
            # while true means the input will keep running until a valid input is used
            while True:
                if choose_edit != "1" and choose_edit != "2" and choose_edit != "-1":
                    choose_edit = input("Please enter a valid function of either 1 to change the assginment of this task, 2 to mark this task as completed or -1 to get back to the main menu: ")
                else:
                    break;
            # this if statement edits the selected task and creates a new list of tasks that is written to task file
            if choose_edit == "2":
                edittasks[-1] = "Yes"
                string = edittasks[0] + ", " + edittasks[1] + ", " + edittasks[2] + ", " + edittasks[3] + ", " + edittasks[4] + ", " + edittasks[5]
                rewriting_task[int(task_selection)-1] = [string]
                task_file = open("tasks.txt", "w")
                for elements in rewriting_task:
                    task_file.write(elements[0])
                    task_file.write("\n")

            # this if statment edits who the task is assigned to and similarly writes it all to the task file
            if choose_edit == "1":
                newly_assign = input("Enter the new user this task is assgined to: ").lower()
                while True:
                    if newly_assign in userpass:
                        edittasks[0] = newly_assign
                        string = edittasks[0] + ", " + edittasks[1] + ", " + edittasks[2] + ", " + edittasks[3] + ", " + edittasks[4] + ", " + edittasks[5]
                        rewriting_task[int(task_selection)-1] = [string]
                        task_file = open("tasks.txt", "w")
                        for elements in rewriting_task:
                            task_file.write(elements[0])
                            task_file.write("\n")
                        break;
                    else:
                        newly_assign = input("Please enter a valid username for this task tp be assgined to: ").lower()            
            if task_selection == "-1":
                break;              


def generate_report():
    # this funciton is created to write to two files, user_overview and task_overview and generates the appropriate lines within the text files
    import datetime
    user_reports = open("user_overview.txt", "w")
    task_reports = open("task_overview.txt", "w")
    number_of_tasks = 0
    number_of_users = 0
    task_file = open("tasks.txt", "r")
    user_file = open("user.txt", "r")
    for line in task_file.readlines():
        number_of_tasks += 1
    for line in user_file.readlines():
        number_of_users += 1
    task_reports.write("The total number of tasks generated is: " + str(number_of_tasks))
    task_reports.write("\n")
    task_file = open("tasks.txt", "r+")
    uncompleted_tasks = 0
    completed_tasks = 0
    tasks_not_overdue = 0
    tasks_overdue = 0

    # this for loop runs in order to check through the lines and checks the dates to determine if the tasks are overdue or not compared to the current date
    for line in task_file.readlines():
        line = line.replace("\n", "")
        alltasks = line.split(", ")
        if alltasks[5] == "No":                                                                                 
            uncompleted_tasks += 1
        if alltasks[5] == "Yes":
            completed_tasks += 1
        currentdate = (datetime.datetime.now().strftime("%d %b %Y")).split()
        if alltasks[5] == "No":
            duedates = alltasks[4].split(" ")
            if duedates[2] >= currentdate[2]:
                if duedates[1] >= currentdate[1]:
                    if duedates[0] >= currentdate[0]:
                        tasks_not_overdue += 1
                    else:
                        tasks_overdue += 1
                else:
                    tasks_overdue += 1
            else:
                tasks_overdue += 1

    # these lines below write the calculated features of this function to the text files in a specific order and layout that is easy for the user to read
    task_reports.write("\nThe number of completed tasks is: " + str(completed_tasks))
    task_reports.write("\nThe number of uncompleted tasks is: " + str(uncompleted_tasks))
    task_reports.write("\n") 
    task_reports.write("\nThe number of tasks that are overdue and incomplete is: " + str(tasks_overdue))
    task_reports.write("\n")
    uncompleted_percentage = (uncompleted_tasks / number_of_tasks) * 100
    task_reports.write("\nThe percentage of uncompleted tasks is: " + str(round(uncompleted_percentage)) + "%")
    overdue_percentage = (tasks_overdue / number_of_tasks) * 100
    task_reports.write("\nThe percentage of overdue tasks is: " + str(round(overdue_percentage)) + "%")
    print("\nYour report has been generated into text files called task_overview.txt and user_overview.txt\n")
    user_reports.write("The total number of registered users is: " + str(number_of_users))
    user_reports.write("\nThe total number of tasks generated is: " + str(number_of_tasks) + "\n")
    task_file = open("tasks.txt", "r+")
    user_task = {}
    user_completed_tasks = {}
    user_duedate_incomplete = {}
    user_notduedate_incomplete = {}
    # the dictionaries above and the for loops below all work towards counting how many tasks are not overdue and incomplete or overdue and incomplete
    for users in userpass:
        user_duedate_incomplete[users] = 0
        user_notduedate_incomplete[users] = 0
    for line in task_file.readlines():
        line = line.replace("\n", "")
        line = line.split(", ")
        user_count = line[0]
        if user_count in user_task:
            user_task[user_count] += 1
        else:
            user_task[user_count] = 1
        for users in userpass:
            if users == line[0]:
                # this starts off the counting of having completed tasks or adding to the number of already completed tasks
                if line[5] == "Yes":
                    if users in user_completed_tasks:
                        user_completed_tasks[users] += 1
                    else:
                        user_completed_tasks[users] = 1
                # this counts the incomplete tasks and determines if they are overdue or if not overdue
                if line[5] == "No":
                    currentdate = (datetime.datetime.now().strftime("%d %b %Y")).split()
                    over_duedate = line[4].split(" ")
                    if over_duedate[2] >= currentdate[2]:
                        if over_duedate[1] >= currentdate[1]:
                            if over_duedate[0] >= currentdate[0]:
                                user_notduedate_incomplete[users] += 1
                            else:
                                user_duedate_incomplete[users] += 1
                        else:
                            user_duedate_incomplete[users] += 1
                    else:
                        user_duedate_incomplete[users] += 1
    # the below for loops with userpass are used to write to the user reports text file in a specific order and format
    for users in userpass:
        if users in user_task:
            user_reports.write("\nNumber of tasks assigned to " + users + " is: " + str(user_task[users]))
        else:
            user_reports.write("\nNumber of tasks assigned to " + users + " is: 0" )
    user_reports.write("\n")
    for users in userpass:
        if users in user_task:
            users_percentage = (user_task[users] / number_of_tasks) * 100
            user_reports.write("\nPercentage of tasks assigned to " + users + " is: " + str(round(users_percentage)) + "%")
        else:
            user_reports.write("\nPercentage of tasks assigned to " + users + " is: 0%")
    user_reports.write("\n")
    for users in userpass:
        if users in user_completed_tasks:
            percentage_completed_tasks = (user_completed_tasks[users] / user_task[users]) * 100
            user_reports.write("\nPercentage of completed tasks assigned to " + users + " is: " + str(round(percentage_completed_tasks)) + "%")
            user_reports.write("\nPercentage of tasks assigned to " + users + " still to be completed is: " + str(round(100 - percentage_completed_tasks)) + "%")
        else:
            user_reports.write("\nPercentage of completed tasks assigned to " + users + " is: 0%")
            user_reports.write("\nPercentage of tasks assigned to " + users + " still to be completed is: 100%")
    user_reports.write("\n")
    for users in userpass:
        if user_duedate_incomplete[users] != 0:
            percentage_overdue_incomplete = (user_duedate_incomplete[users] / user_task[users]) * 100
            user_reports.write("\nPercentage of tasks assigned to " + users + " that are overdue and incomplete is: " + str(round(percentage_overdue_incomplete)) + "%")
        else:
            user_reports.write("\nPercentage of tasks assigned to " + users + " that are overdue and incomplete is: 0%")

# creating a 2d list for the usernames and passwords
my_userpass_2d_list = []

# creates an empty task lines string called tasks lines

# this for loop runs through the user file and takes away the new line special function within the text file and then stores the saved line in a list by splitting ", "
for line in user_file.readlines():
    line = line.replace("\n", "")
    my_list = line.split(", ")
    # this last step adds the new list created from the line to the 2d list
    my_userpass_2d_list.append(my_list)

# an empty dictionary is created
userpass = {}

# this ensures we start at the beginning of the lists within the 2d list
i = 0

# this for loop creates the key and values within the dictionaries for each username and password within the 2d list
for items in my_userpass_2d_list:
    x = my_userpass_2d_list[i][0]
    y = my_userpass_2d_list[i][1]
    userpass[x] = y
    i +=1

# this input requests the username from the user
username = input("Enter your username: ").lower()

# this while loop runs until it is broken to ensure that the login is correctly done
while True:
    # this if statement tests whether the username is found within the dictionary and then requests a password if found otherwise requests a valid username
    if username in userpass:
        password = input("Enter your password: ").lower()
        # this if statment tests if the username and password entered is valid and stored within the dictionary, if found then prints successful login and breaks the while loop
        if userpass[username] == password:
            print("\nYou have successfully logged in.\n")
            break;
        # else statement here is if the username is valid but not the password and continues to request input of password till correct password is entered
        else:
            while True:
                password = input("Please enter the correct password: ").lower()
                # this if statment tests if the username and password entered is valid and stored within the dictionary, if found then prints successful login and breaks the while loop
                if userpass[username] == password:
                    print("\nYou have successfully logged in.\n")
                    break;
            break;
    # this else is if an invalid username is entered into the system
    else:
        username = input("Please enter a valid username: ").lower()

# this if else statment only changes the options available if the admin user is logged in
if username == "admin":
    menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nds - display statistics \ne - exit \n:").lower()
else:
    menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \ne - exit \n:").lower()


# this while loop runs unil the program is exited so that menu options can be looked at by the user within stopping    
while True:
    # this while loop ensures that only the correct input options are available
    while True:
        if menu_option != "r" and menu_option != "a" and menu_option != "va" and menu_option != "vm" and menu_option != "e" and menu_option != "ds" and menu_option != "gr":
            print("\n")
            if username == "admin":
                menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nds - display statistics \ne - exit \n:").lower()
            else:
                menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \ne - exit \n:").lower()
        else:
            break;

    # this if statment checks if the admin is logged in and selects the option of registering a user
    if username == "admin" and menu_option == "r":
        register_user()
        # once the code has been written to the text file, the menu option will appear again
        if username == "admin":
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nds - display statistics \ne - exit \n:").lower()
        else:
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \ne - exit \n:").lower()
    # this elif statment catches if the user is not the admin but attempting to register a user and then prints out an appropriate message, followed by the menu options
    elif username != "admin" and menu_option == "r":
        print("Only the admin can register new users.\n")
        if username == "admin":
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nds - display statistics \ne - exit \n:").lower()
        else:
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \ne - exit \n:").lower()

    # this if statment is for adding a task
    if menu_option == "a":
        adding_task()
        # once the new task is written in, the menu option is shown again
        if username == "admin":
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nds - display statistics \ne - exit \n:").lower()
        else:
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \ne - exit \n:").lower()

    # this menu option is for viewing all the tasks
    if menu_option == "va":
        view_all_tasks()
        # once printed, it shows the menu options again
        if username == "admin":
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nds - display statistics \ne - exit \n:").lower()
        else:
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \ne - exit \n:").lower()

    # this menu option shows personal tasks according to who is logged in at the time
    if menu_option == "vm":
        view_my_tasks()
        # this then runs the menu option after printing out the personal tasks
        if username == "admin":
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nds - display statistics \ne - exit \n:").lower()
        else:
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \ne - exit \n:").lower()

    # this runs the function generate report when gr is selected as the input
    if menu_option == "gr":
        generate_report()

        if username == "admin":
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nds - display statistics \ne - exit \n:").lower()
        else:
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \ne - exit \n:").lower()

    if username == "admin" and menu_option == "ds":

        # first this runs the generate report function
        generate_report()

        # this prints user stats for each line that is generated in both the task_overview file and the user_overview file
        task_overview = open("task_overview.txt", "r")
        user_overview = open("user_overview.txt", "r")
        user_stats = ""
        task_stats = ""
        for line in user_overview.readlines():
            line = line.replace("\n", "")
            user_stats += line
            user_stats += "\n"
        print(user_stats)
        for line in task_overview.readlines():
            line = line.replace("\n", "")
            task_stats += line
            task_stats += "\n"
        print(task_stats)
        
        # this then brings up the menu option again to allow for other options to be selected
        if username == "admin":
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nds - display statistics \ne - exit \n:").lower()
        else:
            menu_option = input("Please select one of the following options: \nr - register user (admin only) \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \ne - exit \n:").lower()
                    
    # this if statement allows for the user to quit the program and breaks the loop
    if menu_option == "e":
        quit
        break;

# these two lines close both the text files at the end of the program
user_file.close()
task_file.close()














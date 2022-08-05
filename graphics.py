import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

tkWindow = Tk()


def login():
    global login_page
    login_page = Toplevel(tkWindow)
    login_page.title("Login")
    login_page.geometry("300x250")
    # bg = PhotoImage(file = "img.png")

    global login_username
    global login_password
    global login_username_enter
    global login_password_enter
    global userid
    userid = 1
    login_username = StringVar()
    login_password = StringVar()

    Label(login_page, text="Please enter details if you already registerd").pack()
    Label(login_page, text="").pack()
    Label(login_page, text="Username:-").pack()
    login_username_enter = Entry(login_page, textvariable=login_username).pack()
    Label(login_page, text="Password:-").pack()
    login_password_enter = Entry(login_page, textvariable=login_password, show="*").pack()
    Label(login_page, text="").pack()
    Button(login_page, text="Login", width=10, height=1, bg="blue", command=exist_user).pack()


def register():
    global register_page
    register_page = Toplevel(tkWindow)
    register_page.title("Register")
    register_page.geometry("300x300")

    global userid
    global username
    global password
    global username_enter
    global password_enter
    global userid
    userid = IntVar()
    username = StringVar()
    password = StringVar()
    Label(register_page, text="Please enter User Details", bg="grey").pack()
    Label(register_page, text="").pack()
    Label(register_page, text="Userid:-").pack()
    username_enter = Entry(register_page, textvariable=userid).pack()
    Label(register_page, text="Username:-").pack()
    username_enter = Entry(register_page, textvariable=username).pack()
    Label(register_page, text="Password:-").pack()
    password_enter = Entry(register_page, textvariable=password, show="*").pack()
    Label(register_page, text="").pack()
    register_button = Button(register_page, text="Register", width=10, height=1, bg="grey", command=new_user)
    register_button.pack()


def add_product():  # #  product_id, product_name, quantity, rate
    global product_page
    product_page = Toplevel(tkWindow)
    product_page.title("product")
    product_page.geometry("300x350")

    global productid
    global productname
    global quantity
    global rate
    global productcatid
    global productuserid
    global productbrandid
    global productname_enter
    global quantity_enter
    global rate_enter
    global productid_enter
    global productcatid_enter
    global productbrandid_enter
    global productuserid_enter
    productid = IntVar()
    productcatid = IntVar()
    productuserid = IntVar()
    productbrandid = IntVar()
    productname = StringVar()
    quantity = IntVar()
    rate = IntVar()
    Label(product_page, text="Please enter Product Details", bg="grey").pack()
    Label(product_page, text="").pack()
    Label(product_page, text="Productid:-").pack()
    productid_enter = Entry(product_page, textvariable=productid).pack()
    Label(product_page, text="Product cat id:-").pack()
    productid_enter = Entry(product_page, textvariable=productcatid).pack()
    Label(product_page, text="Product user id:-").pack()
    productid_enter = Entry(product_page, textvariable=productuserid).pack()
    Label(product_page, text="Product brand id:-").pack()
    productid_enter = Entry(product_page, textvariable=productbrandid).pack()
    Label(product_page, text="Product name:-").pack()
    productname_enter = Entry(product_page, textvariable=productname).pack()
    Label(product_page, text="Quantity:-").pack()
    quantity_enter = Entry(product_page, textvariable=quantity).pack()
    Label(product_page, text="Rate:-").pack()
    rate_enter = Entry(product_page, textvariable=rate).pack()
    Label(product_page, text="").pack()
    product_button = Button(product_page, text="product", width=10, height=1, bg="grey", command=new_product)
    product_button.pack()


def order_product():
    global order_page
    order_page = Toplevel(tkWindow)
    order_page.title("order")
    order_page.geometry("300x500")

    global orderid
    global clientname
    global no_of_items
    global payment_status
    global paid
    global due
    global total
    global product_id
    global phone_no1
    global phone_no2
    global orderid_enter
    global clientname_enter
    global no_of_items_enter
    global payment_status_enter
    global paid_enter
    global due_enter
    global total_enter
    global product_id_enter
    global phone_no1_enter
    global phone_no2_enter
    orderid = IntVar()
    no_of_items = IntVar()
    clientname = StringVar()
    payment_status = StringVar()
    paid = IntVar()
    due = IntVar()
    total = IntVar()
    product_id = IntVar()
    phone_no1 = IntVar()
    phone_no2 = IntVar()
    Label(order_page, text="Please enter order Details", bg="grey").pack()
    Label(order_page, text="").pack()
    Label(order_page, text="orderid:-").pack()
    orderid_enter = Entry(order_page, textvariable=orderid).pack()
    Label(order_page, text="client name:-").pack()
    clientname_enter = Entry(order_page, textvariable=clientname).pack()
    Label(order_page, text="client Phone no 1:-").pack()
    phone_no1_enter = Entry(order_page, textvariable=phone_no1).pack()
    Label(order_page, text="client phone no 2:-").pack()
    phone_no2_enter = Entry(order_page, textvariable=phone_no2).pack()
    Label(order_page, text="no of items:-").pack()
    no_of_items_enter = Entry(order_page, textvariable=no_of_items).pack()
    Label(order_page, text="Payment status:-").pack()
    payment_status_enter = Entry(order_page, textvariable=payment_status).pack()
    Label(order_page, text="paid:-").pack()
    paid_enter = Entry(order_page, textvariable=paid).pack()
    Label(order_page, text="due:-").pack()
    due_enter = Entry(order_page, textvariable=due).pack()
    Label(order_page, text="Total:-").pack()
    total_enter = Entry(order_page, textvariable=total).pack()
    Label(order_page, text="Product id:-").pack()
    product_id_enter = Entry(order_page, textvariable=product_id).pack()
    Label(order_page, text="").pack()

    product_button = Button(order_page, text="Order", width=10, height=1, bg="grey", command=new_order)
    product_button.pack()


def add_category():  # category_id, category_name, quantity, rate
    global category_page
    category_page = Toplevel(tkWindow)
    category_page.title("category")
    category_page.geometry("300x300")

    global categoryid
    global categoryname
    global active
    global categoryname_enter
    global active_enter
    global categoryid_enter
    categoryid = IntVar()
    categoryname = StringVar()
    active = StringVar()
    Label(category_page, text="Please enter Category Details", bg="grey").pack()
    Label(category_page, text="").pack()
    Label(category_page, text="categoryid:-").pack()
    categoryid_enter = Entry(category_page, textvariable=categoryid).pack()
    Label(category_page, text="category name:-").pack()
    categoryname_enter = Entry(category_page, textvariable=categoryname).pack()
    Label(category_page, text="Active:-").pack()
    active_enter = Entry(category_page, textvariable=active).pack()
    Label(category_page, text="").pack()
    category_button = Button(category_page, text="Add", width=10, height=1, bg="grey", command=new_cat)
    category_button.pack()


def add_brand():
    global brand_page
    brand_page = Toplevel(tkWindow)
    brand_page.title("brand")
    brand_page.geometry("300x300")

    global brandid
    global brandname
    global active
    global brandname_enter
    global active_enter
    global brandid_enter
    brandid = IntVar()
    brandname = StringVar()
    active = StringVar()
    Label(brand_page, text="Please enter brand Details", bg="grey").pack()
    Label(brand_page, text="").pack()
    Label(brand_page, text="brandid:-").pack()
    brandid_enter = Entry(brand_page, textvariable=brandid).pack()
    Label(brand_page, text="brand name:-").pack()
    brandname_enter = Entry(brand_page, textvariable=brandname).pack()
    Label(brand_page, text="Active:-").pack()
    active_enter = Entry(brand_page, textvariable=active, show="*").pack()
    Label(brand_page, text="").pack()
    brand_button = Button(brand_page, text="Add", width=10, height=1, bg="grey", command=new_brand)
    brand_button.pack()


def add_contact():
    global contact_page
    contact_page = Toplevel(tkWindow)
    contact_page.title("brand")
    contact_page.geometry("300x300")

    global orderid
    global contct
    global orderid_enter
    global contct_enter
    orderid = IntVar()
    contct = IntVar()
    Label(contact_page, text="Please enter brand Details", bg="grey").pack()
    Label(contact_page, text="").pack()
    Label(contact_page, text="orderid:-").pack()
    orderid_enter = Entry(contact_page, textvariable=orderid).pack()
    Label(contact_page, text="brand name:-").pack()
    contct_enter = Entry(brand_page, textvariable=contct).pack()
    Label(contact_page, text="").pack()
    c_button = Button(contact_page, text="Add", width=10, height=1, bg="grey", command=new_contact)
    c_button.pack()


def add_department():
    global dept_page
    dept_page = Toplevel(tkWindow)
    dept_page.title("department")
    dept_page.geometry("300x300")

    global deptid
    global deptname
    global manager_id
    global deptname_enter
    global deptid_enter
    global manager_id_enter
    deptid = IntVar()
    deptname = StringVar()
    manager_id = IntVar()
    Label(dept_page, text="Please enter Department Details", bg="grey").pack()
    Label(dept_page, text="").pack()
    Label(dept_page, text="Dept id:-").pack()
    brandid_enter = Entry(dept_page, textvariable=deptid).pack()
    Label(dept_page, text="Dept name:-").pack()
    brandname_enter = Entry(dept_page, textvariable=deptname).pack()
    Label(dept_page, text="manager_id:-").pack()
    active_enter = Entry(dept_page, textvariable=manager_id, show="*").pack()
    Label(dept_page, text="").pack()
    brand_button = Button(dept_page, text="Add", width=10, height=1, bg="grey", command=new_department)
    brand_button.pack()

def add_order(): #order_id, client_name, no_of_items, payment_status, due, paid, total, product_id
    global orderpage
    orderpage = Toplevel(tkWindow)
    orderpage.title("order")
    orderpage.geometry("300x300")

    global orderid
    global client_name
    global no_of_items
    global payment_status
    global due
    global paid
    global total
    global productid
    orderid = IntVar()
    client_name = StringVar()
    no_of_items = IntVar()
    payment_status = StringVar()
    due = IntVar()
    paid = IntVar()
    total = IntVar()
    productid = IntVar()
    Label(orderpage, text="Please enter Order Details", bg="grey").pack()
    Label(orderpage, text="").pack()
    Label(orderpage, text="Order id:-").pack()
    orderid_enter = Entry(orderpage, textvariable=orderid).pack()
    Label(orderpage, text="Client name:-").pack()
    client_name_enter = Entry(orderpage, textvariable=client_name).pack()
    Label(orderpage, text="No of items:-").pack()
    items_enter = Entry(orderpage, textvariable=no_of_items, show="*").pack()
    Label(orderpage, text="Payment Status:-").pack()
    pay_enter = Entry(orderpage, textvariable=payment_status, show="*").pack()
    Label(orderpage, text="Due:-").pack()
    due_enter = Entry(orderpage, textvariable=due, show="*").pack()
    Label(orderpage, text="Paid:-").pack()
    paid_entry = Entry(orderpage, textvariable=paid, show="*").pack()
    Label(orderpage, text="Total:-").pack()
    total_entry = Entry(orderpage, textvariable=total, show="*").pack()
    Label(orderpage, text="Product Id:-").pack()
    productid_entry = Entry(orderpage, textvariable=productid, show="*").pack()
    brand_button = Button(orderpage, text="Add", width=10, height=1, bg="grey", command=new_order)
    brand_button.pack()

def add_employee():  # #  product_id, product_name, quantity, rate
    global epl_page_page
    epl_page = Toplevel(tkWindow)
    epl_page.title("product")
    epl_page.geometry("300x350")

    global empid
    global emp_first_name
    global salary
    global birthdate
    global emp_last_name
    global usr_id
    global dpt_id
    global empid_enter
    global emp_first_name_enter
    global emp_last_name_enter
    global salary_enter
    global birthdate_enter
    global usrid_enter
    global dptid_enter
    empid = IntVar()
    emp_first_name = StringVar()
    salary = IntVar()
    birthdate = StringVar()
    emp_last_name = StringVar()
    usr_id = IntVar()
    dpt_id = IntVar()
    Label(epl_page, text="Please enter Employee Details", bg="grey").pack()
    Label(epl_page, text="").pack()
    Label(epl_page, text="employee id:-").pack()
    empid_enter = Entry(epl_page, textvariable=empid).pack()
    Label(epl_page, text="Employee first name:-").pack()
    emp_first_name_enter = Entry(epl_page, textvariable=emp_first_name).pack()
    Label(epl_page, text="Employee last name:-").pack()
    emp_last_name_enter = Entry(epl_page, textvariable=emp_last_name).pack()
    Label(epl_page, text="salary:-").pack()
    salary_enter = Entry(epl_page, textvariable=salary).pack()
    Label(epl_page, text="Birthdate:-").pack()
    birthdate_enter = Entry(epl_page, textvariable=birthdate).pack()
    Label(epl_page, text="user id:-").pack()
    usrid_enter = Entry(epl_page, textvariable=usr_id).pack()
    Label(epl_page, text="department id:-").pack()
    dptid_enter = Entry(epl_page, textvariable=dpt_id).pack()
    Label(epl_page, text="").pack()
    emp_button = Button(epl_page, text="Employee", width=10, height=1, bg="grey", command=new_employee)
    emp_button.pack()


def display_list():
    global display_list
    display_list = Toplevel(login_page)
    display_list.title("Dashboard")
    display_list.geometry("565x260")
    B1 = Button(display_list, text="Users", width=20, height=3, bg="blue", command=lambda m=None: display_users())
    B2 = Button(display_list, text="Brand", width=20, height=3, bg="cyan", command=lambda m=None: display_brand())
    B3 = Button(display_list, text="Category", width=20, height=3, bg="magenta",
                command=lambda m=None: display_category())
    B4 = Button(display_list, text="Products", width=20, height=3, bg="yellow",
                command=lambda m=None: display_products())
    B5 = Button(display_list, text="Order", width=20, height=3, bg="red", command=lambda m=None: display_orders())
    B6 = Button(display_list, text="Search", width=20, height=3, bg='cyan', command=lambda m=None: search())
    B7 = Button(display_list, text="SHOW INVENTORY", width=25, height=3, bg="grey",
                command=lambda m=None: create_charts())
    B8 = Button(display_list, text="Employee", width=20, height=3, bg='cyan',
                command=lambda m=None: display_employess())
    B9 = Button(display_list, text="Department", width=20, height=3, bg="red",
                command=lambda m=None: display_department())
    B10 = Button(display_list, text="Contacts", width=20, height=3, bg="blue", command=lambda m=None: display_contact())
    B1.grid(row=1, column=0)
    B2.grid(row=1, column=1)
    B3.grid(row=1, column=2)
    B4.grid(row=2, column=0)
    B5.grid(row=2, column=1)
    B6.grid(row=2, column=2)
    B8.grid(row=3, column=0)
    B9.grid(row=3, column=1)
    B10.grid(row=3, column=2)
    B7.place(relx=0.5, rely=0.87, anchor=CENTER)

def search():
    global display_search
    display_search = Toplevel(display_list)
    display_search.title("Search Items")
    display_search.geometry("380x550")

    global username
    global username_enter
    global emp_first_name
    global emp_first_name_enter
    global product_name
    global product_name_enter
    global brand_name
    global brand_name_enter
    global category_name
    global category_name_enter

    username = StringVar()
    emp_first_name = StringVar()
    product_name = StringVar()
    brand_name = StringVar()
    category_name = StringVar()

    Label(display_search, text="Please enter Name of the entity", bg="grey").pack()
    Label(display_search, text="").pack()
    Label(display_search, text="username:-").pack()
    username_enter = Entry(display_search, textvariable=username).pack()
    Label(display_search, text="emp_first_name:-").pack()
    emp_first_name_enter = Entry(display_search, textvariable=emp_first_name).pack()
    Label(display_search, text="product name:-").pack()
    product_name_enter = Entry(display_search, textvariable=product_name).pack()
    Label(display_search, text="brand name:-").pack()
    brand_name_enter = Entry(display_search, textvariable=brand_name).pack()
    Label(display_search, text="Category name:-").pack()
    category_name_enter = Entry(display_search, textvariable=category_name).pack()
    B1 = Button(display_search, text="Brand", width=20, height=3, bg="cyan", command=lambda m=None:submit_brand())
    B2 = Button(display_search, text="Category", width=20, height=3, bg="magenta", command=lambda m=None:submit_category())
    B3 = Button(display_search, text="Products", width=20, height=3, bg="red", command=lambda m=None:submit_product())
    B4 = Button(display_search, text="Users", width=20, height=3, bg="blue", command=lambda m=None:submit_user())
    B5 = Button(display_search, text="Employee", width=20, height=3, bg="blue", command=lambda m=None:submit_employee())
    B1.pack()
    B2.pack()
    B3.pack()
    B4.pack()
    B5.pack()

def submit_user():
    usr = username.get()
    username.set("")
    print(usr)
    display_searched_users(usr)
def submit_employee():
    emp = emp_first_name.get()
    emp_first_name.set("")
    print(emp)
    display_searched_employess(emp)
def submit_product():
   prdt = product_name.get()
   product_name.set("")
   print(prdt)
   display_searched_products(prdt)
def submit_brand():
    brnd = brand_name.get()
    brand_name.set("")
    print(brnd)
    display_searched_brand(brnd)

def submit_category():
    cat = category_name.get()
    category_name.set("")
    print(cat)
    display_searched_category(cat)

def delete_brand():
    brd = Brand()
    selected_item = brand_table.selection()[0]
    brand_id = brand_table.item(selected_item)['values'][0]
    brd.remove_brands(brand_id)
    brand_table.delete(selected_item)


def delete_category():
    cat = Category()
    selected_item = category_table.selection()[0]
    cat_id = category_table.item(selected_item)['values'][0]
    cat.remove_category(cat_id)
    category_table.delete(selected_item)


def delete_product():
    p = Product()
    selected_item = product_table.selection()[0]
    p_id = product_table.item(selected_item)['values'][0]
    p.remove_product(p_id)
    product_table.delete(selected_item)


def delete_order():
    o = Order()
    selected_item = order_table.selection()[0]
    o_id = order_table.item(selected_item)['values'][0]
    o.remove_order(o_id)
    order_table.delete(selected_item)


def delete_department():
    d = Department()
    selected_item = dept_table.selection()[0]
    d_id = dept_table.item(selected_item)['values'][0]
    d.remove_department(d_id)
    dept_table.delete(selected_item)


def delete_employee():
    e = Employee()
    selected_item = emp_table.selection()[0]
    e_id = emp_table.item(selected_item)['values'][0]
    e.remove_employee(e_id)
    emp_table.delete(selected_item)


def delete_contact():
    c = Contact()
    selected_item = contact_table.selection()[0]
    con = emp_table.item(selected_item)['values'][1]
    c.remove_contact(con)
    contact_table.delete(selected_item)


def create_charts():
    global inventory_page
    inventory_page = Toplevel(display_list)
    inventory_page.title("inventory")
    inventory_page.geometry("400x300")
    user = USER()
    emp = Employee()
    prdt = Product()
    brnd = Brand()
    cat = Category()

    global x1
    global x2
    global x3
    global x4
    global x5
    global pie2

    pc = prdt.distinct_product()
    uc = user.distinct_users()
    ec = emp.distinct_employees()
    bc = brnd.distinct_brand()
    cc = cat.distinct_category()

    x1 = uc[0][0]
    x2 = pc[0][0]
    x3 = ec[0][0]
    x4 = bc[0][0]
    x5 = cc[0][0]

    figure2 = Figure(figsize=(4, 3), dpi=100)
    subplot2 = figure2.add_subplot(111)
    labels2 = 'Users', 'Product', 'Employees', 'Brands', 'Category'
    pieSizes = [float(x1), float(x2), float(x3), float(x4), float(x5)]
    my_colors2 = ['lightblue', 'lightsteelblue', 'silver']
    explode2 = (0, 0.1, 0, 0.1, 0)
    subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True,
                 startangle=90)
    subplot2.axis('equal')
    pie2 = FigureCanvasTkAgg(figure2,inventory_page)
    pie2.get_tk_widget().pack()
    print("problem")


def display_users():
    user = USER()
    users = user.display_users()
    global user_table
    global display_user
    display_user = Toplevel(display_list)
    display_user.title("Users")
    display_user.geometry("300x250")
    user_table = ttk.Treeview(display_user, column=("c1", "c2", "c3"), show='headings')
    for user in users:
        user_table.insert("", tk.END, values=user)
        # print("password: " + user[2])
    user_table.column("#1", anchor=tk.CENTER)
    user_table.heading("#1", text="userid")
    user_table.column("#2", anchor=tk.CENTER)
    user_table.heading("#2", text="username")
    user_table.column("#3", anchor=tk.CENTER)
    user_table.heading("#3", text="password")
    user_table.grid(row=1,column=0)


def display_searched_users(username):
    user = USER()
    print(username)
    users = user.search_user(username)
    print(users)
    global user_table
    global display_user
    display_user = Toplevel(display_list)
    display_user.title("Users")
    display_user.geometry("300x250")
    user_table = ttk.Treeview(display_user, column=("c1", "c2", "c3"), show='headings')

    for user in users:
        user_table.insert("", tk.END, values=user)
        # print("password: " + user[2])
    user_table.column("#1", anchor=tk.CENTER)
    user_table.heading("#1", text="userid")
    user_table.column("#2", anchor=tk.CENTER)
    user_table.heading("#2", text="username")
    user_table.column("#3", anchor=tk.CENTER)
    user_table.heading("#3", text="password")
    user_table.grid(row=1, column=0)

def display_employess():
    emp = Employee()
    employee = emp.display_employees()
    global emp_table
    global display_emp
    display_emp = Toplevel(display_list)
    display_emp.title("Employee")
    display_emp.geometry("300x250")
    emp_table = ttk.Treeview(display_emp, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')
    B1 = Button(display_emp, text="add", width=20, height=1, bg='blue', command=lambda m=None: add_employee())
    B1.grid(row=0, column=0, sticky=W, columnspan=1)
    B1 = Button(display_emp, text="delete", width=20, height=1, bg='blue', command=lambda m=None: delete_employee())
    B1.grid(row=0, column=0, columnspan=1)
    for emp in employee:
        emp_table.insert("", tk.END, values=emp)
    emp_table.column("#1", anchor=tk.CENTER)
    emp_table.heading("#1", text="emp_id")
    emp_table.column("#2", anchor=tk.CENTER)
    emp_table.heading("#2", text="First name")
    emp_table.column("#3", anchor=tk.CENTER)
    emp_table.heading("#3", text="Last name")
    emp_table.column("#4", anchor=tk.CENTER)
    emp_table.heading("#4", text="birth date")
    emp_table.column("#5", anchor=tk.CENTER)
    emp_table.heading("#5", text="salary")
    emp_table.column("#6", anchor=tk.CENTER)
    emp_table.heading("#6", text="user_id")
    emp_table.column("#7", anchor=tk.CENTER)
    emp_table.heading("#7", text="dept_id")
    emp_table.grid(row=1, column=0)

def display_searched_employess(emp_name):
    emp = Employee()
    employee = emp.search_employee(emp_name)
    global emp_table
    global display_emp
    display_emp = Toplevel(display_list)
    display_emp.title("Employee")
    display_emp.geometry("300x250")
    emp_table = ttk.Treeview(display_emp, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')
    B1 = Button(display_emp, text="add", width=20, height=1, bg='blue', command=lambda m=None: add_employee())
    B1.grid(row=0, column=0, sticky=W, columnspan=1)
    B1 = Button(display_emp, text="delete", width=20, height=1, bg='blue', command=lambda m=None: delete_employee())
    B1.grid(row=0, column=0, columnspan=1)
    for emp in employee:
        emp_table.insert("", tk.END, values=emp)
    emp_table.column("#1", anchor=tk.CENTER)
    emp_table.heading("#1", text="emp_id")
    emp_table.column("#2", anchor=tk.CENTER)
    emp_table.heading("#2", text="First name")
    emp_table.column("#3", anchor=tk.CENTER)
    emp_table.heading("#3", text="Last name")
    emp_table.column("#4", anchor=tk.CENTER)
    emp_table.heading("#4", text="birth date")
    emp_table.column("#5", anchor=tk.CENTER)
    emp_table.heading("#5", text="salary")
    emp_table.column("#6", anchor=tk.CENTER)
    emp_table.heading("#6", text="user_id")
    emp_table.column("#7", anchor=tk.CENTER)
    emp_table.heading("#7", text="dept_id")
    emp_table.grid(row=1, column=0)

def display_brand():
    brnd = Brand()
    brand = brnd.display_brands()
    global brand_table
    global display_brand
    display_brand = Toplevel(display_list)
    display_brand.title("Brand")
    display_brand.geometry("300x250")
    B1 = Button(display_brand, text="add", width=20, height=1, bg='blue', command=lambda m=None: add_brand())
    B1.grid(row=0, column=0, sticky=W, columnspan=1)
    B1 = Button(display_brand, text="delete", width=20, height=1, bg='blue', command=lambda m=None: delete_brand())
    B1.grid(row=0, column=0, columnspan=1)
    brand_table = ttk.Treeview(display_brand, column=("c1", "c2", "c3"), show='headings')

    for b in brand:
        brand_table.insert("", tk.END, values=b)
        # print("password: " + user[2])
    brand_table.column("#1", anchor=tk.CENTER)
    brand_table.heading("#1", text="brandid")
    brand_table.column("#2", anchor=tk.CENTER)
    brand_table.heading("#2", text="brand name")
    brand_table.column("#3", anchor=tk.CENTER)
    brand_table.heading("#3", text="brand status")
    # brand_table.bind('<ButtonRelease-1>', selectBrand)
    brand_table.grid(row=1, column=0)

def display_searched_brand(brand_name):
    brnd = Brand()
    brand = brnd.search_brand(brand_name)
    global brand_table
    global display_brand
    display_brand = Toplevel(display_list)
    display_brand.title("Brand")
    display_brand.geometry("300x250")
    B1 = Button(display_brand, text="add", width=20, height=1, bg='blue', command=lambda m=None: add_brand())
    B1.grid(row=0, column=0, sticky=W, columnspan=1)
    B1 = Button(display_brand, text="delete", width=20, height=1, bg='blue', command=lambda m=None: delete_brand())
    B1.grid(row=0, column=0, columnspan=1)
    brand_table = ttk.Treeview(display_brand, column=("c1", "c2", "c3"), show='headings')

    for b in brand:
        brand_table.insert("", tk.END, values=b)
        # print("password: " + user[2])
    brand_table.column("#1", anchor=tk.CENTER)
    brand_table.heading("#1", text="brandid")
    brand_table.column("#2", anchor=tk.CENTER)
    brand_table.heading("#2", text="brand name")
    brand_table.column("#3", anchor=tk.CENTER)
    brand_table.heading("#3", text="brand status")
    # brand_table.bind('<ButtonRelease-1>', selectBrand)
    brand_table.grid(row=1, column=0)


def display_category():
    cat = Category()
    category = cat.display_categorys()
    global category_table
    global display_category
    display_category = Toplevel(display_list)
    display_category.title("Category")
    display_category.geometry("300x250")
    B1 = Button(display_category, text="add", width=20, height=1, bg='blue', command=lambda m=None: add_category())
    B1.grid(row=0, column=0, sticky=W, columnspan=1)
    B1 = Button(display_category, text="delete", width=20, height=1, bg='blue',
                command=lambda m=None: delete_category())
    B1.grid(row=0, column=0, columnspan=1)
    category_table = ttk.Treeview(display_category, column=("c1", "c2", "c3"), show='headings')

    for c in category:
        category_table.insert("", tk.END, values=c)
    category_table.column("#1", anchor=tk.CENTER)
    category_table.heading("#1", text="categoryid")
    category_table.column("#2", anchor=tk.CENTER)
    category_table.heading("#2", text="category name")
    category_table.column("#3", anchor=tk.CENTER)
    category_table.heading("#3", text="category status")

    category_table.grid(row=1, column=0)

def display_searched_category(category_name):
    cat = Category()
    category = cat.search_category(category_name)
    global category_table
    global display_category
    display_category = Toplevel(display_list)
    display_category.title("Category")
    display_category.geometry("300x250")
    B1 = Button(display_category, text="add", width=20, height=1, bg='blue', command=lambda m=None: add_category())
    B1.grid(row=0, column=0, sticky=W, columnspan=1)
    B1 = Button(display_category, text="delete", width=20, height=1, bg='blue',
                command=lambda m=None: delete_category())
    B1.grid(row=0, column=0, columnspan=1)
    category_table = ttk.Treeview(display_category, column=("c1", "c2", "c3"), show='headings')

    for c in category:
        category_table.insert("", tk.END, values=c)
    category_table.column("#1", anchor=tk.CENTER)
    category_table.heading("#1", text="categoryid")
    category_table.column("#2", anchor=tk.CENTER)
    category_table.heading("#2", text="category name")
    category_table.column("#3", anchor=tk.CENTER)
    category_table.heading("#3", text="category status")

    category_table.grid(row=1, column=0)

def display_contact():
    con = Contact()
    contact = con.display_contact()
    global contact_table
    global display_contacts
    display_contacts = Toplevel(display_list)
    display_contacts.title("Category")
    display_contacts.geometry("300x250")
    B1 = Button(display_contacts, text="add", width=20, height=1, bg='blue', command=lambda m=None: add_contact())
    B1.grid(row=0, column=0, sticky=W, columnspan=1)
    B1 = Button(display_contacts, text="delete", width=20, height=1, bg='blue', command=lambda m=None: delete_contact())
    B1.grid(row=0, column=0, sticky=E, columnspan=1)
    contact_table = ttk.Treeview(display_contacts, column=("c1", "c2"), show='headings')

    for c in contact:
        contact_table.insert("", tk.END, values=c)
    contact_table.column("#1", anchor=tk.CENTER)
    contact_table.heading("#1", text="orderid")
    contact_table.column("#2", anchor=tk.CENTER)
    contact_table.heading("#2", text="contact")
    contact_table.grid(row=1, column=0)


def display_products():
    prdt = Product()
    products = prdt.display_products()
    global product_table
    global display_product
    display_product = Toplevel(display_list)
    display_product.title("Products")
    display_product.geometry("300x250")
    B1 = Button(display_product, text="add", width=20, height=1, bg='blue', command=lambda m=None: add_product())
    B1.grid(row=0, column=0, sticky=W, columnspan=1)
    B1 = Button(display_product, text="delete", width=20, height=1, bg='blue', command=lambda m=None: delete_product())
    B1.grid(row=0, column=0, columnspan=1)
    product_table = ttk.Treeview(display_product, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

    for p in products:
        product_table.insert("", tk.END, values=p)
    product_table.column("#1", anchor=tk.CENTER)
    product_table.heading("#1", text="Product_id")
    product_table.column("#2", anchor=tk.CENTER)
    product_table.heading("#2", text="Product name")
    product_table.column("#3", anchor=tk.CENTER)
    product_table.heading("#3", text="Quantity")
    product_table.column("#4", anchor=tk.CENTER)
    product_table.heading("#4", text="Rate")
    product_table.column("#5", anchor=tk.CENTER)
    product_table.heading("#5", text="user_id")
    product_table.column("#6", anchor=tk.CENTER)
    product_table.heading("#6", text="brand_id")
    product_table.column("#7", anchor=tk.CENTER)
    product_table.heading("#7", text="categoty_id")
    product_table.grid(row=1, column=0)

def display_searched_products(product_name):
    prdt = Product()
    products = prdt.search_product(product_name)
    global product_table
    global display_product
    display_product = Toplevel(display_list)
    display_product.title("Products")
    display_product.geometry("300x250")
    B1 = Button(display_product, text="add", width=20, height=1, bg='blue', command=lambda m=None: add_product())
    B1.grid(row=0, column=0, sticky=W, columnspan=1)
    B1 = Button(display_product, text="delete", width=20, height=1, bg='blue', command=lambda m=None: delete_product())
    B1.grid(row=0, column=0, columnspan=1)
    product_table = ttk.Treeview(display_product, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

    for p in products:
        product_table.insert("", tk.END, values=p)
    product_table.column("#1", anchor=tk.CENTER)
    product_table.heading("#1", text="Product_id")
    product_table.column("#2", anchor=tk.CENTER)
    product_table.heading("#2", text="Product name")
    product_table.column("#3", anchor=tk.CENTER)
    product_table.heading("#3", text="Quantity")
    product_table.column("#4", anchor=tk.CENTER)
    product_table.heading("#4", text="Rate")
    product_table.column("#5", anchor=tk.CENTER)
    product_table.heading("#5", text="user_id")
    product_table.column("#6", anchor=tk.CENTER)
    product_table.heading("#6", text="brand_id")
    product_table.column("#7", anchor=tk.CENTER)
    product_table.heading("#7", text="categoty_id")
    product_table.grid(row=1, column=0)

def display_orders():
    orde = Order()
    orders = orde.display_order()
    global order_table
    global display_order
    display_order = Toplevel(display_list)
    display_order.title("orders")
    display_order.geometry("300x250")
    B1 = Button(display_order, text="add", width=20, height=1, bg='blue', command=lambda m=None: order_product())
    B1.grid(row=0, column=0, sticky=W, columnspan=1)
    B1 = Button(display_order, text="delete", width=20, height=1, bg='blue', command=lambda m=None: delete_order())
    B1.grid(row=0, column=0, columnspan=1)
    order_table = ttk.Treeview(display_order, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "C8"), show='headings')

    for o in orders:
        order_table.insert("", tk.END, values=o)
    order_table.column("#1", anchor=tk.CENTER)
    order_table.heading("#1", text="order_id")
    order_table.column("#2", anchor=tk.CENTER)
    order_table.heading("#2", text="client name")
    order_table.column("#3", anchor=tk.CENTER)
    order_table.heading("#3", text="No of items")
    order_table.column("#4", anchor=tk.CENTER)
    order_table.heading("#4", text="payment_status")
    order_table.column("#5", anchor=tk.CENTER)
    order_table.heading("#5", text="due")
    order_table.column("#6", anchor=tk.CENTER)
    order_table.heading("#6", text="paid")
    order_table.column("#7", anchor=tk.CENTER)
    order_table.heading("#7", text="total")
    order_table.column("#7", anchor=tk.CENTER)
    order_table.heading("#8", text="prodct_id")
    order_table.grid(row=1, column=0)


def display_department():
    dep = Department()
    dept = dep.display_department()
    global dept_table
    global display_dept
    display_dept = Toplevel(display_list)
    display_dept.title("department")
    display_dept.geometry("300x250")
    B1 = Button(display_dept, text="add", width=20, height=1, bg='blue', command=lambda m=None: add_department())
    B1.grid(row=0, column=0, sticky=W, columnspan=1)
    B1 = Button(display_dept, text="delete", width=20, height=1, bg='blue', command=lambda m=None: delete_department())
    B1.grid(row=0, column=0, columnspan=1)
    dept_table = ttk.Treeview(display_dept, column=("c1", "c2", "c3"), show='headings')

    for c in dept:
        dept_table.insert("", tk.END, values=c)
    dept_table.column("#1", anchor=tk.CENTER)
    dept_table.heading("#1", text="dept_id")
    dept_table.column("#2", anchor=tk.CENTER)
    dept_table.heading("#2", text="dept name")
    dept_table.column("#3", anchor=tk.CENTER)
    dept_table.heading("#3", text="manager id")
    # dept_table.bind('<ButtonRelease-1>', selectdept)
    dept_table.grid(row=1, column=0)


def new_user():
    user = USER()
    userId = userid.get()
    userName = username.get()
    pwd = password.get()
    print(userName)
    print(pwd)
    user.insert_user(userId, userName, pwd)


def new_product():
    prdt = Product()
    productID = productid.get()
    productName = productname.get()
    qnty = quantity.get()
    prdcatid = productcatid.get()
    prdtbrndid = productbrandid.get()
    prdtusrid = productuserid.get()
    rte = rate.get()
    p = (productID, productName, qnty, rte, prdcatid, prdtbrndid, prdtusrid)
    product_table.insert("", tk.END, values=p)
    prdt.insert_product(productID, productName, qnty, rte, prdcatid, prdtbrndid, prdtusrid)


def new_employee():
    ep = Employee()
    empID = empid.get()
    emp_firstName = emp_first_name.get()
    emp_lastName = emp_last_name.get()
    userID = usr_id.get()
    dID = dpt_id.get()
    dob = birthdate.get()
    sal = salary.get()
    e = (empID, emp_firstName, emp_lastName, dob, sal, userID, dID)
    emp_table.insert("", tk.END, values=e)
    ep.insert_employee(empID, emp_firstName, emp_lastName, dob, sal, userID, dID)


def new_order():
    order = Order()
    c = Contact()
    orderID = orderid.get()
    clientName = clientname.get()
    items = no_of_items.get()
    pay_stat = payment_status.get()
    pyd = paid.get()
    du = due.get()
    ttl = total.get()
    prdtid = product_id.get()
    ph1 = phone_no1.get()
    ph2 = phone_no2.get()
    if (ph2 == 0):
        c.insert_contact(orderID, ph1)

    else:
        c.insert_contact(orderID, ph1)
        c.insert_contact(orderID, ph2)

    order.insert_order(orderID, clientName, items, pay_stat, pyd, du, ttl, prdtid)


def new_cat():  # category_id, category_name, category_active
    cat = Category()
    catID = categoryid.get()
    catName = categoryname.get()
    act = active.get()
    category = (catID, catName, act)
    category_table.insert("", tk.END, values=category)
    cat.insert_category(catID, catName, act)


def new_contact():  # category_id, category_name, category_active
    co = Contact()
    oID = orderid.get()
    contact = contct.get()
    cont = (oID, contact)
    contact_table.insert("", tk.END, values=cont)
    co.insert_contact(oID, contact)


def new_brand():  # brand_id, brand_name, brand_active #category_id
    brnd = Brand()
    brndID = brandid.get()
    brndName = brandname.get()
    act = active.get()
    brand = (brndID, brndName, act)
    brand_table.insert("", tk.END, values=brand)
    brnd.insert_brands(brndID, brndName, act)


def new_department():
    dept = Department()
    dept_id = deptid.get()
    deptName = deptname.get()
    man_id = manager_id.get()
    m = (dept_id, deptName, man_id)
    dept_table.insert("", tk.END, values=m)
    dept.insert_department(dept_id, deptName, man_id)


def exist_user():
    user = login_username.get()
    pwd = login_password.get()
    print(user)
    print(pwd)
    Exist(connect(), user)


def Exist(mydb, user):
    mycursor = mydb.cursor()
    mycursor.execute('select* from users where username =\'' + user + '\';')
    users = mycursor.fetchall()
    if (len(users) > 0):
        display_list()


def main():
    # all_count()
    tkWindow.geometry("300x250")
    tkWindow.title("Account Login")
    # bg = PhotoImage(file = "bg.jpg")
    label1 = Label(tkWindow)
    label1.place(x=0, y=0)

    Button(text="Register", height="2", width="30", command=register).pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    #  create_charts()
    tkWindow.mainloop()


main()
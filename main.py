import mysql.connector

#global variables
host = "localhost"
user = "root"
password = "Vrathod07@"
port = 3306
database = "inventory"


def connect():
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=database
    )
    return mydb


class USER:

    def display_users(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM users')
        users = mycursor.fetchall()
        for user in users:
            print(f"username: {user[0]}, userid: {user[1]}")
        mycursor.close()
        mydb.close()
        return users

    def insert_user(self, userid, username, password):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO users (user_id, username, password) VALUES (%s, %s, %s)"
        val = (userid, username, password)
        mycursor.execute(sql, val)
        print("Succesfully added user")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_user(self, userid):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM users  WHERE user_id = %s;' % (userid))
        print("Succesfully deleted user")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def count_user(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(user_id) FROM users;')
        count = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        return count

    def distinct_users(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(DISTINCT username) FROM users;')
        count = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return count

    def search_user(self,user_name):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM users WHERE username = %s"
        user = (user_name,)
        mycursor.execute(sql,user)
        users = mycursor.fetchall()
        for user in users:
            print(f"username: {user[0]}, userid: {user[1]}")
        mycursor.close()
        mydb.close()
        return users

class Employee:

    def display_employees(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM employee')
        employees = mycursor.fetchall()
        for employee in employees:
            print(f"Id: {employee[0]} Name: {employee[1]} {employee[2]} Salary {employee[4]}")
        mycursor.close()
        mydb.close()
        return employees

    def insert_employee(self, emp_id, first_name, last_name, birth_date, salary, user_id,dept_id):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO employee(emp_id, first_name, last_name, birth_date, salary, usr_id,dept_id) VALUES (%s, %s, %s,%s, %s, %s,%s)"
        val = (emp_id, first_name, last_name, birth_date, salary, user_id,dept_id)
        mycursor.execute(sql, val)
        print("Succesfully added employee")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_employee(self, emp_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM employee  WHERE emp_id = %s;' % (emp_id))
        print("Succesfully deleted employee")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def count_employee(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(emp_id) FROM employee;')
        count = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        return count

    def distinct_employees(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(DISTINCT first_name) FROM employee;')
        count = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return count

    def search_employee(self,first_name):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM employee WHERE first_name = %s"
        emp_name = (first_name,)
        mycursor.execute(sql,emp_name)
        employees = mycursor.fetchall()
        for employee in employees:
            print(f"emp_id: {employee[0]}, first_name: {employee[1]}, last_name: {employee[2]}")
        mycursor.close()
        mydb.close()
        return employees

class Department:

    def display_department(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM department')
        departments = mycursor.fetchall()
        for department in departments: #     dept_id, dept_name, manager_id
            print(f"Dept_ID {department[0]} DeptName: {department[1]} Manager_ID: {department[2]}")
        mycursor.close()
        mydb.close()
        return departments

    def insert_department(self, dept_id, dept_name, manager_id):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO department (dept_id, dept_name, manager_id) VALUES (%s, %s, %s)"
        val = (dept_id, dept_name, manager_id)
        mycursor.execute(sql, val)
        print("Succesfully added department")
        mydb.commit()
        mycursor.close()
        mydb.close()


    def remove_department(self, dept_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM department  WHERE dept_id = %s;' % (dept_id))
        print("Succesfully deleted product")
        mydb.commit()
        mycursor.close()
        mydb.close()


class Product:

    def display_products(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM product')
        products = mycursor.fetchall()
        for product in products: #  product_id, product_name, quantity, rate
            print(f"Id: {product[0]} Name: {product[1]} Quantity: {product[2]} Rate: {product[3]}")
        mycursor.close()
        mydb.close()
        return products

    def insert_product(self, product_id, product_name, quantity, rate, category_id, brand_id,user_id): #product_id, product_name, quantity, rate, category_id, brand_id
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO product(product_id, product_name, quantity, rate,category_id,branch_id,user_id) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        val = (product_id, product_name, quantity, rate,category_id, brand_id,user_id)
        mycursor.execute(sql, val)
        print("Succesfully added product")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_product(self, product_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM product  WHERE product_id = %s;' % (product_id))
        print("Succesfully deleted product")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def count_product(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(product_id) FROM product;')
        count = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        return count

    def distinct_product(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(DISTINCT product_name) FROM product;')
        count = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return count

    def search_product(self,product_name):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM product WHERE product_name = %s"
        prdt = (product_name,)
        mycursor.execute(sql,prdt)
        products = mycursor.fetchall()
        for product in products:
            print(f"product_id: {product[0]}, product_name: {product[1]}, rate: {product[3]}")
        mycursor.close()
        mydb.close()
        return products


class Category:

    def display_categorys(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM category')
        categorys = mycursor.fetchall()
        for category in categorys: #     category_id, category_name, category_active
            print(f"Id: {category[0]} Name: {category[1]} Active: {category[2]}")
        mycursor.close()
        mydb.close()
        return categorys

    def insert_category(self, category_id, category_name, category_active):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO category (category_id, category_name, category_active) VALUES (%s, %s, %s)"
        val = (category_id, category_name, category_active)
        mycursor.execute(sql, val)
        print("Succesfully added category")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_category(self, category_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM category  WHERE category_id = %s;' % (category_id))
        print("Succesfully deleted category")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def count_category(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(category_id) FROM category;')
        count = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        return count

    def distinct_category(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(DISTINCT category_name) FROM category;')
        count = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return count

    def search_category(self,cat_name):
        mydb = connect()
        mycursor = mydb.cursor()
        cat = (cat_name,)
        sql = "SELECT * FROM category WHERE category_name = %s"
        mycursor.execute(sql,cat)
        categorys = mycursor.fetchall()
        for category in categorys:
            print(f"category_id: {category[0]}, category_name: {category[1]}")
        mycursor.close()
        mydb.close()
        return categorys


class Brand:
    def display_brands(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM brands')
        brands = mycursor.fetchall()
        for brand in brands: #branch_id, brand_name, brand_active
            print(f"Id: {brand[0]} Name: {brand[1]} Active: #{brand[2]}")
        mycursor.close()
        mydb.close()
        return brands

    def insert_brands(self, branch_id, brand_name, brand_active):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO brands (branch_id, brand_name, brand_active) VALUES (%s, %s, %s)"
        val = (branch_id, brand_name, brand_active)
        mycursor.execute(sql, val)
        print("Succesfully added brand")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_brands(self, branch_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM brands WHERE branch_id = %s;' % (branch_id))
        print("Succesfully deleted brand")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def count_brand(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(branch_id) FROM brands;')
        count = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        return count

    def distinct_brand(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(DISTINCT brand_name) FROM brands;')
        count = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return count

    def search_brand(self,brand_name):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM brands WHERE brand_name = %s"
        brnd = (brand_name,)
        mycursor.execute(sql,brnd)
        brands = mycursor.fetchall()
        for brand in brands:
            print(f"brand_id: {brand[0]}, brand_name: {brand[1]}")
        mycursor.close()
        mydb.close()
        return brands

class Order:

    def display_order(self): #order_id, client_name, no_of_items, payment_status, due, paid, total, product_id, category_id, user_id
      mydb = connect()
      mycursor = mydb.cursor()
      mycursor.execute('SELECT * FROM orders')
      orders= mycursor.fetchall()
      for order in orders:
          print(f"Id: {orders[0]} Name: {order[1]} Total: {order[7]}")
      mycursor.close()
      mydb.close()
      return orders

    def insert_order(self,order_id, client_name, no_of_items, payment_status, due, paid, total, product_id):
      mydb = connect()
      mycursor = mydb.cursor()
      sql ="INSERT INTO orders(order_id, client_name, no_of_items, payment_status, due, paid, total, product_id) VALUES (%s, %s, %s, %s, %s,%s, %s, %s)"
      val = (order_id, client_name, no_of_items, payment_status, due, paid, total, product_id)
      mycursor.execute(sql, val)
      print("Succesfully added order")
      mydb.commit()
      mycursor.close()
      mydb.close()

    def remove_order(self, order_id):
      mydb = connect()
      mycursor = mydb.cursor()
      mycursor.execute('DELETE FROM orders WHERE order_id = %s;' % (order_id))
      print("Succesfully deleted order")
      mydb.commit()
      mycursor.close()
      mydb.close()

class Contact:

    def display_contact(self): #order_id,contact
      mydb = connect()
      mycursor = mydb.cursor()
      mycursor.execute('SELECT * FROM contact')
      con= mycursor.fetchall()
      mycursor.close()
      mydb.close()
      return con

    def insert_contact(self,order_id, contact):
      mydb = connect()
      mycursor = mydb.cursor()
      sql ="INSERT INTO contact (order_id, contact) VALUES (%s, %s)"
      val = (order_id, contact)

      mycursor.execute(sql, val)
      print("Succesfully added order")
      mydb.commit()
      mycursor.close()
      mydb.close()

    def remove_contact(self, order_id):
      mydb = connect()
      mycursor = mydb.cursor()
      mycursor.execute('DELETE FROM contact WHERE order_id = %s;' % (order_id))
      print("Succesfully deleted contact")
      mydb.commit()
      mycursor.close()
      mydb.close()



def main():
  emp = Employee()
  e = emp.search_employee("sai")

if __name__ == "__main__":
    main()
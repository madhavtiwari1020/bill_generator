import mysql.connector
def bill():
    #forsql
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Madhav@2002",
        database="newdb1"
        )
    cur=con.cursor()
    #user se input
    id=int(input("enter order id"))
    name=input("enter product name")
    price=float(input("enter product price"))
    quantity=int(input("enter product quantity"))
    total=price*quantity
    #insert query
    sql="insert into order_detail(order_id, product_name, p_price, quantity,amount) values(%s,%s,%s,%s,%s)"
    values=(id,name,price,quantity,total)
    cur.execute(sql,values)
    con.commit()
    print("data inserted succesfuly into table")
    cur.close()
    con.close()
    x=str(id)
    y=".txt"
    z=x+y
    file=open(z,"w")
    a=str(price)
    b=str(quantity)
    c=str(total)
    st=(f'======Your Bill======\n Product ID    : {x}\n Product Name  : {name}\n Product Price : {a}\n Quantity      : {b}\n Total Price   : {c}\n==Thank You For Shoping==')
    file.write(st)
bill()

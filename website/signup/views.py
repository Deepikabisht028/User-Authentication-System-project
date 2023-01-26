from django.shortcuts import render
import mysql.connector as sql
fn=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Sam@97560",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}')".format(fn,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signuppage.html')

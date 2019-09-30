import tkinter as tk
import pymysql

def success_tip(username):
    root.destroy()
    root1 = tk.Tk()
    root1.title('通知信息')
    welcome = username+'，欢迎您！！！'
    tk.Label(root1,text=welcome,font=36).pack(padx=100,pady=100)
    root1.mainloop()

def fail_tip():
    root2 = tk.Tk()
    root2.title('错误提示')
    tk.Label(root2,text='登录失败！密码错误或者账号不存在！',font=18,fg='red').pack(padx=20,pady=20)
    root2.mainloop()

def auto_login():
    #连接数据库
    db = pymysql.connect(host='localhost',user='root',password='yuan',db='test',port=3306)
    #获取操作游标
    cur = db.cursor()
    #查询数据库
    sql = 'select * from user'
    entry1 = input1.get()
    entry2 = input2.get()
    flag = True
    try:
        cur.execute(sql)    #执行查询
        results = cur.fetchall()    #获取所有查询数据
        for row in results:
            uid = row[4]    #账号
            pwd = row[5]    #密码
            #判断输入的账号和密码是否正确
            if entry1 == uid and entry2 == pwd:
                username = row[0]
                success_tip(username)
                flag = True
                break
            else:
                flag = False
        if flag == False:
            fail_tip()
    except Exception as e:
        print('登录异常')

def exit_login():
    root.destroy()

def frame():
    global root
    root = tk.Tk()
    root.title('登录窗口')
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    #账号标签，位置在第0行第0列
    tk.Label(root,text='账号:').grid(row=0,column=0)
    #密码标签，位置在第1行第0列
    tk.Label(root,text='密码:').grid(row=1,column=0)
    #账号输入框
    global input1
    input1 = tk.Entry(root,textvariable=v1)
    input1.grid(row=0,column=1,padx=10,pady=5)
    #密码输入框
    global input2
    input2 = tk.Entry(root,textvariable=v2,show='*')
    input2.grid(row=1,column=1,padx=10,pady=5)
    #登录按钮
    tk.Button(root,text='登录',width=10,command=auto_login).grid(row=3,column=0,sticky=tk.W,padx=10,pady=5)
    #退出按钮
    tk.Button(root,text='退出',width=10,command=exit_login).grid(row=3,column=1,sticky=tk.E,padx=10,pady=5)
    root.mainloop()

if __name__ == '__main__':
    frame()

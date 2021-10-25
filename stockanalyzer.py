#stock
#please make sure to connect it to the internet 
#imports
import tkinter as tk
from tkinter import messagebox
from yahoo_fin import stock_info
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#functions
def graph():
    year = []
    price = []
    #function to read the file 
    user_input=e.get()
    f = open(user_input+".txt",'r')
    for row in f:
        row = row.split(' ')
        year.append(row[0])
        price.append(row[1])
    #ploting graph
    plt.plot(year, price,'o-g',label = 'Stock Data')
    
    plt.xlabel('year', fontsize = 12)
    plt.ylabel('price', fontsize = 12)    
    plt.title(user_input, fontsize = 20)
    plt.legend()
    plt.show()

#function to get stock price
def stock_update():
    price=stock_info.get_live_price(e.get())
    stock_price.set(price) 

#adding upper case to e Entry
def up(event):
    upper_case.set(upper_case.get().upper())                                    

#updating the search list
def update_list_box(data):
    list_box.delete(0,END)
    for item in data:
        list_box.insert(END,item)

def update(e):
    entry.delete(0,END)

    entry.insert(0,list_box.get(ANCHOR))
#checking and verifying the words entered in entry 
#dont know full functionality
def check(e):
    typed_text = entry.get()

    if typed_text =="":
        data=lang
    else:
        data = []
        for item in lang:
            if typed_text.lower() in item:
              data.append(item)

    update_list_box(data)

    
    
def mail():
    
    sender_address = 'eyes.8082@gmail.com'
    sender_pass = 'Mandal@1312'
    receiver_address = email.get()
    mail_content = '''we will get you notified when your target price hit
    '''

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'alert setup notification'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

    messagebox.showinfo("succeed","thank you,We will notify you")
     
#window creating using tkinter
root = tk.Tk()
#background color
root.config(bg='white')
#title
root.title('project')
#window size
root.geometry('1200x920')
#fixing size
root.resizable(0,0)
#manages the value
stock_price=StringVar()
upper_case=StringVar()
email=StringVar()
#menu
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
menubar = Menu(root)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="yo")  
   
  
file.add_separator()  
  
file.add_command(label="Exit", command=root.quit)  
  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar, tearoff=0)  
  
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar)  
 
menubar.add_cascade(label="about", menu=help)  
about=Menu(menubar)
root.config(menu=menubar) 
#images
#icon image
icon=PhotoImage(file="stocklogo.png")
root.iconphoto(False,icon)
#commented out
'''image1 = ImageTk.PhotoImage(file="candle.png")
label1=Label(root,image=image1,height=450,width=800) 
label1.place(x=0, y=0)
'''

image2 = ImageTk.PhotoImage(file="search.jpg")
label2=Label(root, image=image2, height=550, width=600)
label2.place(x=630, y=455)

image3 = ImageTk.PhotoImage(file="c.jpg")
label3=Label(root, image=image3, height=300, width=600)
label3.place(x=0, y=590)

#email 
label_email=Label(root,text="Enter E-mail here to get alert:",bg="white",font=("none",15)).place(x=10,y=270)
receiver_address=Entry(root, font=("none",14), bg='lightblue',textvariable=email)
receiver_address.place(x=280, y=270)
print(email)
#target 
label_taget=Label(root,text="Set Target Here:",bg="white",font=("none",15)).place(x=150,y=320)
target=Label(root,text="When Current Price",bg="white",font=("none",11))
target.place(x=10, y=370)
operator_choice = ttk.Combobox(root, width=17, font=("none",12))
  
# Adding combobox drop down list
operator_choice['value'] = ('select the operation',
                          ' is equal to', 
                          ' is less than',
                          ' is greater than',
                          ' is greater than equal to',
                          ' is less than equal to',
                          )
  
operator_choice.place(x=170, y=370)
#fix the first element n the list
operator_choice.current(0)
#target price
tp=Label(root, text="target price", bg="white", font=("none",12)).place(x=370,y=330)
target2=Entry(root, font=("none",18), bg='lightblue')
target2.place(x=370, y=365, width=110)
#target button
target_button=Button(root,text="click to submit",command=mail,height=2,width=40,bg='green',fg='white').place(x=100, y=405)
#title
label_top=Label(root, text="Stock's \nAnalyzer", font=("none",75), fg='gray', bg='white')
label_top.place(x=50, y=15)
#stock data
name=Label(root, text="stock name:", bg='white', font=("none",38)).place(x=590,y=70)
e=Entry(root,bg='lightblue',textvariable=upper_case,font=("none",18))
e.place(x=900,y=88,height=40)
#whenever i release the typed/hold key it impliments
e.bind("<KeyRelease>", up)

label_sign=Label(root, text="please enter the stock code \nor find it in search below", font=("none",11),bg='white')
label_sign.place(x=790, y=140)
#exception is thrown because stock name has codes but excption is not proper as we dont know much
# and except label is also not woring but its kinda working 
try:
   submit_button=Button(root, text='submit', command=stock_update, bg='white', height=2, width=20,border=2,font=('none',12)).place(x=770, y=220)
except AssertionError:
    #not working
    error_label=Label(root,text="please check the company code").place(x=630, y=290)
showResult=Label(root, text="price: $", bg='white', font=("none",18)).place(x=710, y=330)
#shows result
result=Label(root, textvariable=stock_price, bg='white', font=("none",18)).place(x=800, y=330)
#stock search 
label=Label(root, text='note: write in lower case', bg='lightblue').place(x=870, y=625)
entry=Entry(root,bg='lightblue',font=('none',20))
entry.place(x=842,y=568,height=44, width=180)
entry.bind("<KeyRelease>",check)
list_box=Listbox(root, width=32, bg='lightblue', font=('none',15))
list_box.place(x=750, y=665)
lang=[
    ' apple:AAPL',' amazon:AMZN',' microsoft:MSFT'
    ,' tata motors:name',' FedEx:FDX',' Google:GOOG',' Ford:F',' oracle:ORCL'
    ,' FACEBOOK:FB',' Mastercard:MA',' Opentext Corp :OTEX',' BlackRock.In:BLK',' AUTOdesk,inc.:Adsk'
    ,' American Express Company:Axp',' Berkshire Hathway inc. Class A:BRK', 
    ]
update_list_box(lang)
list_box.bind("<<ListboxSelect>>",update)
#chart
line=Label(root,text="____________________________________________________________________________________________________________________________",bg='white',fg='gray')
line.place(x=4, y=440)
chart_label=Label(root, text="to view chart click here", bg ='white', font=("none",11)).place(x=200, y=480)
b=Button(root, text='Click me', bg='white', command=graph, height=2, width=20)
b.place(x=200, y=530)
#mainloop
root.mainloop()

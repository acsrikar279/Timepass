from tkinter import*
import random,time,datetime

root=Tk()
root.geometry("1600x8000")
root.title("Gayatri College Canteen")
root.config(bg='white')
Tops=Frame(root, width=1600,bg='white',relief=SUNKEN)
Tops.pack(side=TOP)
f1=Frame(root,width=800,height=700,bg='white',relief=SUNKEN)
f1.pack(side=LEFT)

# Time thecchukovatiniki

localtime=time.asctime(time.localtime(time.time()))
lblInfo=Label(Tops,font=("courier",50,'bold'),text="Canteen",fg="Steel Blue",bg='white',bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=("courier",20,'bold'),text=localtime,fg="Steel Blue",bg='white',bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
def Ref():
    num=random.randint(1000,2000)
    BillId.set(str(num))
    if (Idly.get()==""):
        CoIdly=0
    else:
        CoIdly=float(Idly.get())
    if (Dosa.get()==""):
        CoDosa=0
    else:
        CoDosa=float(Dosa.get())
    if (Upma.get()==""):
        CoUpma=0
    else:
        CoUpma=float(Upma.get())
    if (Biryani.get()==""):
        CoBiryani=0
    else:
        CoBiryani=float(Biryani.get())
    if (Manchuriya.get()==""):
        CoManchuriya=0
    else:
        CoManchuriya=float(Manchuriya.get())
    if (Bhajji.get()==""):
        CoBhajji=0
    else:
        CoBhajji=float(Bhajji.get())
    FCIdly =CoIdly * 20
    FCBhajji=CoBhajji * 20
    FCDosa = CoDosa* 13
    FCUpma = CoUpma * 20
    FCBiryani = CoBiryani* 50
    FCManchuriya=CoManchuriya * 25

    TotalCost=(FCIdly+FCBhajji+FCDosa+FCUpma+FCBiryani+FCManchuriya)
    Total.set(TotalCost)

def qExit():
    root.destroy()

def Reset():
    BillId.set("")
    Idly.set("")
    Dosa.set("")
    Upma.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Bhajji.set("")
    Tax.set("")
    Cost.set("")
    Biryani.set("")
    Manchuriya.set("")

BillId = StringVar()
Idly=StringVar()
Dosa=StringVar()
Upma=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Bhajji=StringVar()
Tax=StringVar()
Cost=StringVar()
Biryani=StringVar()
Manchuriya=StringVar()

# First Column lo items

lblBillId= Label(f1, font=("courier", 16, 'bold'),text="Bill ID",bd=16,bg='white',anchor="w")
lblBillId.grid(row=0, column=0)
txtBillID=Entry(f1, font=("courier",16,'bold'),textvariable=BillId,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBillID.grid(row=0,column=1)

lblIdly= Label(f1, font=("courier", 16, 'bold'),text="Idly",bd=16,bg='white',anchor="w")
lblIdly.grid(row=1, column=0)
txtIdly=Entry(f1, font=("courier",16,'bold'),textvariable=Idly,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtIdly.grid(row=1,column=1)


lblDosa= Label(f1, font=("courier", 16, 'bold'),text="Dosa",bd=16,bg='white',anchor="w")
lblDosa.grid(row=2, column=0)
txtDosa=Entry(f1, font=("courier",16,'bold'),textvariable=Dosa,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDosa.grid(row=2,column=1)


lblUpma= Label(f1, font=("courier", 16, 'bold'),text="Upma",bg='white',bd=16,anchor="w")
lblUpma.grid(row=3, column=0)
txtUpma=Entry(f1, font=("courier",16,'bold'),textvariable=Upma,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtUpma.grid(row=3,column=1)

# Second Column of Items

lblBhajji= Label(f1, font=("courier", 16, 'bold'),text="Bhajji",bd=16,bg='white',anchor="w")
lblBhajji.grid(row=0, column=2)
txtBhajji=Entry(f1, font=("courier",16,'bold'),textvariable=Bhajji,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBhajji.grid(row=0,column=3)

lblBiryani= Label(f1, font=("courier", 16, 'bold'),text="Biryani",bd=16,bg='white',anchor="w")
lblBiryani.grid(row=1, column=2)
txtBiryani=Entry(f1, font=("courier",16,'bold'),textvariable=Biryani,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBiryani.grid(row=1,column=3)

lblMachuriya= Label(f1, font=("courier", 16, 'bold'),text="Manchuriya",bd=16,bg='white',anchor="w")
lblMachuriya.grid(row=2, column=2)
txtMachuriya=Entry(f1, font=("courier",16,'bold'),textvariable=Manchuriya,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtMachuriya.grid(row=2,column=3)

lblTotalCost= Label(f1, font=("courier", 16, 'bold'),text="Total Cost",bd=16,bg='white',anchor="w")
lblTotalCost.grid(row=5, column=0)
txtTotalCost=Entry(f1, font=("courier",16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=1)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("courier",16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("courier",16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("courier",16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

root.mainloop()

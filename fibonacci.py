from tkinter import *
root=Tk()
root.title("fibonacci Series")
root.geometry("400x400")
entry_no=Entry(root)
label1=Label(root,text="fibonacci series")
label2=Label(root,text="fibonacci sum")
def generateseries():
    input_no=int(entry_no.get())
    num1=0
    num2=1
    sum=0
    sum2=0
    counter=1
    while(counter<=input_no):
        label1["text"]+=str(sum)+" "
        label2["text"]=str(sum2)
        counter= counter+1
        num1=num2
        num2=sum
        sum=num1+num2
        sum2=sum+sum2
button1=Button(root, text="Generate fibonacci series", command=generateseries, bg="dark blue", fg="white")
button1.pack()
label1.pack()
label2.pack()
entry_no.pack()
root.mainloop()
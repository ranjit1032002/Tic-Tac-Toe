from tkinter import *

window=Tk()
window.geometry("310x310")
window.resizable(0,0)
x=1
def show(b):
     global x
     x=x+1
     if(x%2==0):
          if(b["text"]==""):
               b["text"]="0"
               if(b["text"]=="0"):
                    b["fg"]="blue"
                    b["bg"]="yellow"
     else:
          if(b["text"]==""):
               b["text"]="X"
               if(b["text"]=="X"):
                    b["fg"]="orange"
                    b["bg"]="red"
     if((b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0")):
          print("Player 1 Is Winner!!")
          
     elif((b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X")):
          print("Player 2 Is Winner!!")
          
     elif((b4["text"]=="0" and b5["text"]=="0" and b6["text"]=="0")):
          print("Player 1 Is Winner!!")
          
     elif((b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X")):
          print("Player 2 Is Winner!!")
          
     elif((b7["text"]=="0" and b8["text"]=="0" and b9["text"]=="0")):
          print("Player 1 Is Winner!!")
          
     elif((b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X")):
          print("Player 2 Is Winner!!")
          
          
     if((b1["text"]=="0" and b4["text"]=="0" and b7["text"]=="0")):
          print("Player 1 Is Winner!!")
          
     elif((b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X")):
          print("Player 2 Is Winner!!")
          
     elif((b2["text"]=="0" and b5["text"]=="0" and b8["text"]=="0")):
          print("Player 1 Is Winner!!")
         
     elif((b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X")):
          print("Player 2 Is Winner!!")
          
     elif((b3["text"]=="0" and b6["text"]=="0" and b9["text"]=="0")):
          print("Player 1 Is Winner!!")
          
     elif((b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X")):
          print("Player 2 Is Winner!!")
          

     if((b1["text"]=="0" and b5["text"]=="0" and b9["text"]=="0")):
          print("Player 1 Is Winner!!")
          
     elif((b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X")):
          print("Player 2 Is Winner!!")
          
     elif((b3["text"]=="0" and b5["text"]=="0" and b7["text"]=="0")):
          print("Player 1 Is Winner!!")
          
     elif((b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X")):
          print("Player 2 Is Winner!!")
          

          
b1=Button(window,width=5,height=2,font=("Arial",25),command=lambda:show(b1))
b2=Button(window,width=5,height=2,font=("Arial",25),command=lambda:show(b2))
b3=Button(window,width=5,height=2,font=("Arial",25),command=lambda:show(b3))
b4=Button(window,width=5,height=2,font=("Arial",25),command=lambda:show(b4))
b5=Button(window,width=5,height=2,font=("Arial",25),command=lambda:show(b5))
b6=Button(window,width=5,height=2,font=("Arial",25),command=lambda:show(b6))
b7=Button(window,width=5,height=2,font=("Arial",25),command=lambda:show(b7))
b8=Button(window,width=5,height=2,font=("Arial",25),command=lambda:show(b8))
b9=Button(window,width=5,height=2,font=("Arial",25),command=lambda:show(b9))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
window.mainloop()


import PIL.Image

#trying to make gui
from tkinter import *
import os,random

window=Tk()
window.geometry("500x800")
window.configure(background='khaki3')
window.title("Color to Black and White BY Saurabh Jadhav")
l1=Label(text='An Awesome B/W Converter\nBy Saurabh Jadhav',font=('Times',18),fg='white',bg='purple')
l1.pack(fill=X)
l2=Label(window,text='Enter File Location :',font=('Century gothic',17),background='khaki2')
l2.pack()
e1=Entry(window,font=('Lucida calligraphy',10))
e1.pack()
b1=Button(window,text="Go",font=('Times',16),background='khaki4',fg='white',command=lambda: code(e1.get()))
b1.pack()

t1=Text(height=4,font=('Comic sans ms',18),bg='sienna4',fg='white')
t1.pack(fill=X)
l3=Label(window,text='''"“Talk is cheap. Show me the code.” 
"
 ― Linus Torvalds''',font=('Comic sans ms',21))
l3.pack()
#code
def code(path):

	try:
		res=open(path,'rb')
		
		col = PIL.Image.open(res)
		gray = col.convert('L')

		gray.save("wow.png")
		bw = gray.point(lambda x: 0 if x<128 else 255, '1')
		bw.save("result_bw.png")
		t1.delete(1.0,END)
		t1.insert(END,"File Converted Successfully")

			
	except FileNotFoundError:
		t1.delete(1.0,END)
		t1.insert(END,"FileNotFoundError check file Location")
	
	

window.mainloop()






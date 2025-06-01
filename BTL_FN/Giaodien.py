#Thêm thư viện tkinter
from tkinter import *
from tkinter.ttk import Combobox

#Tạo một cửa sổ mới
window = Tk("Tranning.csv")

#Thêm tiêu đề cho cửa sổ
window.title('Dự đoán giá nhà tại Hanoi')

#Đặt kích thước của cửa sổ
window.geometry('350x200')

#Thêm label có nội dung Hello, font chữ
# lbl = Label(window, text="Dự đoán giá nhà tại Hanoi" , font=("Arial Bold", 20))
#
# #Xác định vị trí của label
# lbl.grid(column=0, row=0)

lbl1 = Label(window, text="Quận" , font=("Arial Bold", 10))
lbl1.grid(column=0, row=1)
lbl2 = Label(window, text="Loại hình nhà ở" , font=("Arial Bold", 10))
lbl2.grid(column=1, row=1)
lbl3 = Label(window, text="Giấy tờ pháp lý" , font=("Arial Bold", 10))
lbl3.grid(column=2, row=1)
lbl4 = Label(window, text="Số tầng" , font=("Arial Bold", 10))
lbl4.grid(column=3, row=1)
lbl5 = Label(window, text="Số phòng khách" , font=("Arial Bold", 10))
lbl5.grid(column=4, row=1)
lbl6 = Label(window, text="Car room" , font=("Arial Bold", 10))
lbl6.grid(column=5, row=1)
lbl7 = Label(window, text="WC" , font=("Arial Bold", 10))
lbl7.grid(column=6, row=1)
lbl8 = Label(window, text="Số phòng ngủ" , font=("Arial Bold", 10))
lbl8.grid(column=7, row=1)
lbl9 = Label(window, text="Diện tích" , font=("Arial Bold", 10))
lbl9.grid(column=8, row=1)
lbl10 = Label(window, text="Giá" , font=("Arial Bold", 10))
lbl10.grid(column=9, row=1)
#Hàm khi nút được nhấn
def clicked():
    lbl.configure(text="Button was clicked !!")

#Gọi hàm clicked khi nút được nhấn
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=3)

#Lặp vô tận để hiển thị cửa sổ
window.mainloop()

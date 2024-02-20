import customtkinter as ctk
from customtkinter import *
from PIL import Image
from dataBase import Data
from tkinter import messagebox,Text
root=ctk.CTk()
root.geometry("700x750+100x200")
root.title("Hospital")


def add_in_database():
    Data.insert_data(ent_name.get(),
                     ent_num.get(),
                     ent_age.get(),
                     ent_mony.get(),
                     ent_mony_.get(),
                     ent_doctor.get(),
                     ent_ding.get("1.0",END),
                     ent_sta.get(),
                     ent_room.get(),
                     ent_ch.get(),
    )
    messagebox.showinfo("Add","Complite {}".format(ent_num.get()))
    ent_name.delete(0,len(ent_name.get()))
    ent_num.delete(0,len( ent_num.get()))
    ent_age.delete(0,len(ent_age.get()))
    ent_mony.delete(0,len(ent_mony.get()))
    ent_mony_.delete(0,len(ent_mony_.get()))
    ent_sta.delete(0,len(ent_sta.get()))
    ent_doctor.delete(0,len(ent_doctor.get()))
    ent_room.delete(0,len(ent_room.get()))
    ent_ch.delete(0,len(ent_ch.get()))
    ent_ding.delete("1.0",len(ent_ding.get("1.0",END)))

def add():
    add=ctk.CTk(fg_color="red")
    add.geometry("500x650")
    add.title("ADD Item")
    add.resizable(False,False)
    global ent_name
    ent_name=CTkEntry(add,width=300)
    ent_name.place(x=10,y=15)
    lab_name=CTkLabel(add,text="الاسم",text_color="white",font=CTkFont(size=22))
    lab_name.place(x=400,y=15)
    
    global ent_num
    ent_num=CTkEntry(add,width=300)
    ent_num.place(x=10,y=50)
    lab_num=CTkLabel(add,text=" الهاتف رقم",text_color="white",font=CTkFont(size=22))
    lab_num.place(x=400,y=50)

    global ent_age
    ent_age=CTkEntry(add,width=300)
    ent_age.place(x=10,y=85)
    lab_age=CTkLabel(add,text=" العمر",text_color="white",font=CTkFont(size=22))
    lab_age.place(x=400,y=85)
  
    global ent_mony
    ent_mony=CTkEntry(add,width=300)
    ent_mony.place(x=10,y=120)
    lab_mony=CTkLabel(add,text=" المدفوع المبلغ",text_color="white",font=CTkFont(size=22))
    lab_mony.place(x=350,y=120)
                   
    global ent_mony_
    ent_mony_=CTkEntry(add,width=300)
    ent_mony_.place(x=10,y=155)
    lab_mony_=CTkLabel(add,text=" المتبقي المبلغ",text_color="white",font=CTkFont(size=22))
    lab_mony_.place(x=350,y=155)

    global ent_doctor
    ent_doctor=CTkEntry(add,width=300)
    ent_doctor.place(x=10,y=190)
    lab_doctor=CTkLabel(add,text="المسئول الدكتور",text_color="white",font=CTkFont(size=22))
    lab_doctor.place(x=350,y=190)

    
    global ent_room
    ent_room=CTkEntry(add,width=300)
    ent_room.place(x=10,y=225)
    lab_room=CTkLabel(add,text="الغرفه",text_color="white",font=CTkFont(size=22))
    lab_room.place(x=400,y=225)

    
    global ent_ch
    ent_ch=CTkEntry(add,width=300)
    ent_ch.place(x=10,y=260)
    lab_ch=CTkLabel(add,text=" مزمن مرض",text_color="white",font=CTkFont(size=22))
    lab_ch.place(x=350,y=260)

    
    global ent_sta
    ent_sta=CTkEntry(add,width=300)
    ent_sta.place(x=10,y=295)
    lab_sta=CTkLabel(add,text=" المريض حاله",text_color="white",font=CTkFont(size=22))
    lab_sta.place(x=350,y=295)

    
    global ent_ding
    ent_ding=Text(add,width=40,height=10)
    ent_ding.place(x=10,y=450)
    lab_ding=CTkLabel(add,text=" التشخيص",font=CTkFont(size=22),text_color="white")
    lab_ding.place(x=400,y=360)

    button_save=CTkButton(add,text="save",fg_color="green",hover_color="green",command=add_in_database)
    button_save.place(x=300,y=600)

    button_canel=CTkButton(add,text="cancel",fg_color="black",hover_color="black",command=add.destroy)
    button_canel.place(x=100,y=600)
    add.mainloop()


def search():
    number=CTkInputDialog(text="Entry Number : ",title="Search")
    num=number.get_input()
    data=Data.select_data(num)
    frame_display_data=CTkFrame(frame,width=700,height=750,fg_color="blue")
    frame_display_data.place(x=0,y=0)
    img_back=Image.open("angle-left.png")
    img_=CTkImage(light_image=img_back,size=(50,50))
    button_back=CTkButton(frame_display_data,text="",image=img_,command=frame_display_data.destroy,fg_color="blue",hover_color="blue")
    button_back.place(x=500,y=10)

    ent_name_dis=CTkEntry(frame_display_data,width=300)
    ent_name_dis.place(x=10,y=15)
    lab_name_dis=CTkLabel(frame_display_data,text="الاسم",text_color="white",font=CTkFont(size=22))
    lab_name_dis.place(x=400,y=15)
    
    
    ent_num_dis=CTkEntry(frame_display_data,width=300)
    ent_num_dis.place(x=10,y=50)
    lab_num_dis=CTkLabel(frame_display_data,text=" الهاتف رقم",text_color="white",font=CTkFont(size=22))
    lab_num_dis.place(x=400,y=50)

    
    ent_age_dis=CTkEntry(frame_display_data,width=300)
    ent_age_dis.place(x=10,y=85)
    lab_age_dis=CTkLabel(frame_display_data,text=" العمر",text_color="white",font=CTkFont(size=22))
    lab_age_dis.place(x=400,y=85)
  
   
    ent_mony_dis=CTkEntry(frame_display_data,width=300)
    ent_mony_dis.place(x=10,y=120)
    lab_mony_dis=CTkLabel(frame_display_data,text=" المدفوع المبلغ",text_color="white",font=CTkFont(size=22))
    lab_mony_dis.place(x=350,y=120)

 
    ent_mony__dis=CTkEntry(frame_display_data,width=300)
    ent_mony__dis.place(x=10,y=155)
    lab_mony__dis=CTkLabel(frame_display_data,text=" المتبقي المبلغ",text_color="white",font=CTkFont(size=22))
    lab_mony__dis.place(x=350,y=155)

    ent_doctor_dis=CTkEntry(frame_display_data,width=300)
    ent_doctor_dis.place(x=10,y=190)
    lab_doctor_dis=CTkLabel(frame_display_data,text="المسئول الدكتور",text_color="white",font=CTkFont(size=22))
    lab_doctor_dis.place(x=350,y=190)

    ent_room_dis=CTkEntry(frame_display_data,width=300)
    ent_room_dis.place(x=10,y=225)
    lab_room_dis=CTkLabel(frame_display_data,text="الغرفه",text_color="white",font=CTkFont(size=22))
    lab_room_dis.place(x=400,y=225)

    ent_ch_dis=CTkEntry(frame_display_data,width=300)
    ent_ch_dis.place(x=10,y=260)
    lab_ch_dis=CTkLabel(frame_display_data,text=" مزمن مرض",text_color="white",font=CTkFont(size=22))
    lab_ch_dis.place(x=350,y=260)

    ent_sta_dis=CTkEntry(frame_display_data,width=300)
    ent_sta_dis.place(x=10,y=295)
    lab_sta_dis=CTkLabel(frame_display_data,text=" المريض حاله",text_color="white",font=CTkFont(size=22))
    lab_sta_dis.place(x=350,y=295)

    ent_ding_dis=Text(frame_display_data,width=40,height=10,font=20)
    ent_ding_dis.place(x=10,y=450)
    lab_ding_dis=CTkLabel(frame_display_data,text=" التشخيص",font=CTkFont(size=22),text_color="white")
    lab_ding_dis.place(x=400,y=360)

    ent_name_dis.insert(0,data[0][0])
    ent_num_dis.insert(0,data[0][1])
    ent_age_dis.insert(0,data[0][2])
    ent_mony_dis.insert(0,data[0][3])
    ent_mony__dis.insert(0,data[0][4])
    ent_doctor_dis.insert(0,data[0][5])
    ent_sta_dis.insert(0,data[0][7])
    ent_room_dis.insert(0,data[0][8])
    ent_ch_dis.insert(0,data[0][9])
    ent_ding_dis.insert("1.0",data[0][6])
  




def main():
    global frame
    frame=CTkFrame(root,width=700,height=750,fg_color="white")
    frame.place(x=0,y=0)
    img_cr=Image.open("pen-clip.png")
    img_=CTkImage(light_image=img_cr,size=(50,50))
    fram_content=CTkFrame(frame,width=250,height=750,fg_color="red")
    fram_content.place(x=250,y=0)
    button_create=CTkButton(frame,text="",image=img_,hover_color="gray",fg_color="red",bg_color="red",command=add)
    button_create.place(x=300,y=50)

    img_se=Image.open("search.png")
    img_s=CTkImage(light_image=img_se,size=(50,50))
    button_create=CTkButton(frame,text="",image=img_s,hover_color="gray",fg_color="red",bg_color="red",command=search)
    button_create.place(x=300,y=200)


img=Image.open("hosbital.jpg")
img_=CTkImage(light_image=img,size=(700,750))
lab_img=CTkLabel(root,text="",image=img_)
lab_img.pack()
button_start=CTkButton(root,text="Start",text_color="white",fg_color="red",bg_color="red",hover_color="red",command=main)
button_start.place(x=300,y=700)
root.mainloop()
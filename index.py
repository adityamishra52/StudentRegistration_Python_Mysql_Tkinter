import ConnectionWithDb as con
import tkinter as tk
from PIL import Image , ImageTk 
from tkinter import filedialog
import InsertionOfData as insert

def browse_photo():
    try:
                
        photo_path=filedialog.askopenfilename(title="Select Photo",filetypes=[("Image Files", ".jpg .jpeg .png")])
        photo_path_entry.delete(0,tk.END)
        photo_path_entry.insert(0,photo_path)

    except Exception as e:
        print("problem in your Index Page: ",e)


def insert_data():
    try:
        
        cur=con.cur
        name=name_entry.get()
        email=email_entry.get()
        branch=branch_entry.get()
        photo_path = photo_path_entry.get()
        with open(photo_path,'rb') as file:
            photo_data=file.read()
            query="INSERT INTO student(name,branch,photo,email) VALUES(%s,%s,%s,%s)"
            cur.execute(query,(name,branch,photo_data,email))
            con.cnx.commit()
            rollno=cur.lastrowid
            status_label.config(text=f"Data Insert Succesfully, your roll No. is {rollno}")
            print("Succesfull insert.....")
                       
    except Exception as e:
        status_label.config(text="Something Went Wrong ")
        print(e)



        #Main Window
root=tk.Tk()
root.title("Student SignUP")

root.geometry("350x500")
root.config(bg="#ecd7d7")

tk.Label(root, text="Name: ",bg="#ecd7d7",fg="black",anchor=tk.CENTER).grid(row=0,column=0)
name_entry=tk.Entry(root)
name_entry.grid(row=0,column=1)


tk.Label(root,text="Branch: ",bg="#ecd7d7",fg="black").grid(row=1,column=0)
branch_entry=tk.Entry(root)
branch_entry.grid(row=1,column=1)

tk.Label(root,text="Email: ",bg="#ecd7d7",fg="black").grid(row=2,column=0)
email_entry=tk.Entry(root)
email_entry.grid(row=2,column=1)

tk.Label(root,text="Photo: ",bg="#ecd7d7",fg="black").grid(row=3,column=0)
photo_path_entry=tk.Entry(root)
photo_path_entry.grid(row=3,column=1)

tk.Button(root,text="Browse",command=browse_photo).grid(row=3,column=2)

tk.Button(root,text="Submit",command=insert_data).grid(row=4,column=1)
status_label =tk.Label(root , text="")
status_label.grid(row=5,column=1)
root.mainloop()

        


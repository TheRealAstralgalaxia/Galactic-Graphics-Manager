import customtkinter




customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  


app = customtkinter.CTk() 
app.geometry("720x240")
app.title("Galactic Graphics Manager")



def button_function():
    print("Button Has Been Pressed")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Galactic Graphics Manager")
label_1.pack(pady=10, padx=10)

button = customtkinter.CTkButton(master=frame_1, text="Manage My Drivers", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()
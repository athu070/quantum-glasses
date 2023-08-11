import tkinter
import qiskit

#define window
root = tkinter.Tk()
root.title('Quantum Glasses')

#set icon
root.iconbitmap(default='logo.ico')
root.geometry('399x410')
root.resizable(0,0) #blocking the resizing feature

#defining the colours and font
background ='#2c94c8'
buttons='#834558'
special_buttons='#bc3454'
button_font=('Arial',18)
display_font=('Arial',32)

#define frame
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root, bg='black')
display_frame.pack()
button_frame.pack(fill='both',expand=True)

#define the display frame layout
display = tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify='left')
display.pack(padx=3,pady=4)

#define first row of buttons
x_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='X')
y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Y')
z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Z')
x_gate.grid(row=0,column=0,ipadx=45, pady=1)
y_gate.grid(row=0,column=1,ipadx=45, pady=1)
z_gate.grid(row=0,column=1,ipadx=53, pady=1)

#define second row of buttons
Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RX')
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RY')
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RZ')
Rx_gate.grid(row=1,column=1,columnspan=1, sticky='WE',pady=1)
Ry_gate.grid(row=1,column=2,columnspan=1, sticky='WE',pady=1)
Rz_gate.grid(row=1,column=3,columnspan=1, sticky='WE',pady=1)

#define thrid row of buttons
s_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='S')
sd_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='SD')
hardmard = tkinter.Button(button_frame, font=button_font, bg=buttons, text='H')
s_gate.grid(row=2,column=0,columnspan=1,sticky='WE',pady=1)
sd_gate.grid(row=2,column=1,sticky='WE', pady=1)
hardmard.grid(row=2, column=2, rowspan=2, sticky='WENS', pady=1)

#define the fifth row of buttons
t_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='T')
td_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='TD')
t_gate.grid(row=3,column=0,sticky='WE',pady=1)
td_gate.grid(row=3, column=1, sticky='WE', pady=1)

#define the quit and visualize buttons
quit = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='quit', command=root.destroy)
visualize = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='Visualize')
quit.grid(row=4,column=0,columnspan=2,sticky='WE',ipadx=5, pady=1)
visualize.grid(row=4,column=2,columnspan=1,sticky='WE',ipadx=8, pady=1)

#define the clear button
clear_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='Clear')
clear_button.grid(row=5, column=0, columnspan=3, sticky='WE')

#define the about button
about_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='About')
about_button.grid(row=6,column=0,columnspan=3,sticky='WE')

#run the main
root.mainloop()
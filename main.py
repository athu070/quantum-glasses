import tkinter
from qiskit import QuantumCircuit
from tkinter import LEFT, END, DISABLED

#define window
root = tkinter.Tk()
root.title('Quantum Glasses')

#set icon
root.iconbitmap(default='logo.ico')
root.geometry('399x425')
root.resizable(0,0) #blocking the resizing feature

#defining the colours and font
background ='#2c94c8'
buttons='#834558'
special_buttons='#bc3454'
button_font=('Arial',18)
display_font=('Arial',32)

# Initialize the Quantum Circuit
def initialize_circuit():
    global circuit
    circuit = QuantumCircuit(1)

initialize_circuit()
theta = 0

#define function for gates

def display_gate(gate_input):
    """
    Adds a corresponding gate notation in the display to track the operations.
    if the number of operation reach ten, all gate buttons are disabled.
    """

    #insert the defined gate
    display.insert(END,gate_input)

    #check if the number of operation has reached ten, if yes,
    #disable all the gate buttons
    input_gates = display.get()
    num_gates_pressed = len(input_gates)
    list_input_gates = list(input_gates)
    search_word = ["R","D"]
    count_double_valued_gates = [list_input_gates.count(i) for i in search_word]
    num_gates_pressed-=sum(count_double_valued_gates)
    if num_gates_pressed==10:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hardmard]
        for gate in gates:
            gate.config(state=DISABLED)

#define Function for about button
def about():
    """
    Display the info about the project!
    """

    info = tkinter.Tk()
    info.title('About')
    info.geometry('650x470')
    info.resizable(0,0)

    text = tkinter.Text(info, height=20, width=20)

    #create label
    label = tkinter.Label(info, text= "About quantum glasses:")
    label.config(font=("Arial", 14))

    text_to_display = """
    About: Visualization tool for single Qubit Rotation on Bloch Sphere

    Created by : G-31
    Created by using Python, Tkinter, Qiskit

    Info about the gate buttons and corresponding qiskit commands:

    X = flips the state of qubit -
    Y = rotates the state vector about Y-axis -
    Z = flips the phase by PI radians - 
    Rx = parameterized rotation about the X axis -
    Ry = parameterized rotation about the Y axis -
    Rz = parameterized rotation about the Z axis -
    S = rotates the state vector about Z axis by PI/2 radians -
    T = rotates the state vector about Z axis by PI/4 radians -
    Sd = rotates the state vector about Z axis by PI/2 radians -
    Td = rotates the state vector about Z axis by PI/4 radians -
    H = creates the state of superposition -

    For Rx, Ry, and Rz
    theta(rotation_angle) allowed range in the app is [-2*PI,2*PI]

    In case of a Visualization Error, the app closes automatically.
    This indicates that visualization of your circuit is not possible.

    At a time, only ten operations can be visualized.
    """

    label.pack()
    text.pack(fill='both',expand=True)

#Insert the text
    text.insert(END, text_to_display)

#run
    info.mainloop()


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
y_gate.grid(row=0,column=1,ipadx=45, pady=1,sticky='WE')
z_gate.grid(row=0,column=2,ipadx=53, pady=1, sticky='E')

#define second row of buttons
Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RX')
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RY')
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RZ')
Rx_gate.grid(row=1,column=0,columnspan=1, sticky='WE',pady=1)
Ry_gate.grid(row=1,column=1,columnspan=1, sticky='WE',pady=1)
Rz_gate.grid(row=1,column=2,columnspan=1, sticky='WE',pady=1)

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
about_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='About', command=about)
about_button.grid(row=6,column=0,columnspan=3,sticky='WE')

#run the main
root.mainloop()
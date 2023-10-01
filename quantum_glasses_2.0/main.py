# Import necessary libraries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from qiskit import QuantumCircuit, transpile, execute, Aer
from qiskit.visualization import plot_bloch_multivector, plot_state_city, plot_state_qsphere, plot_state_paulivec
from tkinter import *
from tkinter import ttk

# Function to visualize the circuit
def visualize_circuit():
    n_qubits = 2
    qc = QuantumCircuit(n_qubits)
    qc.h(0)  # Hadamard gate on qubit 0
    qc.x(1)  # X gate on qubit 1
    qc.cx(0, 1)  # CNOT gate (controlled-X) between qubit 0 and qubit 1

    # Visualize the circuit
    circuit_info_label.config(text="Quantum Circuit:\n" + str(qc))

    # Visualize the circuit diagram
    fig, ax = plt.subplots()
    qc.draw(output="mpl", ax=ax)
    ax.set_title("Quantum Circuit Diagram")
    
    # Create a canvas for the circuit diagram
    canvas = FigureCanvasTkAgg(fig, master=circuit_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    canvas_widget.draw()

# Function to visualize Bloch spheres
def visualize_bloch_spheres():
    simulator = Aer.get_backend('statevector_simulator')
    result = execute(qc, simulator).result().get_statevector()

    for i in range(n_qubits):
        fig, ax = plt.subplots()
        plot_bloch_multivector(result, ax=ax, title=f"Bloch Sphere Qubit {i}")
        
        # Create a canvas for the Bloch sphere
        canvas = FigureCanvasTkAgg(fig, master=bloch_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
        canvas_widget.draw()

# Function to visualize state vector
def visualize_state_vector():
    simulator = Aer.get_backend('statevector_simulator')
    result = execute(qc, simulator).result().get_statevector()

    fig, ax = plt.subplots()
    plot_state_city(result, ax=ax, title="State City")
    
    # Create a canvas for the State City visualization
    canvas = FigureCanvasTkAgg(fig, master=state_vector_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    canvas_widget.draw()

    fig, ax = plt.subplots()
    plot_state_qsphere(result, ax=ax, title="State Q-sphere")
    
    # Create a canvas for the State Q-sphere visualization
    canvas = FigureCanvasTkAgg(fig, master=state_vector_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    canvas_widget.draw()

    fig, ax = plt.subplots()
    plot_state_paulivec(result, ax=ax, title="Pauli Vector Representation")
    
    # Create a canvas for the Pauli Vector visualization
    canvas = FigureCanvasTkAgg(fig, master=state_vector_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    canvas_widget.draw()

# Create the main window
root = Tk()
root.title("Quantum Gate Visualizer")

# Create frames for different visualizations
circuit_frame = ttk.Frame(root)
circuit_frame.pack(side=LEFT, padx=10, pady=10)
bloch_frame = ttk.Frame(root)
bloch_frame.pack(side=LEFT, padx=10, pady=10)
state_vector_frame = ttk.Frame(root)
state_vector_frame.pack(side=LEFT, padx=10, pady=10)

# Create a button to trigger visualization
visualize_button = ttk.Button(root, text="Visualize", command=lambda: [visualize_circuit(), visualize_bloch_spheres(), visualize_state_vector()])
visualize_button.pack(padx=10, pady=10)

# Label to display circuit information
circuit_info_label = Label(circuit_frame, text="", justify=LEFT)
circuit_info_label.pack()

# Start the GUI main loop
root.mainloop()

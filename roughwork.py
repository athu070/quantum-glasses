from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition

circuit = QuantumCircuit(1,1)
circuit.x(0)
visualize_transition(circuit)
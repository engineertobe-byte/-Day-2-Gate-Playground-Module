"""
Gate Playground Module — QAI Labs Week 1, Day 2
Author: [Your Name]
Qiskit Version: 2.3.0 (Modern API: Statevector)
Interview Payoff: Fluency with unitary gates — the #1 thing interviewers sanity-check first.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np


def apply_gate(gate_name: str, initial_state: str = "0") -> Statevector:
    """
    Applies a specific quantum gate to |0⟩ or |1⟩ and returns the resulting Statevector.
    
    Args:
        gate_name (str): One of 'X', 'Z', 'H', 'CNOT', 'Toffoli'
        initial_state (str): '0' for |0⟩, '1' for |1⟩ (applied to the first qubit)
        
    Returns:
        Statevector: The resulting quantum state after gate application.
    """
    # Determine number of qubits needed based on the gate
    if gate_name == "Toffoli":
        n_qubits = 3
    elif gate_name == "CNOT":
        n_qubits = 2
    else:
        n_qubits = 1
        
    qc = QuantumCircuit(n_qubits)
    
    # Prepare initial state |1⟩ if requested (default is |0...0⟩)
    if initial_state == "1":
        qc.x(0)
    
    # Apply the requested unitary gate
    if gate_name == "X":
        qc.x(0)
    elif gate_name == "Z":
        qc.z(0)
    elif gate_name == "H":
        qc.h(0)
    elif gate_name == "CNOT":
        qc.cx(0, 1)
    elif gate_name == "Toffoli":
        qc.ccx(0, 1, 2)
    else:
        raise ValueError(f"Unknown gate: {gate_name}. Supported: X, Z, H, CNOT, Toffoli.")
    
    # Extract Statevector using Modern Qiskit 2.x API (no deprecated execute)
    sv = Statevector(qc)
    
    # Format and print visual output
    print(f"\n{'='*50}")
    print(f"Gate Applied : {gate_name}")
    print(f"Initial State: |{initial_state}⟩" + (" (on qubit 0)" if n_qubits > 1 else ""))
    print(f"Statevector  : {np.round(sv.data, 4)}")
    print(f"Probabilities: {np.round(np.abs(sv.data)**2, 4)}")
    print(f"{'='*50}")
    
    return sv


if __name__ == "__main__":
    print("🔬 GATE PLAYGROUND MODULE — DAY 2 DEMO")
    print("Demonstrating all 5 gates on both |0⟩ and |1⟩ initial states.\n")
    
    gates_to_demo = ["X", "Z", "H", "CNOT", "Toffoli"]
    initial_states = ["0", "1"]
    
    for gate in gates_to_demo:
        for state in initial_states:
            try:
                apply_gate(gate, state)
            except Exception as e:
                print(f"Error running {gate} on |{state}⟩: {e}")

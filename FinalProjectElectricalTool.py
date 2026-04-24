"""
Interactive Electrical Calculator Tool
Supports: Ohm's Law (V, I, R), Power (P, V, I, R), and Capacitance calculations
"""

def get_float_input(prompt: str) -> float:
    """Safely get float input from user with validation."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Value must be non-negative. Try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def ohms_law_menu() -> None:
    """Calculate voltage, current, or resistance using Ohm's Law (V = I * R)."""
    print("\n--- Ohm's Law Calculator ---")
    print("1. Calculate Voltage (V = I × R)")
    print("2. Calculate Current (I = V ÷ R)")
    print("3. Calculate Resistance (R = V ÷ I)")
    
    choice = input("Select (1-3): ").strip()
    
    if choice == "1":
        current = get_float_input("Enter Current (Amps): ")
        resistance = get_float_input("Enter Resistance (Ohms): ")
        if resistance == 0:
            print("Error: Resistance cannot be zero.")
            return
        voltage = current * resistance
        print(f"Voltage: {voltage:.2f} V")
    
    elif choice == "2":
        voltage = get_float_input("Enter Voltage (Volts): ")
        resistance = get_float_input("Enter Resistance (Ohms): ")
        if resistance == 0:
            print("Error: Resistance cannot be zero.")
            return
        current = voltage / resistance
        print(f"Current: {current:.2f} A")
    
    elif choice == "3":
        voltage = get_float_input("Enter Voltage (Volts): ")
        current = get_float_input("Enter Current (Amps): ")
        if current == 0:
            print("Error: Current cannot be zero.")
            return
        resistance = voltage / current
        print(f"Resistance: {resistance:.2f} Ω")
    
    else:
        print("Error: Invalid selection.")

def power_menu() -> None:
    """Calculate power, voltage, current, or resistance using Power formulas."""
    print("\n--- Power Calculator ---")
    print("1. Calculate Power (P = V × I)")
    print("2. Calculate Power (P = I² × R)")
    print("3. Calculate Voltage (V = P ÷ I)")
    print("4. Calculate Current (I = P ÷ V)")
    
    choice = input("Select (1-4): ").strip()
    
    if choice == "1":
        voltage = get_float_input("Enter Voltage (Volts): ")
        current = get_float_input("Enter Current (Amps): ")
        power = voltage * current
        print(f"Power: {power:.2f} W")
    
    elif choice == "2":
        current = get_float_input("Enter Current (Amps): ")
        resistance = get_float_input("Enter Resistance (Ohms): ")
        power = (current ** 2) * resistance
        print(f"Power: {power:.2f} W")
    
    elif choice == "3":
        power = get_float_input("Enter Power (Watts): ")
        current = get_float_input("Enter Current (Amps): ")
        if current == 0:
            print("Error: Current cannot be zero.")
            return
        voltage = power / current
        print(f"Voltage: {voltage:.2f} V")
    
    elif choice == "4":
        power = get_float_input("Enter Power (Watts): ")
        voltage = get_float_input("Enter Voltage (Volts): ")
        if voltage == 0:
            print("Error: Voltage cannot be zero.")
            return
        current = power / voltage
        print(f"Current: {current:.2f} A")
    
    else:
        print("Error: Invalid selection.")

def capacitance_menu() -> None:
    """Calculate capacitance using C = ε₀ × εᵣ × A / d."""
    print("\n--- Capacitance Calculator ---")
    print("1. Calculate Capacitance (C = ε₀ × εᵣ × A / d)")
    print("2. Calculate Energy (E = 0.5 × C × V²)")
    
    choice = input("Select (1-2): ").strip()
    
    epsilon_0 = 8.854e-12  # Permittivity of free space (F/m)
    
    if choice == "1":
        epsilon_r = get_float_input("Enter Relative Permittivity (εᵣ): ")
        area = get_float_input("Enter Plate Area (m²): ")
        if area == 0:
            print("Error: Area cannot be zero.")
            return
        distance = get_float_input("Enter Distance Between Plates (m): ")
        if distance == 0:
            print("Error: Distance cannot be zero.")
            return
        capacitance = (epsilon_0 * epsilon_r * area) / distance
        print(f"Capacitance: {capacitance:.2e} F ({capacitance * 1e12:.2f} pF)")
    
    elif choice == "2":
        capacitance = get_float_input("Enter Capacitance (Farads): ")
        voltage = get_float_input("Enter Voltage (Volts): ")
        energy = 0.5 * capacitance * (voltage ** 2)
        print(f"Energy: {energy:.2e} J")
    
    else:
        print("Error: Invalid selection.")

def main() -> None:
    """Main menu loop for the electrical calculator tool."""
    print("=" * 40)
    print("  Electrical Tool - Interactive Calculator")
    print("=" * 40)
    
    while True:
        print("\nMain Menu:")
        print("1. Ohm's Law (V, I, R)")
        print("2. Power Calculations (P, V, I, R)")
        print("3. Capacitance Calculations (C, E)")
        print("4. Exit")
        
        choice = input("Select (1-4): ").strip()
        
        if choice == "1":
            ohms_law_menu()
        elif choice == "2":
            power_menu()
        elif choice == "3":
            capacitance_menu()
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Error: Invalid selection. Try again.")

if __name__ == "__main__":
    main()
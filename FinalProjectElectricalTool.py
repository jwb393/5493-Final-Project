import tkinter as tk
from tkinter import ttk, messagebox

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
    """Calc voltage, current, or resistance using Ohm's Law (V = I * R)."""
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
    """Calc power, voltage, current, or resistance using Power formulas."""
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
        print(f"Capacitance: {capacitance:.2e} F({capacitance * 1e12:.2f} pF)")

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

    def create_gui():
        """Create a GUI version of the electrical calculator tool."""
        root = tk.Tk()
        root.title("Electrical Tool - Interactive Calculator")
        root.geometry("520x420")

        def show_ohms_law():
            ohms_window = tk.Toplevel(root)
            ohms_window.title("Ohm's Law Calculator")
            ohms_window.geometry("420x380")

            ttk.Label(ohms_window, text="Ohm's Law Calculator").pack(pady=10)
            mode_var = tk.StringVar(value="voltage")

            ttk.Radiobutton(ohms_window, text="Calculate Voltage (V = I × R)", variable=mode_var, value="voltage",
                            command=lambda: update_fields()).pack(anchor="w", padx=20)
            ttk.Radiobutton(ohms_window, text="Calculate Current (I = V ÷ R)", variable=mode_var, value="current",
                            command=lambda: update_fields()).pack(anchor="w", padx=20)
            ttk.Radiobutton(ohms_window, text="Calculate Resistance (R = V ÷ I)", variable=mode_var, value="resistance",
                            command=lambda: update_fields()).pack(anchor="w", padx=20)

            field_frame = ttk.Frame(ohms_window)
            field_frame.pack(pady=15, padx=20, fill="x")

            label1 = ttk.Label(field_frame, text="Current (A):")
            label1.pack(anchor="w")
            entry1 = ttk.Entry(field_frame)
            entry1.pack(fill="x")

            label2 = ttk.Label(field_frame, text="Resistance (Ω):")
            label2.pack(anchor="w", pady=(10, 0))
            entry2 = ttk.Entry(field_frame)
            entry2.pack(fill="x")

            def update_fields():
                mode = mode_var.get()
                if mode == "voltage":
                    label1.config(text="Current (A):")
                    label2.config(text="Resistance (Ω):")
                elif mode == "current":
                    label1.config(text="Voltage (V):")
                    label2.config(text="Resistance (Ω):")
                else:
                    label1.config(text="Voltage (V):")
                    label2.config(text="Current (A):")
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)

            def calculate_ohms():
                try:
                    a = float(entry1.get())
                    b = float(entry2.get())
                    mode = mode_var.get()
                    if mode == "voltage":
                        result = a * b
                        message = f"Voltage: {result:.2f} V"
                    elif mode == "current":
                        if b == 0:
                            raise ZeroDivisionError
                        result = a / b
                        message = f"Current: {result:.2f} A"
                    else:
                        if b == 0:
                            raise ZeroDivisionError
                        result = a / b
                        message = f"Resistance: {result:.2f} Ω"
                    messagebox.showinfo("Result", message)
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers")
                except ZeroDivisionError:
                    messagebox.showerror("Error", "Division by zero is not allowed")

            update_fields()
            ttk.Button(ohms_window, text="Calculate", command=calculate_ohms).pack(pady=10)

        def show_power_calculations():
            power_window = tk.Toplevel(root)
            power_window.title("Power Calculator")
            power_window.geometry("420x420")

            ttk.Label(power_window, text="Power Calculator").pack(pady=10)
            option_var = tk.StringVar(value="1")

            ttk.Radiobutton(power_window, text="P = V × I", variable=option_var, value="1",
                            command=lambda: update_power_fields()).pack(anchor="w", padx=20)
            ttk.Radiobutton(power_window, text="P = I² × R", variable=option_var, value="2",
                            command=lambda: update_power_fields()).pack(anchor="w", padx=20)
            ttk.Radiobutton(power_window, text="V = P ÷ I", variable=option_var, value="3",
                            command=lambda: update_power_fields()).pack(anchor="w", padx=20)
            ttk.Radiobutton(power_window, text="I = P ÷ V", variable=option_var, value="4",
                            command=lambda: update_power_fields()).pack(anchor="w", padx=20)

            power_frame = ttk.Frame(power_window)
            power_frame.pack(pady=15, padx=20, fill="x")

            power_label_a = ttk.Label(power_frame, text="Voltage (V):")
            power_label_a.pack(anchor="w")
            power_entry_a = ttk.Entry(power_frame)
            power_entry_a.pack(fill="x")

            power_label_b = ttk.Label(power_frame, text="Current (A):")
            power_label_b.pack(anchor="w", pady=(10, 0))
            power_entry_b = ttk.Entry(power_frame)
            power_entry_b.pack(fill="x")

            def update_power_fields():
                option = option_var.get()
                if option == "1":
                    power_label_a.config(text="Voltage (V):")
                    power_label_b.config(text="Current (A):")
                elif option == "2":
                    power_label_a.config(text="Current (A):")
                    power_label_b.config(text="Resistance (Ω):")
                elif option == "3":
                    power_label_a.config(text="Power (W):")
                    power_label_b.config(text="Current (A):")
                else:
                    power_label_a.config(text="Power (W):")
                    power_label_b.config(text="Voltage (V):")
                power_entry_a.delete(0, tk.END)
                power_entry_b.delete(0, tk.END)

            def calculate_power():
                try:
                    a = float(power_entry_a.get())
                    b = float(power_entry_b.get())
                    option = option_var.get()
                    if option == "1":
                        result = a * b
                        message = f"Power: {result:.2f} W"
                    elif option == "2":
                        result = (a ** 2) * b
                        message = f"Power: {result:.2f} W"
                    elif option == "3":
                        if b == 0:
                            raise ZeroDivisionError
                        result = a / b
                        message = f"Voltage: {result:.2f} V"
                    else:
                        if b == 0:
                            raise ZeroDivisionError
                        result = a / b
                        message = f"Current: {result:.2f} A"
                    messagebox.showinfo("Result", message)
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers")
                except ZeroDivisionError:
                    messagebox.showerror("Error", "Division by zero is not allowed")

            update_power_fields()
            ttk.Button(power_window, text="Calculate", command=calculate_power).pack(pady=10)

        def show_capacitance_calculations():
            cap_window = tk.Toplevel(root)
            cap_window.title("Capacitance Calculator")
            cap_window.geometry("420x360")

            ttk.Label(cap_window, text="Capacitance Calculator").pack(pady=10)
            cap_option = tk.StringVar(value="1")

            ttk.Radiobutton(cap_window, text="Calculate Capacitance (C = ε₀ × εᵣ × A / d)", variable=cap_option,
                            value="1", command=lambda: update_cap_fields()).pack(anchor="w", padx=20)
            ttk.Radiobutton(cap_window, text="Calculate Energy (E = 0.5 × C × V²)", variable=cap_option, value="2",
                            command=lambda: update_cap_fields()).pack(anchor="w", padx=20)

            cap_frame = ttk.Frame(cap_window)
            cap_frame.pack(pady=15, padx=20, fill="x")

            cap_label1 = ttk.Label(cap_frame, text="Relative Permittivity (εᵣ):")
            cap_label1.pack(anchor="w")
            cap_entry1 = ttk.Entry(cap_frame)
            cap_entry1.pack(fill="x")

            cap_label2 = ttk.Label(cap_frame, text="Plate Area (m²):")
            cap_label2.pack(anchor="w", pady=(10, 0))
            cap_entry2 = ttk.Entry(cap_frame)
            cap_entry2.pack(fill="x")

            cap_label3 = ttk.Label(cap_frame, text="Distance Between Plates (m):")
            cap_label3.pack(anchor="w", pady=(10, 0))
            cap_entry3 = ttk.Entry(cap_frame)
            cap_entry3.pack(fill="x")

            def update_cap_fields():
                option = cap_option.get()
                if option == "1":
                    cap_label1.config(text="Relative Permittivity (εᵣ):")
                    cap_label2.config(text="Plate Area (m²):")
                    cap_label3.config(text="Distance Between Plates (m):")
                    cap_label3.pack(anchor="w", pady=(10, 0))
                    cap_entry3.pack(fill="x")
                else:
                    cap_label1.config(text="Capacitance (F):")
                    cap_label2.config(text="Voltage (V):")
                    cap_label3.pack_forget()
                    cap_entry3.pack_forget()
                cap_entry1.delete(0, tk.END)
                cap_entry2.delete(0, tk.END)
                if option == "1":
                    cap_entry3.delete(0, tk.END)

            def calculate_capacitance():
                try:
                    option = cap_option.get()
                    if option == "1":
                        epsilon_r = float(cap_entry1.get())
                        area = float(cap_entry2.get())
                        distance = float(cap_entry3.get())
                        if area == 0 or distance == 0:
                            raise ZeroDivisionError
                        epsilon_0 = 8.854e-12
                        capacitance = (epsilon_0 * epsilon_r * area) / distance
                        messagebox.showinfo("Result", f"Capacitance: {capacitance:.2e} F ({capacitance * 1e12:.2f} pF)")
                    else:
                        capacitance = float(cap_entry1.get())
                        voltage = float(cap_entry2.get())
                        energy = 0.5 * capacitance * (voltage ** 2)
                        messagebox.showinfo("Result", f"Energy: {energy:.2e} J")
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers")
                except ZeroDivisionError:
                    messagebox.showerror("Error", "Area and distance must be non-zero")

            update_cap_fields()
            ttk.Button(cap_window, text="Calculate", command=calculate_capacitance).pack(pady=10)

        ttk.Button(root, text="Ohm's Law", command=show_ohms_law).pack(pady=10)
        ttk.Button(root, text="Power Calculations", command=show_power_calculations).pack(pady=10)
        ttk.Button(root, text="Capacitance Calculations", command=show_capacitance_calculations).pack(pady=10)
        ttk.Button(root, text="Exit", command=root.quit).pack(pady=10)

        root.mainloop()

    create_gui()

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

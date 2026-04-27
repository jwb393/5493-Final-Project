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
    """Calculate capacitance and resistance in series/parallel."""
    print("\n--- Capacitance/Resistance Calculator ---")
    print("1. Capacitance in Series")
    print("2. Capacitance in Parallel")
    print("3. Resistance in Series")
    print("4. Resistance in Parallel")

    choice = input("Select (1-4): ").strip()

    if choice in ["1", "2", "3", "4"]:
        values_str = input("Enter values separated by commas: ").strip()
        try:

            values = [float(x.strip()) for x in values_str.split(',') if x.strip()]
            if not values:
                print("Error: No valid values entered.")
                return
        except ValueError:
            print("Error: Invalid input. Please enter numbers separated by commas.")
            return

        if choice == "1":  # Capacitance in Series
            total = sum(1 / v for v in values)
            if total == 0:
                print("Error: Division by zero.")
                return
            result = 1 / total
            print(f"Total Capacitance in Series: {result:.2e} F")
        elif choice == "2":  # Capacitance in Parallel
            result = sum(values)
            print(f"Total Capacitance in Parallel: {result:.2e} F")
        elif choice == "3":  # Resistance in Series
            result = sum(values)
            print(f"Total Resistance in Series: {result:.2f} Ω")
        elif choice == "4":  # Resistance in Parallel
            total = sum(1 / v for v in values)
            if total == 0:
                print("Error: Division by zero.")
                return
            result = 1 / total
            print(f"Total Resistance in Parallel: {result:.2f} Ω")
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
        root.geometry("520x500")

        # Calculator selection
        ttk.Label(root, text="Select Calculator:").pack(pady=10)
        calc_var = tk.StringVar(value="Ohm's Law")
        calc_combo = ttk.Combobox(root, textvariable=calc_var,
                                  values=["Ohm's Law", "Power", "Series/Parallel"], state="readonly")
        calc_combo.pack(pady=5)
        calc_combo.bind("<<ComboboxSelected>>", lambda e: update_calculator())

        # Mode selection frame
        mode_frame = ttk.Frame(root)
        mode_frame.pack(pady=10, padx=20, fill="x")

        mode_var = tk.StringVar()

        # Input fields frame
        fields_frame = ttk.Frame(root)
        fields_frame.pack(pady=10, padx=20, fill="x")

        def update_calculator():
            # Clear previous widgets
            for widget in mode_frame.winfo_children():
                widget.destroy()
            for widget in fields_frame.winfo_children():
                widget.destroy()

            calc = calc_var.get()
            if calc == "Ohm's Law":
                ttk.Label(mode_frame, text="Ohm's Law Calculator").pack(pady=5)
                mode_var.set("voltage")
                ttk.Radiobutton(mode_frame, text="Calculate Voltage (V = I × R)", variable=mode_var,
                                value="voltage", command=update_fields).pack(anchor="w", padx=20)
                ttk.Radiobutton(mode_frame, text="Calculate Current (I = V ÷ R)", variable=mode_var,
                                value="current", command=update_fields).pack(anchor="w", padx=20)
                ttk.Radiobutton(mode_frame, text="Calculate Resistance (R = V ÷ I)", variable=mode_var,
                                value="resistance", command=update_fields).pack(anchor="w", padx=20)
            elif calc == "Power":
                ttk.Label(mode_frame, text="Power Calculator").pack(pady=5)
                mode_var.set("1")
                ttk.Radiobutton(mode_frame, text="P = V × I", variable=mode_var, value="1",
                                command=update_fields).pack(anchor="w", padx=20)
                ttk.Radiobutton(mode_frame, text="P = I² × R", variable=mode_var,
                                value="2", command=update_fields).pack(anchor="w", padx=20)
                ttk.Radiobutton(mode_frame, text="V = P ÷ I", variable=mode_var, value="3",
                                command=update_fields).pack(anchor="w", padx=20)
                ttk.Radiobutton(mode_frame, text="I = P ÷ V", variable=mode_var, value="4",
                                command=update_fields).pack(anchor="w", padx=20)
            elif calc == "Series/Parallel":
                ttk.Label(mode_frame, text="Capacitance/Resistance Calculator").pack(pady=5)
                mode_var.set("cap_series")
                ttk.Radiobutton(mode_frame, text="Capacitance in Series (F)", variable=mode_var,
                                value="cap_series", command=update_fields).pack(anchor="w", padx=20)
                ttk.Radiobutton(mode_frame, text="Capacitance in Parallel (F)", variable=mode_var,
                                value="cap_parallel", command=update_fields).pack(anchor="w", padx=20)
                ttk.Radiobutton(mode_frame, text="Resistance in Series (Ω)", variable=mode_var,
                                value="res_series", command=update_fields).pack(anchor="w", padx=20)
                ttk.Radiobutton(mode_frame, text="Resistance in Parallel (Ω)", variable=mode_var,
                                value="res_parallel", command=update_fields).pack(anchor="w", padx=20)

            update_fields()

        def update_fields():
            # Clear fields
            for widget in fields_frame.winfo_children():
                widget.destroy()

            calc = calc_var.get()
            mode = mode_var.get()

            if calc == "Ohm's Law":
                if mode == "voltage":
                    ttk.Label(fields_frame, text="Current (A):").pack(anchor="w")
                    entry1 = ttk.Entry(fields_frame)
                    entry1.pack(fill="x")
                    ttk.Label(fields_frame, text="Resistance (Ω):").pack(anchor="w", pady=(10, 0))
                    entry2 = ttk.Entry(fields_frame)
                    entry2.pack(fill="x")
                elif mode == "current":
                    ttk.Label(fields_frame, text="Voltage (V):").pack(anchor="w")
                    entry1 = ttk.Entry(fields_frame)
                    entry1.pack(fill="x")
                    ttk.Label(fields_frame, text="Resistance (Ω):").pack(anchor="w", pady=(10, 0))
                    entry2 = ttk.Entry(fields_frame)
                    entry2.pack(fill="x")
                else:  # resistance
                    ttk.Label(fields_frame, text="Voltage (V):").pack(anchor="w")
                    entry1 = ttk.Entry(fields_frame)
                    entry1.pack(fill="x")
                    ttk.Label(fields_frame, text="Current (A):").pack(anchor="w", pady=(10, 0))
                    entry2 = ttk.Entry(fields_frame)
                    entry2.pack(fill="x")
            elif calc == "Power":
                if mode == "1":
                    ttk.Label(fields_frame, text="Voltage (V):").pack(anchor="w")
                    entry1 = ttk.Entry(fields_frame)
                    entry1.pack(fill="x")
                    ttk.Label(fields_frame, text="Current (A):").pack(anchor="w", pady=(10, 0))
                    entry2 = ttk.Entry(fields_frame)
                    entry2.pack(fill="x")
                elif mode == "2":
                    ttk.Label(fields_frame, text="Current (A):").pack(anchor="w")
                    entry1 = ttk.Entry(fields_frame)
                    entry1.pack(fill="x")
                    ttk.Label(fields_frame, text="Resistance (Ω):").pack(anchor="w", pady=(10, 0))
                    entry2 = ttk.Entry(fields_frame)
                    entry2.pack(fill="x")
                elif mode == "3":
                    ttk.Label(fields_frame, text="Power (W):").pack(anchor="w")
                    entry1 = ttk.Entry(fields_frame)
                    entry1.pack(fill="x")
                    ttk.Label(fields_frame, text="Current (A):").pack(anchor="w", pady=(10, 0))
                    entry2 = ttk.Entry(fields_frame)
                    entry2.pack(fill="x")
                else:  # 4
                    ttk.Label(fields_frame, text="Power (W):").pack(anchor="w")
                    entry1 = ttk.Entry(fields_frame)
                    entry1.pack(fill="x")
                    ttk.Label(fields_frame, text="Voltage (V):").pack(anchor="w", pady=(10, 0))
                    entry2 = ttk.Entry(fields_frame)
                    entry2.pack(fill="x")
            elif calc == "Series/Parallel":
                if mode in ["cap_series", "cap_parallel", "res_series", "res_parallel"]:
                    ttk.Label(fields_frame, text="Enter values separated by commas:").pack(anchor="w")
                    entry1 = ttk.Entry(fields_frame)
                    entry1.pack(fill="x")

        def calculate():
            try:
                calc = calc_var.get()
                mode = mode_var.get()
                entries = [w for w in fields_frame.winfo_children() if isinstance(w, ttk.Entry)]
                
                # Handle Capacitance separately (comma-separated values)
                if calc == "Series/Parallel":
                    values_str = entries[0].get()
                    values = [float(x.strip()) for x in values_str.split(',') if x.strip()]
                    if not values:
                        raise ValueError("No values entered")
                    if mode == "cap_series":
                        total = sum(1 / v for v in values)
                        if total == 0:
                            raise ZeroDivisionError
                        result = 1 / total
                        message = f"Total Capacitance in Series: {result:.2e} F"
                    elif mode == "cap_parallel":
                        result = sum(values)
                        message = f"Total Capacitance in Parallel: {result:.2e} F"
                    elif mode == "res_series":
                        result = sum(values)
                        message = f"Total Resistance in Series: {result:.2f} Ω"
                    elif mode == "res_parallel":
                        total = sum(1 / v for v in values)
                        if total == 0:
                            raise ZeroDivisionError
                        result = 1 / total
                        message = f"Total Resistance in Parallel: {result:.2f} Ω"
                    messagebox.showinfo("Result", message)
                    return

                # Handle Ohm's Law and Power (individual numeric entries)
                values = [float(e.get()) for e in entries]

                if calc == "Ohm's Law":
                    a, b = values
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
                elif calc == "Power":
                    a, b = values
                    if mode == "1":
                        result = a * b
                        message = f"Power: {result:.2f} W"
                    elif mode == "2":
                        result = (a ** 2) * b
                        message = f"Power: {result:.2f} W"
                    elif mode == "3":
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

        ttk.Button(root, text="Calculate", command=calculate).pack(pady=20)
        ttk.Button(root, text="Exit", command=root.quit).pack(pady=5)

        update_calculator()
        root.mainloop()

    create_gui()


if __name__ == "__main__":
    main()

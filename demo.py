import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime

# Importar las clases y diccionarios del código original
from principal import CUENTAS, AsientoContable, DiarioContable, MayorContable, BalanzaComprobacion

class ContabilidadGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Registro Contable")
        self.master.geometry("800x600")

        self.diario = DiarioContable()
        self.mayor = MayorContable()

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Botones principales
        ttk.Button(main_frame, text="Agregar Asiento", command=self.agregar_asiento).grid(row=0, column=0, pady=5)
        ttk.Button(main_frame, text="Mostrar Diario", command=self.mostrar_diario).grid(row=0, column=1, pady=5)
        ttk.Button(main_frame, text="Mostrar Mayor", command=self.mostrar_mayor).grid(row=0, column=2, pady=5)
        ttk.Button(main_frame, text="Balanza de Comprobación", command=self.mostrar_balanza).grid(row=0, column=3, pady=5)

        # Área de texto para mostrar información
        self.text_area = tk.Text(main_frame, height=30, width=90)
        self.text_area.grid(row=1, column=0, columnspan=4, pady=10)

        # Scrollbar para el área de texto
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.text_area.yview)
        scrollbar.grid(row=1, column=4, sticky="ns")
        self.text_area.configure(yscrollcommand=scrollbar.set)

    def agregar_asiento(self):
        asiento_window = tk.Toplevel(self.master)
        asiento_window.title("Agregar Asiento")
        asiento_window.geometry("400x500")

        ttk.Label(asiento_window, text="Fecha (dd/mm/yyyy):").pack()
        fecha_entry = ttk.Entry(asiento_window)
        fecha_entry.pack()

        ttk.Label(asiento_window, text="Glosa:").pack()
        glosa_entry = ttk.Entry(asiento_window)
        glosa_entry.pack()

        debe_frame = ttk.LabelFrame(asiento_window, text="Debe")
        debe_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        haber_frame = ttk.LabelFrame(asiento_window, text="Haber")
        haber_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        debe_entries = []
        haber_entries = []

        def add_entry(frame, entries):
            cuenta_entry = ttk.Entry(frame, width=10)
            monto_entry = ttk.Entry(frame, width=10)
            cuenta_entry.pack(side="left", padx=5)
            monto_entry.pack(side="left", padx=5)
            entries.append((cuenta_entry, monto_entry))

        ttk.Button(debe_frame, text="+", command=lambda: add_entry(debe_frame, debe_entries)).pack()
        ttk.Button(haber_frame, text="+", command=lambda: add_entry(haber_frame, haber_entries)).pack()

        def guardar_asiento():
            fecha = fecha_entry.get()
            glosa = glosa_entry.get()
            cuentas_debe = []
            montos_debe = []
            cuentas_haber = []
            montos_haber = []

            for cuenta_entry, monto_entry in debe_entries:
                cuenta = cuenta_entry.get()
                monto = monto_entry.get()
                if cuenta and monto:
                    cuentas_debe.append(cuenta)
                    montos_debe.append(float(monto))

            for cuenta_entry, monto_entry in haber_entries:
                cuenta = cuenta_entry.get()
                monto = monto_entry.get()
                if cuenta and monto:
                    cuentas_haber.append(cuenta)
                    montos_haber.append(float(monto))

            asiento = AsientoContable(fecha, glosa, cuentas_debe, cuentas_haber, montos_debe, montos_haber)
            self.diario.agregar_asiento(asiento)
            self.mayor.registrar_asiento_mayor(asiento)
            messagebox.showinfo("Éxito", "Asiento agregado correctamente")
            asiento_window.destroy()

        ttk.Button(asiento_window, text="Guardar Asiento", command=guardar_asiento).pack(pady=10)

    def mostrar_diario(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "--- Diario Contable ---\n\n")
        for asiento in self.diario.asientos:
            self.text_area.insert(tk.END, str(asiento) + "\n")

    def mostrar_mayor(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "--- Libro Mayor (Cuentas en T) ---\n\n")
        for cuenta, movimientos in self.mayor.cuentas_t.items():
            debe = sum(movimientos['Debe'])
            haber = sum(movimientos['Haber'])
            self.text_area.insert(tk.END, f"Cuenta: {CUENTAS[cuenta]}\n")
            self.text_area.insert(tk.END, f"  Debe: {debe}\n")
            self.text_area.insert(tk.END, f"  Haber: {haber}\n\n")

    def mostrar_balanza(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "--- Balanza de Comprobación ---\n\n")
        balanza = BalanzaComprobacion(self.mayor)
        total_debe = 0
        total_haber = 0
        for cuenta, movimientos in self.mayor.cuentas_t.items():
            debe = sum(movimientos['Debe'])
            haber = sum(movimientos['Haber'])
            total_debe += debe
            total_haber += haber
            self.text_area.insert(tk.END, f"Cuenta: {CUENTAS[cuenta]} | Debe: {debe} | Haber: {haber}\n")
        
        self.text_area.insert(tk.END, f"\nTotal Debe: {total_debe} | Total Haber: {total_haber}\n")
        if total_debe == total_haber:
            self.text_area.insert(tk.END, "Balanza de Comprobación: CORRECTA")
        else:
            self.text_area.insert(tk.END, "Balanza de Comprobación: DESCUADRE")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContabilidadGUI(root)
    root.mainloop()
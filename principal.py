from datetime import datetime

# Diccionario de cuentas contables
CUENTAS = {
    # ELEMENTO 1 ACTIVO CORRIENTE
    "10": "Efectivo y equivalentes de efectivo",
    "11": "Inversiones financieras",
    "12": "Cuentas por cobrar comerciales – Terceros",
    "13": "Cuentas por cobrar comerciales – Relacionadas",
    "14": "Cuentas por cobrar al personal, accionistas, directores y gerentes",
    "16": "Cuentas por cobrar diversas – Terceros",
    "17": "Cuentas por cobrar diversas – Relacionadas",
    "18": "Servicios y otros contratados por anticipado",

    # ELEMENTO 2 ACTIVO CORRIENTE (EXISTENCIAS)
    "20": "Mercaderías",
    "21": "Productos terminados",
    "22": "Subproductos, desechos y desperdicios",
    "23": "Productos en proceso",
    "24": "Materias primas",
    "25": "Materiales auxiliares, suministros y repuestos",
    "26": "Envases y embalajes",
    "27": "Activos no corrientes mantenidos para la venta",
    "28": "Existencias por recibir",
    "29": "Desvalorización de existencias",

    # ELEMENTO 3 ACTIVO NO CORRIENTE
    "30": "Inversiones mobiliarias",
    "31": "Inversiones inmobiliarias",
    "32": "Activos adquiridos en arrendamiento financiero",
    "33": "Inmuebles, maquinaria y equipo",
    "34": "Intangibles",
    "35": "Activos biológicos",
    "36": "Desvalorización de activo inmovilizado",
    "37": "Activo diferido",
    "38": "Otros activos",
    "39": "Depreciación, amortización y agotamiento acumulados",

    # ELEMENTO 4 PASIVOS
    "40": "Tributos y aportes al sistema de pensiones y de salud por pagar",
    "41": "Remuneraciones y participaciones por pagar",
    "42": "Cuentas por pagar comerciales – Terceros",
    "43": "Cuentas por pagar comerciales – Relacionadas",
    "44": "Cuentas por pagar a los accionistas, directores y gerentes",
    "45": "Obligaciones financieras",
    "46": "Cuentas por pagar diversas – Terceros",
    "47": "Cuentas por pagar diversas – Relacionadas",
    "48": "Provisiones",
    "49": "Pasivo diferido",

    # ELEMENTO 5 PATRIMONIO
    "50": "Capital",
    "51": "Acciones de inversión",
    "52": "Capital adicional",
    "56": "Resultados no realizados",
    "57": "Excedente de revaluación",
    "58": "Reservas",

    # CLASE 6 GASTOS
    "60": "Compras",
    "61": "Variación de existencias",
    "62": "Gastos de personal, directores y gerentes",
    "63": "Gastos de servicios prestados por terceros",
    "64": "Gastos por tributos",
    "65": "Otros gastos de gestión",
    "66": "Pérdida por medición de activos no financieros al valor razonable",
    "67": "Gastos financieros",
    "68": "Valuación y deterioro de activos y provisiones",
    "69": "Costo de ventas",

    # CLASE 8 CUENTAS DE CIERRE
    "81": "Producción del ejercicio",
    "82": "Valor agregado",
    "83": "Excedente bruto (insuficiencia bruta) de explotación",
    "84": "Resultado de explotación",
    "85": "Resultado antes de participaciones e impuestos",

    # CLASE 9 CUENTAS ANALÍTICAS DE EXPLOTACIÓN
    "91": "Costos por distribuir",
    "92": "Costos de producción",
    "93": "Centros de costos",
    "94": "Gastos administrativos",
    "95": "Gastos de ventas",
    "96": "Gastos financieros",

    # CLASE 7 INGRESOS
    "70": "Ventas",
    "71": "Variación de la producción almacenada",
    "72": "Producción de activo inmovilizado",
    "73": "Descuentos, rebajas y bonificaciones obtenidos",
    "74": "Descuentos, rebajas y bonificaciones concedidos",
    "75": "Otros ingresos de gestión",
    "76": "Ganancia por medición de activos no financieros al valor razonable",
    "77": "Ingresos financieros",
    "78": "Cargas cubiertas por provisiones",
    "79": "Cargas imputables a cuentas de costos y gastos",

    # CLASES ADICIONALES
    "87": "Participaciones de los trabajadores",
    "88": "Impuesto a la renta",
    "89": "Determinación del resultado del ejercicio"
}

class AsientoContable:
    def __init__(self, fecha, glosa, cuentas_debe, cuentas_haber, montos_debe, montos_haber):
        self.fecha = fecha
        self.glosa = glosa
        self.cuentas_debe = cuentas_debe
        self.cuentas_haber = cuentas_haber
        self.montos_debe = montos_debe
        self.montos_haber = montos_haber

    def __str__(self):
        detalles = f"Fecha: {self.fecha}\nGlosa: {self.glosa}\n"
        detalles += "Debe:\n"
        for cuenta, monto in zip(self.cuentas_debe, self.montos_debe):
            detalles += f"  {CUENTAS[cuenta]}: {monto}\n"
        
        detalles += "Haber:\n"
        for cuenta, monto in zip(self.cuentas_haber, self.montos_haber):
            detalles += f"  {CUENTAS[cuenta]}: {monto}\n"
        return detalles


class DiarioContable:
    def __init__(self):
        self.asientos = []

    def agregar_asiento(self, asiento):
        self.asientos.append(asiento)

    def mostrar_diario(self):
        for asiento in self.asientos:
            print(asiento)


# Clase Mayor (Cuentas T)
class MayorContable:
    def __init__(self):
        self.cuentas_t = {}

    def registrar_asiento_mayor(self, asiento):
        # Registrar en el Debe
        for cuenta, monto in zip(asiento.cuentas_debe, asiento.montos_debe):
            if cuenta not in self.cuentas_t:
                self.cuentas_t[cuenta] = {'Debe': [], 'Haber': []}
            self.cuentas_t[cuenta]['Debe'].append(monto)

        # Registrar en el Haber
        for cuenta, monto in zip(asiento.cuentas_haber, asiento.montos_haber):
            if cuenta not in self.cuentas_t:
                self.cuentas_t[cuenta] = {'Debe': [], 'Haber': []}
            self.cuentas_t[cuenta]['Haber'].append(monto)

    def mostrar_cuentas_t(self):
        print("\n--- Libro Mayor (Cuentas en T) ---")
        for cuenta, movimientos in self.cuentas_t.items():
            debe = sum(movimientos['Debe'])
            haber = sum(movimientos['Haber'])
            print(f"\nCuenta: {CUENTAS[cuenta]}")
            print(f"  Debe: {debe}")
            print(f"  Haber: {haber}")


# Clase para Balanza de Comprobación
class BalanzaComprobacion:
    def __init__(self, mayor):
        self.mayor = mayor

    def mostrar_balanza(self):
        print("\n--- Balanza de Comprobación ---")
        total_debe = 0
        total_haber = 0
        for cuenta, movimientos in self.mayor.cuentas_t.items():
            debe = sum(movimientos['Debe'])
            haber = sum(movimientos['Haber'])
            total_debe += debe
            total_haber += haber
            print(f"Cuenta: {CUENTAS[cuenta]} | Debe: {debe} | Haber: {haber}")
        
        print(f"\nTotal Debe: {total_debe} | Total Haber: {total_haber}")
        if total_debe == total_haber:
            print("Balanza de Comprobación: CORRECTA")
        else:
            print("Balanza de Comprobación: DESCUADRE")



# Función para agregar un asiento
def agregar_asiento():
    fecha = input("Ingrese la fecha (dd/mm/yyyy): ")
    glosa = input("Ingrese la glosa: ")

    cuentas_debe = []
    montos_debe = []
    cuentas_haber = []
    montos_haber = []

    print("Ingrese las cuentas y montos en el Debe (0 para terminar):")
    while True:
        cuenta_debe = input("Cuenta Debe: ")
        if cuenta_debe == "0":
            break
        if cuenta_debe not in CUENTAS:
            print("Cuenta no válida. Intente de nuevo.")
            continue
        monto_debe = float(input("Monto Debe: "))
        cuentas_debe.append(cuenta_debe)
        montos_debe.append(monto_debe)

    print("Ingrese las cuentas y montos en el Haber (0 para terminar):")
    while True:
        cuenta_haber = input("Cuenta Haber: ")
        if cuenta_haber == "0":
            break
        if cuenta_haber not in CUENTAS:
            print("Cuenta no válida. Intente de nuevo.")
            continue
        monto_haber = float(input("Monto Haber: "))
        cuentas_haber.append(cuenta_haber)
        montos_haber.append(monto_haber)

    asiento = AsientoContable(fecha, glosa, cuentas_debe, cuentas_haber, montos_debe, montos_haber)
    return asiento


def iniciar_bot():
    diario = DiarioContable()
    mayor = MayorContable()

    while True:
        print("\n--- Sistema de Registro Contable ---")
        print("1. Agregar asiento contable")
        print("2. Mostrar diario contable")
        print("3. Mostrar cuentas en T (Libro Mayor)")
        print("4. Mostrar balanza de comprobación")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            asiento = agregar_asiento()
            diario.agregar_asiento(asiento)
            mayor.registrar_asiento_mayor(asiento)
            print("\nAsiento agregado correctamente!\n")
        elif opcion == "2":
            print("\n--- Diario Contable ---\n")
            diario.mostrar_diario()
        elif opcion == "3":
            print("\n--- Cuentas en T (Libro Mayor) ---\n")
            mayor.mostrar_cuentas_t()
        elif opcion == "4":
            print("\n--- Balanza de Comprobación ---\n")
            balanza = BalanzaComprobacion(mayor)
            balanza.mostrar_balanza()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")



# Iniciar el bot
if __name__ == "__main__":
    iniciar_bot()
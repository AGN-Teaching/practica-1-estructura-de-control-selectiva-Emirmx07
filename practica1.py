# Definir tabla de ISR como listas de tuplas
isr_tabla = [
    (0.01, 746.04, 0.00, 1.92),
    (746.05, 6332.05, 14.32, 6.40),
    (6332.06, 11128.01, 371.83, 10.88),
    (11128.02, 12935.83, 893.63, 16.00),
    (12935.84, 15487.72, 1182.88, 17.92),
    (15487.73, 31236.49, 1640.18, 21.36),
    (31236.50, 49233.00, 5004.12, 23.52),
    (49233.01, 93993.94, 9236.89, 30.00),
    (93993.95, 125325.20, 22252.83, 32.00),
    (125325.21, 375925.62, 39220.32, 34.00),
    (375925.63, float('inf'), 117912.32, 35.00)
]

def calcular_sueldo_bruto(salario_hora, horas_trabajadas):
    if horas_trabajadas <= 160:
        return salario_hora * horas_trabajadas
    elif horas_trabajadas <= 200:
        return (salario_hora * 160) + ((horas_trabajadas - 160) * salario_hora * 1.5)
    else:
        return (salario_hora * 160) + (40 * salario_hora * 1.5) + ((horas_trabajadas - 200) * salario_hora * 2)

def calcular_isr(sueldo_bruto):
    for limite_inferior, limite_superior, cuota_fija, porcentaje in isr_tabla:
        if limite_inferior <= sueldo_bruto <= limite_superior:
            excedente = sueldo_bruto - limite_inferior
            return cuota_fija + (excedente * (porcentaje / 100))
    return 0  # En caso de error

def calcular_descuentos(sueldo_bruto, caja_ahorro, ahorro_solidario):
    seguridad_social = sueldo_bruto * 0.025
    ahorro_empresa = 0
    if caja_ahorro == 'fija':
        ahorro_empresa = 1000
    elif caja_ahorro == '3%':
        ahorro_empresa = sueldo_bruto * 0.03
    elif caja_ahorro == '5%':
        ahorro_empresa = sueldo_bruto * 0.05
    
    ahorro_solidario_valor = sueldo_bruto * ahorro_solidario
    return seguridad_social, ahorro_empresa, ahorro_solidario_valor

# Entrada de datos
salario_hora = float(input("Ingrese el salario por hora: "))
horas_trabajadas = int(input("Ingrese las horas trabajadas en el mes: "))
caja_ahorro = input("Ingrese el tipo de caja de ahorro (fija/3%/5%/ninguna): ")
if caja_ahorro not in ['fija', '3%', '5%', 'ninguna']:
    caja_ahorro = 'ninguna'

tipo_ahorro = int(input("Ingrese el porcentaje de ahorro solidario (0, 1, 2): "))
if tipo_ahorro not in [0, 1, 2]:
    tipo_ahorro = 0

# Cálculos
sueldo_bruto = calcular_sueldo_bruto(salario_hora, horas_trabajadas)
isr = calcular_isr(sueldo_bruto)
seguridad_social, ahorro_empresa, ahorro_solidario = calcular_descuentos(sueldo_bruto, caja_ahorro, tipo_ahorro / 100)
sueldo_neto = sueldo_bruto - (isr + seguridad_social + ahorro_empresa + ahorro_solidario)

# Salida de resultados
print("\n--- Resumen de Nómina ---")
print(f"Sueldo Bruto: ${sueldo_bruto:.2f}")
print(f"ISR: ${isr:.2f}")
print(f"Seguridad Social: ${seguridad_social:.2f}")
print(f"Ahorro en Caja: ${ahorro_empresa:.2f}")
print(f"Ahorro Solidario: ${ahorro_solidario:.2f}")
print(f"Sueldo Neto: ${sueldo_neto:.2f}")

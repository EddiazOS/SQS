import datetime
from fpdf import FPDF

# ==========================================
# CONFIGURACIÓN PERMANENTE SQS (EMISOR)
# ==========================================
NIT_SQS = "900.123.456-7" # <-- CAMBIA ESTO UNA SOLA VEZ POR TU NIT REAL
COLOR_INDIGO = (29, 17, 96)    # #1D1160 (Fondo)
COLOR_CORAL = (255, 107, 107)  # #FF6B6B (Resaltado/Total)
COLOR_GLACIAR = (142, 202, 230) # #8ECAE6 (Acento)
TASA_IVA = 0.19 # <-- 19% de IVA 

class FacturaSQS(FPDF):
    def header(self):
        # Bloque de Encabezado Indigo
        self.set_fill_color(*COLOR_INDIGO)
        self.rect(0, 0, 210, 45, 'F')
        
        try:
            self.image('logo.jpeg', 10, 8, 33) 
        except:
            self.set_font('Arial', 'B', 16)
            self.set_text_color(*COLOR_GLACIAR)
            self.text(10, 25, "SQS - Syntropy Quantum Solutions")

        self.set_font('Arial', 'B', 18)
        self.set_text_color(255, 255, 255)
        self.cell(0, 25, 'PROPUESTA ECONÓMICA TÉCNICA ', 0, 1, 'R')
        self.ln(10)

    def footer(self):
        self.set_y(-25)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(*COLOR_INDIGO)
        self.cell(0, 5, 'Esta cotización tiene una vigencia de quince (15) días calendario a partir de su emisión.', 0, 1, 'C')
        self.set_font('Arial', 'B', 8)
        self.cell(0, 5, f'Syntropy Quantum Solutions S.A.S. - NIT: {NIT_SQS} - Cartagena, Colombia', 0, 0, 'C')

def agregar_encabezado_datos(pdf, cliente_nombre, cliente_nit, proyecto):
    """Función auxiliar para imprimir los datos del cliente y proyecto en ambos PDFs"""
    pdf.ln(12)
    pdf.set_font('Arial', 'B', 11)
    pdf.set_text_color(*COLOR_INDIGO)
    
    pdf.cell(40, 7, "EMISOR:", 0, 0)
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 7, f"Syntropy Quantum Solutions S.A.S. (NIT: {NIT_SQS})", 0, 1)
    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(40, 7, "CLIENTE:", 0, 0)
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 7, f"{cliente_nombre.upper()} (NIT: {cliente_nit})", 0, 1)
    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(40, 7, "PROYECTO:", 0, 0)
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 7, proyecto, 0, 1)
    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(40, 7, "FECHA:", 0, 0)
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 7, str(datetime.date.today()), 0, 1)
    pdf.ln(12)

def ejecutar_interfaz():
    print("-" * 60)
    print(" SQS: GENERADOR DE PROPUESTAS COMERCIALES V2.3 ".center(60, " "))
    print("-" * 60)
    
    # 1. Datos del Cliente
    cliente_nombre = input("Nombre de la Empresa/Cliente: ")
    cliente_nit = input("NIT del Cliente: ")
    proyecto = input("Nombre del Proyecto: ")
    
    # 2. Parámetros de la Cotización
    print("\n--- Costos de Operación ---")
    h_nube = float(input("Horas de procesamiento Cloud: "))
    t_nube = float(input("Tarifa Cloud por hora (COP): "))
    
    nivel_esp = input("Perfil del Especialista (ej. Magíster Semi-Senior): ")
    h_esp = float(input(f"Horas asignadas al {nivel_esp}: "))
    t_esp = float(input("Tarifa por hora del especialista (COP): "))
    
    margen_utilidad = float(input("\nMargen de utilidad deseado (%): "))

    # 3. Motor de Cálculo
    costo_nube = h_nube * t_nube
    costo_talento = h_esp * t_esp
    costo_operativo_fijo = 1200000 * 0.10 
    
    total_costos_directos = costo_nube + costo_talento + costo_operativo_fijo
    
    # Cálculos finales
    precio_final = total_costos_directos / (1 - (margen_utilidad / 100))
    utilidad_neta = precio_final - total_costos_directos
    valor_iva = precio_final * TASA_IVA
    total_con_iva = precio_final + valor_iva

    nombre_base_archivo = cliente_nombre.replace(' ', '_')

    # =====================================================================
    # 4. CONSTRUCCIÓN DEL PDF 1: PARA EL CLIENTE (CONSOLIDADO)
    # =====================================================================
    pdf_cliente = FacturaSQS()
    pdf_cliente.add_page()
    agregar_encabezado_datos(pdf_cliente, cliente_nombre, cliente_nit, proyecto)

    # Tabla Consolidada
    pdf_cliente.set_fill_color(*COLOR_INDIGO)
    pdf_cliente.set_text_color(255, 255, 255)
    pdf_cliente.set_font('Arial', 'B', 10)
    pdf_cliente.cell(140, 10, ' DESCRIPCIÓN DE LA ACTIVIDAD', 1, 0, 'L', True)
    pdf_cliente.cell(50, 10, ' VALOR (COP)', 1, 1, 'C', True)

    pdf_cliente.set_text_color(0, 0, 0)
    pdf_cliente.set_font('Arial', '', 10)
    pdf_cliente.cell(140, 10, f' Ejecución integral de servicios para: {proyecto}', 1, 0, 'L')
    pdf_cliente.cell(50, 10, f'$ {precio_final:,.0f}', 1, 1, 'R')

    # Totales Cliente
    pdf_cliente.ln(6)
    pdf_cliente.set_font('Arial', 'B', 11)
    pdf_cliente.set_text_color(*COLOR_INDIGO)
    pdf_cliente.cell(140, 8, 'SUBTOTAL (SIN IVA):', 0, 0, 'R')
    pdf_cliente.set_font('Arial', '', 11)
    pdf_cliente.cell(50, 8, f'$ {precio_final:,.0f}', 0, 1, 'R')

    pdf_cliente.set_font('Arial', 'B', 11)
    pdf_cliente.cell(140, 8, f'IVA ({int(TASA_IVA*100)}%):', 0, 0, 'R')
    pdf_cliente.set_font('Arial', '', 11)
    pdf_cliente.cell(50, 8, f'$ {valor_iva:,.0f}', 0, 1, 'R')

    pdf_cliente.set_font('Arial', 'B', 14)
    pdf_cliente.set_text_color(*COLOR_CORAL)
    pdf_cliente.cell(140, 12, 'TOTAL INVERSIÓN:', 0, 0, 'R')
    pdf_cliente.set_text_color(*COLOR_INDIGO)
    pdf_cliente.cell(50, 12, f'$ {total_con_iva:,.0f}', 0, 1, 'R')

    archivo_cliente = f"Propuesta_SQS_{nombre_base_archivo}_CLIENTE.pdf"
    pdf_cliente.output(archivo_cliente)


    # =====================================================================
    # 5. CONSTRUCCIÓN DEL PDF 2: INTERNO (DESGLOSE DE COSTOS)
    # =====================================================================
    pdf_interno = FacturaSQS()
    pdf_interno.add_page()
    agregar_encabezado_datos(pdf_interno, cliente_nombre, cliente_nit, proyecto)

    # Etiqueta de Uso Interno
    pdf_interno.set_font('Arial', 'B', 12)
    pdf_interno.set_text_color(*COLOR_CORAL)
    pdf_interno.cell(0, 10, '*** DOCUMENTO DE USO INTERNO - DESGLOSE DE COSTOS ***', 0, 1, 'C')
    pdf_interno.ln(5)

    # Tabla Detallada
    pdf_interno.set_fill_color(*COLOR_INDIGO)
    pdf_interno.set_text_color(255, 255, 255)
    pdf_interno.set_font('Arial', 'B', 9)
    pdf_interno.cell(80, 8, ' CONCEPTO', 1, 0, 'L', True)
    pdf_interno.cell(60, 8, ' PARÁMETROS', 1, 0, 'C', True)
    pdf_interno.cell(50, 8, ' SUBTOTAL (COP)', 1, 1, 'C', True)

    pdf_interno.set_text_color(0, 0, 0)
    pdf_interno.set_font('Arial', '', 9)

    # Costos Nube
    pdf_interno.cell(80, 8, ' Infraestructura Cloud', 1, 0, 'L')
    pdf_interno.cell(60, 8, f'{h_nube} h x $ {t_nube:,.0f}', 1, 0, 'C')
    pdf_interno.cell(50, 8, f'$ {costo_nube:,.0f}', 1, 1, 'R')

    # Costos Talento
    pdf_interno.cell(80, 8, f' Honorarios ({nivel_esp})', 1, 0, 'L')
    pdf_interno.cell(60, 8, f'{h_esp} h x $ {t_esp:,.0f}', 1, 0, 'C')
    pdf_interno.cell(50, 8, f'$ {costo_talento:,.0f}', 1, 1, 'R')

    # Operativos
    pdf_interno.cell(80, 8, ' Gasto Administrativo Base', 1, 0, 'L')
    pdf_interno.cell(60, 8, '10% Referencia Operativa', 1, 0, 'C')
    pdf_interno.cell(50, 8, f'$ {costo_operativo_fijo:,.0f}', 1, 1, 'R')

    # Subtotal Costos Directos
    pdf_interno.set_font('Arial', 'B', 9)
    pdf_interno.set_fill_color(240, 240, 240)
    pdf_interno.cell(140, 8, ' TOTAL COSTOS DIRECTOS OPE.:', 1, 0, 'R', True)
    pdf_interno.cell(50, 8, f'$ {total_costos_directos:,.0f}', 1, 1, 'R', True)

    # Margen de Utilidad
    pdf_interno.set_font('Arial', '', 9)
    pdf_interno.cell(80, 8, ' Margen de Utilidad Proyectado', 1, 0, 'L')
    pdf_interno.cell(60, 8, f'{margen_utilidad} % sobre Venta', 1, 0, 'C')
    pdf_interno.set_text_color(0, 150, 0) # Verde para la utilidad
    pdf_interno.cell(50, 8, f'$ {utilidad_neta:,.0f}', 1, 1, 'R')
    pdf_interno.set_text_color(0, 0, 0)

    # Resumen Financiero Interno
    pdf_interno.ln(6)
    pdf_interno.set_font('Arial', 'B', 10)
    pdf_interno.cell(140, 8, 'PRECIO DE VENTA SUGERIDO (SIN IVA):', 0, 0, 'R')
    pdf_interno.cell(50, 8, f'$ {precio_final:,.0f}', 0, 1, 'R')

    pdf_interno.set_font('Arial', '', 10)
    pdf_interno.cell(140, 8, f'IVA ({int(TASA_IVA*100)}%):', 0, 0, 'R')
    pdf_interno.cell(50, 8, f'$ {valor_iva:,.0f}', 0, 1, 'R')

    pdf_interno.set_font('Arial', 'B', 12)
    pdf_interno.set_text_color(*COLOR_INDIGO)
    pdf_interno.cell(140, 10, 'TOTAL A FACTURAR:', 0, 0, 'R')
    pdf_interno.cell(50, 10, f'$ {total_con_iva:,.0f}', 0, 1, 'R')

    archivo_interno = f"Propuesta_SQS_{nombre_base_archivo}_INTERNO.pdf"
    pdf_interno.output(archivo_interno)

    print(f"\n[SISTEMA] Se han generado dos documentos:")
    print(f"  -> Para enviar: {archivo_cliente}")
    print(f"  -> Para archivo: {archivo_interno}")

if __name__ == "__main__":
    ejecutar_interfaz()
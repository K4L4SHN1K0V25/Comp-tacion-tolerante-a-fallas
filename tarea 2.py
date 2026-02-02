# Primero, necesitas instalar la herramienta: pip install loguru
from loguru import logger

# Configuracion de la herramienta:
# Esto crea un archivo llamado "errores_app.log" que guardara todos los errores.
# 'rotation="500 MB"' significa que si el archivo crece mucho, crea uno nuevo.
logger.add("errores_app.log", rotation="500 MB", level="ERROR")

def calcular_descuento(precio, porcentaje):
    try:
        # Simulamos una validacion
        if porcentaje > 100:
            raise ValueError("El descuento no puede ser mayor al 100%")
        
        resultado = precio * (porcentaje / 100)
        
        # Simulamos un error matematico (division por cero) para probar la herramienta
        # Esto ocurrira si el usuario pasa un precio y luego forzamos un error
        if precio == 0:
            x = 10 / 0 
            
        logger.info(f"Calculo exitoso. Descuento: {resultado}")
        return resultado

    except ZeroDivisionError as e:
        # Aqui usamos la herramienta para manejar el error
        # .exception() guarda automaticamente el "stack trace" completo (donde ocurrio)
        logger.exception("¡Error Critico! Se intento dividir por cero.")
        print(">> Ocurrio un problema interno, el equipo tecnico ha sido notificado.")

    except ValueError as e:
        # Manejamos un error de logica de negocio
        logger.error(f"Error de validacion: {e}")
        print(f">> Error: {e}")

# --- Simulacion del Programa ---

print("--- Intento 1: Datos validos ---")
calcular_descuento(1000, 20)

print("\n--- Intento 2: Error de Logica (Valor invalido) ---")
calcular_descuento(1000, 150)

print("\n--- Intento 3: Error Critico (Crash) ---")
calcular_descuento(0, 20)

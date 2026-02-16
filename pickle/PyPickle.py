import pickle
import time
import os

# Nombre del archivo donde guardaremos el "checkpoint"
NOMBRE_ARCHIVO = "estado_ejecucion.pkl"

def guardar_estado(contador):
    """Guarda el valor actual del contador en un archivo."""
    print(f"\n[!] Guardando checkpoint en el paso {contador}...")
    with open(NOMBRE_ARCHIVO, 'wb') as archivo:
        # pickle.dump(objeto, archivo) serializa el objeto y lo guarda
        pickle.dump(contador, archivo)
    print("[✓] Estado guardado correctamente.")

def cargar_estado():
    """Intenta cargar el estado previo si el archivo existe."""
    if os.path.exists(NOMBRE_ARCHIVO):
        print("[!] Encontrado archivo de checkpoint. Restaurando estado...")
        with open(NOMBRE_ARCHIVO, 'rb') as archivo:
            # pickle.load(archivo) lee el archivo y reconstruye el objeto
            contador = pickle.load(archivo)
        return contador
    else:
        print("[*] No hay checkpoint previo. Iniciando desde cero.")
        return 0

def proceso_largo():
    # 1. Intentamos restaurar el estado (si existe)
    contador = cargar_estado()
    
    print(f"--- Iniciando/Retomando ejecucion en el paso: {contador} ---")
    print("(Presiona Ctrl + C para detener y guardar el progreso)")

    try:
        # Simulamos un trabajo infinito o muy largo
        while True:
            contador += 1
            print(f"Procesando tarea numero: {contador}")
            time.sleep(2) # Espera 1 segundo para simular trabajo

    except KeyboardInterrupt:
        # Esto captura cuando presionas Ctrl + C en la terminal
        print("\n\n[!] Interrupcion detectada.")
        guardar_estado(contador)
        print("Programa terminado. Puedes ejecutarlo de nuevo para continuar.")

if __name__ == "__main__":
    proceso_largo()
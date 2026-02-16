# PyPickle 🥒 — Checkpointing y Persistencia en Python

Este proyecto es una demostración práctica de la técnica de **Checkpointing** (puntos de control). Implementa un script capaz de guardar su estado de ejecución actual en el disco y restaurarlo automáticamente tras una interrupción, garantizando la tolerancia a fallos.

## 📋 Descripción del Archivo Principal

`PyPickle.py` es el script que simula un proceso largo y guarda un "checkpoint" (un contador numérico) en disco para poder retomar la ejecución tras una interrupción.

### Funciones Principales:

* **`NOMBRE_ARCHIVO`**: Constante que define el nombre del archivo donde se guarda el estado (`estado_ejecucion.pkl`).
* **`guardar_estado(contador)`**: Se encarga de serializar y escribir el valor actual del contador en el disco utilizando `pickle.dump`.
* **`cargar_estado()`**: Verifica si existe el archivo de checkpoint. Si existe, carga y devuelve el contador mediante `pickle.load`; si no, devuelve `0` para iniciar desde el principio.
* **`proceso_largo()`**: Es el núcleo del programa. Restaura el estado inicial y ejecuta un bucle infinito que incrementa el contador, simulando trabajo con `time.sleep()`.

## 🛠️ Requisitos

* Python 3.x
* Librería estándar (módulos `pickle`, `os`, `time`).

## 🚀 Uso

1.  Abre una consola o terminal en la carpeta del proyecto.
2.  Ejecuta el script:
    ```bash
    python PyPickle.py
    ```
3.  El programa comenzará a contar.
4.  Presiona `Ctrl + C` para detener la ejecución. El programa capturará la interrupción y guardará el progreso en `estado_ejecucion.pkl`.
5.  Ejecuta de nuevo el comando del paso 2. Notarás que el programa reanuda el conteo desde el último número guardado.

### Ejemplo de Salida

**Primera ejecución:**
```text
[*] No hay checkpoint previo. Iniciando desde cero.
--- Iniciando/Retomando ejecución en el paso: 0 ---
Procesando tarea número: 1
Procesando tarea número: 2
^C
[!] Interrupción detectada. Guardando...
<img width="697" height="413" alt="Captura de pantalla 2026-02-16 085152" src="https://github.com/user-attachments/assets/7d9db2fc-cfd1-4264-b7c4-7ca113df54e6" />

**Segunda ejecución (Restauración):**
```text
[!] Encontrado archivo de checkpoint. Restaurando estado...
--- Iniciando/Retomando ejecución en el paso: 2 ---
Procesando tarea número: 3
...
<img width="707" height="394" alt="Captura de pantalla 2026-02-16 085448" src="https://github.com/user-attachments/assets/c47bc771-e47d-473a-9b4a-20ca602cbd05" />

## ⚠️ Advertencia de Seguridad

> **Importante:** El módulo `pickle` no es seguro contra datos erróneos o maliciosos. Nunca cargues (*unpickle*) datos recibidos de una fuente no confiable o no autenticada, ya que podrían ejecutar código arbitrario durante la carga.

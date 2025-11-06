# Instrucciones para ejecutar el proyecto Dash

## Problemas comunes resueltos:

### ❌ Errores que tenías:
1. **Typo**: `pyhton` → debe ser `python`
2. **Venv incorrecto**: `python -m venv.venv` → debe ser `python -m venv venv`
3. **Código incompleto**: Faltaba `app.run_server(debug=True)`

## ✅ Pasos correctos para ejecutar:

### 1. Crear el entorno virtual (solo la primera vez)
```bash
# CORRECTO:
python -m venv venv

# NO uses:
# python -m venv.venv  ❌
```

### 2. Activar el entorno virtual

**En Windows Git Bash:**
```bash
source venv/Scripts/activate
```

**En Windows CMD:**
```cmd
venv\Scripts\activate.bat
```

**En Windows PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
# CORRECTO (fíjate en la ortografía):
python Dash.py

# NO uses:
# pyhton Dash.py  ❌
```

### 5. Abrir en el navegador
Una vez ejecutado, abre tu navegador en:
```
http://127.0.0.1:8050
```

## Verificación rápida:

```bash
# 1. Navega al directorio
cd ~/OneDrive\ -\ NTT\ DATA\ EMEAL/Desktop/BOOTCAMP/Repositorio/datascience-g5/dash

# 2. Crea el venv (solo primera vez)
python -m venv venv

# 3. Activa el venv
source venv/Scripts/activate

# 4. Instala dependencias (solo primera vez)
pip install -r requirements.txt

# 5. Ejecuta la app
python Dash.py
```

## Notas importantes:
- Siempre verifica la ortografía: es **python**, no "pyhton"
- El comando para crear venv es: `python -m venv venv` (el primer "venv" es el módulo, el segundo es el nombre de la carpeta)
- Debes activar el entorno virtual antes de instalar paquetes o ejecutar la app
- Si ves `(venv)` al inicio de tu prompt, significa que el entorno está activado correctamente

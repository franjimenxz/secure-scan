
# SecureScan

## Introducción

Bienvenido a **SecureScan**, tu herramienta minimalista para escanear vulnerabilidades en las dependencias de tus proyectos. Ya seas desarrollador o un profesional preocupado por la seguridad, SecureScan está aquí para ayudarte a encontrar y corregir vulnerabilidades en tus proyectos Python y JavaScript.

Con unos pocos comandos, SecureScan analiza tus archivos `requirements.txt` (para Python) y `package.json` (para Node.js), proporcionándote un informe detallado de las vulnerabilidades encontradas y las soluciones recomendadas.

## Características

- **Escaneo de Dependencias de Python**: Utiliza `pip-audit` para detectar vulnerabilidades en dependencias de Python listadas en `requirements.txt`.
- **Escaneo de Dependencias de JavaScript**: Usa `npm audit` para identificar riesgos de seguridad en dependencias de JavaScript declaradas en `package.json`.
- **Informes Detallados**: SecureScan genera informes fáciles de leer, proporcionando una visión clara de las vulnerabilidades y las soluciones disponibles.
- **Simplicidad y Extensibilidad**: La herramienta está diseñada para ser sencilla pero puede ser extendida fácilmente para cubrir otros lenguajes o ecosistemas.

## Requisitos

Para empezar, necesitarás lo siguiente:

1. **Python 3.x**
2. **Node.js** y **npm** (para el análisis de dependencias de Node.js)
3. Instalar `pip-audit` para el análisis de dependencias de Python.

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/franjimenxz/secure-scan.git
   cd secure-scan
   ```

2. **Instala las dependencias de Python**:
   ```bash
   pip install pip-audit
   ```

3. **Instala las dependencias de Node.js**:
   ```bash
   npm install
   ```

## Uso

Una vez que tengas todo instalado, usar SecureScan es tan sencillo como ejecutar un comando:

```bash
python main.py
```

SecureScan buscará archivos `requirements.txt` y `package.json` en tu directorio de proyecto y analizará sus contenidos para encontrar vulnerabilidades conocidas.

### Ejemplo de Salida

Aquí tienes un ejemplo de lo que verás después de ejecutar SecureScan:

```plaintext
Escaneando dependencias de Python en requirements.txt...
=== Vulnerabilidades Encontradas ===
- Dependencia: requests, Versión: 2.24.0
  Vulnerabilidad: PYSEC-2023-74, Fix: 2.31.0

- Dependencia: flask, Versión: 1.0.2
  Vulnerabilidad: GHSA-9wx4-h78v-vm56, Fix: 2.32.0

Escaneando dependencias de Node.js en package.json...
=== Vulnerabilidades Encontradas ===
- Dependencia: express, Versión: 4.16.0
  Vulnerabilidad: GHSA-9wx4-h78v-vm56, Fix: >=4.17.1
```

## Estructura del Proyecto

Aquí tienes una visión rápida de la estructura del proyecto:

```plaintext
SecureScan/
│
├── main.py                     # Punto de entrada para ejecutar el escaneo
├── secure_scan.py               # Lógica principal del escaneo
├── requirements.txt             # Ejemplo de dependencias de Python
├── package.json                 # Ejemplo de dependencias de Node.js
├── test/                        # Tests para SecureScan
│   └── test_secure_scan.py      # Tests unitarios
└── README.md                    # Este archivo
```

## Pruebas

Hemos incluido algunas pruebas para asegurarnos de que todo funcione como se espera. Puedes ejecutar las pruebas usando `pytest`:

```bash
pytest test/test_secure_scan.py
```

### Qué se cubre en las pruebas

- `test_parse_vulnerabilities()`: Verifica que el análisis de la salida de `pip-audit` funcione correctamente.
- `test_parse_npm_vulnerabilities()`: Comprueba que el análisis de la salida de `npm audit` funcione como se espera.
- `test_check_python_vulnerabilities()`: Simula el escaneo de dependencias de Python.
- `test_check_js_vulnerabilities()`: Simula el escaneo de dependencias de JavaScript.

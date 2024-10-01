import subprocess
import os
import logging
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función para ejecutar pip-audit y analizar las vulnerabilidades
def check_python_vulnerabilities(requirements_file):
    if not os.path.exists(requirements_file):
        logger.error(f"El archivo {requirements_file} no existe.")
        return []

    logger.info(f"Escaneando {requirements_file} con pip-audit...")

    try:
        result = subprocess.run(['pip-audit', '-r', requirements_file], capture_output=True, text=True)
        vulnerabilities = parse_vulnerabilities(result.stdout)
        return vulnerabilities
    except Exception as e:
        logger.error(f"Ocurrió un error al ejecutar pip-audit: {e}")
        return []

# Función para ejecutar npm audit y analizar vulnerabilidades de package.json
def check_js_vulnerabilities(package_file):
    if not os.path.exists(package_file):
        logger.error(f"El archivo {package_file} no existe.")
        return []

    logger.info(f"Escaneando {package_file} con npm audit...")

    try:
        result = subprocess.run(['npm', 'audit', '--json'], capture_output=True, text=True)
        vulnerabilities = parse_npm_vulnerabilities(result.stdout)
        return vulnerabilities
    except Exception as e:
        logger.error(f"Ocurrió un error al ejecutar npm audit: {e}")
        return []

# Función para analizar la salida de pip-audit
def parse_vulnerabilities(output):
    vulnerabilities = []
    lines = output.strip().split('\n')[2:]  # Saltar las líneas de encabezado
    for line in lines:
        parts = line.split()
        if len(parts) >= 4:
            vulnerabilities.append({
                'package': parts[0],
                'version': parts[1],
                'vulnerability_id': parts[2],
                'fix_version': parts[3]
            })
    return vulnerabilities

# Función para analizar la salida de npm audit
def parse_npm_vulnerabilities(output):
    vulnerabilities = []
    try:
        audit_data = json.loads(output)
        for package, details in audit_data['advisories'].items():
            vulnerabilities.append({
                'package': details['module_name'],
                'version': details['findings'][0]['version'],
                'vulnerability_id': details['id'],
                'fix_version': details.get('patched_versions', 'No fix available')
            })
    except Exception as e:
        logger.error(f"Error al analizar la salida de npm audit: {e}")
    return vulnerabilities

# Generar un informe detallado
def generate_report(vulnerabilities):
    if vulnerabilities:
        report = "=== Vulnerabilidades Encontradas ===\n"
        for vuln in vulnerabilities:
            report += f"- Dependencia: {vuln['package']}, Versión: {vuln['version']}\n"
            report += f"  Vulnerabilidad: {vuln['vulnerability_id']}, Fix: {vuln['fix_version']}\n"
        return report
    return "No se encontraron vulnerabilidades."

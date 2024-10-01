import os
from SecureScan.secure_scan import check_python_vulnerabilities, check_js_vulnerabilities, generate_report

def main():
    vulnerabilities = []

    # Escaneo de Python (requirements.txt)
    if os.path.exists('requirements.txt'):
        print("Escaneando dependencias de Python en requirements.txt...")
        vulnerabilities += check_python_vulnerabilities('requirements.txt')

    # Escaneo de Node.js (package.json)
    if os.path.exists('package.json'):
        print("Escaneando dependencias de Node.js en package.json...")
        vulnerabilities += check_js_vulnerabilities('package.json')

    # Generar y mostrar informe
    report = generate_report(vulnerabilities)
    print(report)

if __name__ == "__main__":
    main()

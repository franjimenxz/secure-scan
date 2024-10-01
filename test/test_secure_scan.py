import pytest
import subprocess
import json
from SecureScan.secure_scan import check_python_vulnerabilities, check_js_vulnerabilities, parse_vulnerabilities, parse_npm_vulnerabilities

# Datos de prueba
MOCK_PIP_AUDIT_OUTPUT = """
Name    Version ID                  Fix Versions
-------- ------- ------------------- ------------
requests 2.24.0 PYSEC-2023-74       2.31.0
flask    1.0.2  GHSA-9wx4-h78v-vm56 2.32.0
"""

MOCK_NPM_AUDIT_OUTPUT = json.dumps({
    "advisories": {
        "1": {
            "module_name": "express",
            "findings": [{"version": "4.16.0"}],
            "id": "GHSA-9wx4-h78v-vm56",
            "patched_versions": ">=4.17.1"
        }
    }
})

def test_parse_vulnerabilities():
    vulnerabilities = parse_vulnerabilities(MOCK_PIP_AUDIT_OUTPUT)
    assert len(vulnerabilities) == 2
    assert vulnerabilities[0] == {
        'package': 'requests',
        'version': '2.24.0',
        'vulnerability_id': 'PYSEC-2023-74',
        'fix_version': '2.31.0'
    }

def test_parse_npm_vulnerabilities():
    vulnerabilities = parse_npm_vulnerabilities(MOCK_NPM_AUDIT_OUTPUT)
    assert len(vulnerabilities) == 1
    assert vulnerabilities[0] == {
        'package': 'express',
        'version': '4.16.0',
        'vulnerability_id': 'GHSA-9wx4-h78v-vm56',
        'fix_version': ">=4.17.1"
    }

def test_check_python_vulnerabilities(mocker):
    mocker.patch('subprocess.run', return_value=mocker.Mock(stdout=MOCK_PIP_AUDIT_OUTPUT))
    vulnerabilities = check_python_vulnerabilities('test/test_requirements.txt')
    assert len(vulnerabilities) == 2
    assert vulnerabilities[0]['package'] == 'requests'

def test_check_js_vulnerabilities(mocker):
    mocker.patch('subprocess.run', return_value=mocker.Mock(stdout=MOCK_NPM_AUDIT_OUTPUT))
    vulnerabilities = check_js_vulnerabilities('test/package.json')
    assert len(vulnerabilities) == 1
    assert vulnerabilities[0]['package'] == 'express'

if __name__ == "__main__":
    pytest.main()

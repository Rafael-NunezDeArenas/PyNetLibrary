# Test: does a button-executed script pass through the static validator?
# Tries imports/assemblies that the MCP bridge rejects, reports each result.
# Harmless: only reads versions and paths, modifies nothing.

import clr
import sys

results = []
results.append("Python embebido: " + sys.version.split(" ")[0])

try:
    import os
    results.append("import os: OK (cwd: " + os.getcwd() + ")")
except Exception as e:
    results.append("import os: BLOQUEADO -> " + str(e)[:100])

try:
    clr.AddReference("ManagedMapApi")
    from Autodesk.Gis.Map import HostMapApplicationServices
    results.append("ManagedMapApi (Map 3D): OK, API disponible")
except Exception as e:
    results.append("ManagedMapApi: BLOQUEADO -> " + str(e)[:100])

try:
    import urllib.request
    results.append("import urllib: OK (red disponible)")
except Exception as e:
    results.append("import urllib: BLOQUEADO -> " + str(e)[:100])

msg = "\n".join(results)
print(msg)

clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import MessageBox
MessageBox.Show(msg, "PyNET - Test sandbox de botones")

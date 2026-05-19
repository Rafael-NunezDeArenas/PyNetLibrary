import clr
import os
import System
from collections import defaultdict
from System.Reflection import BindingFlags #type:ignore


ASSEMBLY_NAME = "Autodesk.Navisworks.Clash"

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
os.makedirs(desktop_path, exist_ok=True)

OUTPUT_FILE = os.path.join(desktop_path, "navisworks_api_stubs.py")

clr.AddReference(ASSEMBLY_NAME)

assemblies = System.AppDomain.CurrentDomain.GetAssemblies()

target_assembly = None
for asm in assemblies:
    if asm.GetName().Name == ASSEMBLY_NAME:
        target_assembly = asm
        break

if not target_assembly:
    raise Exception(f"Assembly {ASSEMBLY_NAME} not found")



TYPE_MAP = {
    "String": "str",
    "Boolean": "bool",
    "Int32": "int",
    "Int64": "int",
    "Double": "float",
    "Single": "float",
    "Void": "None",
    "Object": "object",
}


def map_type(t):
    try:
        name = t.Name
        return TYPE_MAP.get(name, name)
    except:
        return "object"


def generate_methods(methods, current_type):
    grouped = defaultdict(list)

    for m in methods:
        if m.IsSpecialName:
            continue
        if m.DeclaringType != current_type:
            continue

        grouped[m.Name].append(m)

    lines = []

    for name, overloads in grouped.items():
        try:
            overloads = sorted(
                overloads,
                key=lambda m: len(m.GetParameters()),
                reverse=True
            )

            best = overloads[0]

            is_static = best.IsStatic
            decorator = "@staticmethod\n    " if is_static else ""

            signature = "self, *args" if not is_static else "*args"

            params_doc = []
            for p in best.GetParameters():
                p_name = p.Name
                p_type = map_type(p.ParameterType)
                params_doc.append(f"{p_name}: {p_type}")

            ret = map_type(best.ReturnType)

            doc = "Signature:\n        "
            doc += f"{name}({', '.join(params_doc)}) -> {ret}"

            lines.append(f"""
    {decorator}def {name}({signature}):
        \"\"\"
        {doc}
        \"\"\"
        pass
            """)
        except:
            continue

    return "\n".join(lines)


def generate_property(p):
    try:
        name = p.Name
        typ = map_type(p.PropertyType)

        return f"""
    {name}: {typ} = property(lambda self: None, lambda self, v: None)
    """
    except:
        return ""


def generate_class(t):
    try:
        if not t.IsPublic:
            return ""

        name = t.Name

        bases = []
        if t.BaseType:
            bases.append(map_type(t.BaseType))

        bases_str = ", ".join(bases) if bases else "object"

        lines = []
        lines.append(f"class {name}({bases_str}):")
        lines.append(f'    """ .NET type: {t.FullName} """')

        lines.append("""
    def __init__(self, *args) -> None:
        pass
        """)

        methods = t.GetMethods(
            BindingFlags.Public |
            BindingFlags.Instance |
            BindingFlags.Static |
            BindingFlags.DeclaredOnly
        )

        lines.append(generate_methods(methods, t))

        # Properties
        for p in t.GetProperties():
            try:
                prop_code = generate_property(p)
                if prop_code:
                    lines.append(prop_code)
            except:
                continue

        return "\n".join(lines)

    except:
        return ""


types = target_assembly.GetTypes()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("# Auto-generated Navisworks API stubs (clean reflection)\n\n")

    for t in types:
        try:
            class_code = generate_class(t)
            if class_code:
                f.write(class_code)
                f.write("\n\n")
        except:
            continue

print(f"Stub created: {OUTPUT_FILE}")
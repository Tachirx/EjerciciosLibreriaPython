import os, glob;
try:
    from pypdf import PdfReader
    has_pypdf = True
except ImportError:
    has_pypdf = False

def analizar_python(fout):
    fout.write("### Análisis de Ejercicios Python ###\n\n")
    archivos_py = glob.glob("**/*.py", recursive=True)
    archivos_py = [f for f in archivos_py if "venv" not in f and "analyzer.py" not in f]
    for archivo in archivos_py:
        with open(archivo, "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.readlines()
        lineas_clave = [l.strip() for l in contenido if l.strip() and not l.strip().startswith("#")][:3]
        fout.write(f"Archivo: {archivo}\n")
        fout.write(f"Muestra inicial: {\" | \".join(lineas_clave)}\n\n")

def analizar_pdfs(fout):
    fout.write("### Análisis de Guías PDF ###\n\n")
    if not has_pypdf: return
    archivos_pdf = glob.glob("*.pdf")
    for archivo in archivos_pdf:
        try:
            reader = PdfReader(archivo)
            num_paginas = len(reader.pages)
            fout.write(f"Documento: {archivo} ({num_paginas} páginas)\n")
            if num_paginas > 0:
                texto_pag1 = reader.pages[0].extract_text()
                lineas = [l for l in texto_pag1.split("\n") if l.strip()][:5]
                fout.write(f"Extracto Pag 1: {\"  \".join(lineas)}\n")
            if reader.outline:
                fout.write("Índice detectado:\n")
                for item in reader.outline:
                    if not isinstance(item, list): fout.write(f" - {item.title}\n")
            fout.write("\n")
        except Exception as e:
            fout.write(f"Error leyendo {archivo}: {e}\n\n")

if __name__ == "__main__":
    with open("reporte_utf8.txt", "w", encoding="utf-8") as fout:
        analizar_python(fout)
        analizar_pdfs(fout)


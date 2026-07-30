from pathlib import Path
from datetime import datetime
import shutil

pasta_organizada = Path("Organizador De Arquivos")
arquivo_log = Path("registro.log")

for arquivo in Path("organizador").iterdir():
    extensao = arquivo.suffix[1:]
    subpasta = pasta_organizada/extensao
    if not subpasta.exists():
        subpasta.mkdir(exist_ok=True, parents=True)
    
    shutil.copy2(arquivo, subpasta/arquivo.name)      
    with open(arquivo_log, "a", encoding="utf-8") as log:
        agora = datetime.now()
        log.write(agora.strftime(f"O Arquivo {arquivo} foi movido para a pasta {subpasta} as %H:%M:%S do dia %d/%m/%Y\n"))
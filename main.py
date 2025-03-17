import os
import rarfile
from dotenv import load_dotenv
import pandas as pd
from parse_match import *

load_dotenv()
demos_path = os.environ.get('demos_path')

df = pd.DataFrame()

subfolders = [f.path for f in os.scandir(demos_path) if f.is_dir()]
for subfolder in subfolders:
    arqs = [f.path for f in os.scandir(subfolder)]
    for arq in arqs:
        fileRar = rarfile.RarFile(arq)
        for file in fileRar.infolist():
            pathDemo = os.path.join(subfolder, file.filename)
            fileRar.extract(file.filename, subfolder)
            df_match = calculeMatch(pathDemo, file.filename)
            df = pd.concat([df, df_match], ignore_index=True)
            os.remove(pathDemo)
            print("mapa processado: ", file.filename) 
        print("jogo processado: ", arq)
    print("time processado: ", subfolder)

df.to_csv("rouds_brasil.csv")
print("Processamento encerrado")
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine( )

conn = engine.connect()


def UploadExcel(archivonombre,tabla):
    excel_f=pd.ExcelFile(archivonombre)
    excel_df=excel_f.parse(sheet_name="Sheet1")
    excel_df=excel_df.set_index('ID')
    excel_df.to_sql(tabla,conn,if_exists="replace",index=True, index_label='ID',)
    query="ALTER TABLE `{table}` ADD PRIMARY KEY (`ID`);".format(table=tabla)
    conn.execute(query)

def GetExcel(urldoc,ubicación):
    gsread=pd.read_csv(urldoc,index_col=0)
    gsread.to_excel(ubicación)
    

GetExcel('',"utils/CERTIFICADOS.xlsx")
GetExcel('',"utils/Productos.xlsx")
GetExcel('',"utils/Noticias.xlsx")
GetExcel('',"utils/Proveedores.xlsx")


UploadExcel('utils/CERTIFICADOS.xlsx',"Usuarios")
UploadExcel('utils/Noticias.xlsx',"Noticias")
UploadExcel('utils/Productos.xlsx',"Productos")
UploadExcel('utils/Proveedores.xlsx',"Proveedores")
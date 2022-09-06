from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://" + "sanmscom_wp316" + ":" + "6upS4Sr3]" + "@" + "69.167.175.221" + ":" + "3306" + "/" + "sanmscom_wp316" + "?" + "charset=utf8mb4")

conn = engine.connect()


def UploadExcel(archivonombre,tabla):
    excel_f=pd.ExcelFile(archivonombre)
    excel_df=excel_f.parse(sheet_name="Sheet1")
    excel_df=excel_df.set_index('ID')
    excel_df.to_sql(tabla,conn,if_exists="replace",index=True, index_label='ID',)
    query="ALTER TABLE `{table}` ADD PRIMARY KEY (`ID`);".format(table=tabla)
    query2="ALTER TABLE `{table}`CHANGE COLUMN `ID` `ID` BIGINT(20) NOT NULL AUTO_INCREMENT FIRST;".format(table=tabla)
    conn.execute(query)
    conn.execute(query2)

def GetExcel(urldoc,ubicación):
    gsread=pd.read_csv(urldoc,index_col=0)
    gsread.to_excel(ubicación)
    

GetExcel('https://docs.google.com/spreadsheets/d/' + 
                   '1VobD0chAEG5QsMxgiSvcEj5v2q_QqWoKcuHzP9frQFo' +
                   '/export?gid=0&format=csv',"utils/CERTIFICADOS.xlsx")
GetExcel('https://docs.google.com/spreadsheets/d/' + 
                   '1VobD0chAEG5QsMxgiSvcEj5v2q_QqWoKcuHzP9frQFo' +
                   '/export?gid=525308165&format=csv',"utils/Productos.xlsx")
GetExcel('https://docs.google.com/spreadsheets/d/' + 
                   '1VobD0chAEG5QsMxgiSvcEj5v2q_QqWoKcuHzP9frQFo' +
                   '/export?gid=1151957110&format=csv',"utils/Noticias.xlsx")
GetExcel('https://docs.google.com/spreadsheets/d/' + 
                   '1VobD0chAEG5QsMxgiSvcEj5v2q_QqWoKcuHzP9frQFo' +
                   '/export?gid=1385796145&format=csv',"utils/Proveedores.xlsx")


UploadExcel('utils/CERTIFICADOS.xlsx',"Usuarios")
UploadExcel('utils/Noticias.xlsx',"Noticias")
UploadExcel('utils/Productos.xlsx',"Productos")
UploadExcel('utils/Proveedores.xlsx',"Proveedores")
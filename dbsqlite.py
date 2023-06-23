import sqlite3


class Datos:
    conexion = sqlite3.connect("pagos/dbsqlite.db")

    cursor =conexion.cursor()

    #Create Data Base
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pago(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    travel VARCHAR(255),
    person INTEGER, 
    dias VARCHAR(255) , 
    monto REAL
    )""")
    
    conexion.commit()

    #function to add data to database
    def insert(self,travel,person,dias,monto):
        self.cursor.execute('INSERT INTO pago VALUES (null, ?, ?, ?, ?)',(travel,person,dias,monto))
        self.conexion.commit()

    #function to delete data to database
    def delete(self,id):
        self.cursor.execute('DELETE FROM pago WHERE id=?',[id])
        self.conexion.commit()


    def showAll(self):
        self.cursor.execute("SELECT * FROM pago")
        self.pago = self.cursor.fetchall()

        for self.p in self.pago:
            print(self.p)


dato = Datos()

dato.showAll()

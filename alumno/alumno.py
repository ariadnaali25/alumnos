import mysql.connector
from mysql.connector import Error

try: 
    conexion = mysql.connector.connect(
        host= 'localhost',
        port= 3306,
        user= 'root',
        password= '',
        db= 'alumnos-ali'
    )

#insertar dato
    if conexion.is_connected():
        print("conexion exitosa")
        cursor = conexion.cursor()
        nombre = input("Ingrese el nombre: ")
        dni = input("Ingrese el DNI: ")
        domicilio = input("Ingrese el domicilio: ")
        email = input("Ingrese el correo electrónico: ")

        sql = "INSERT INTO alumno (Nombre, DNI, Domicilio, Email) VALUES (%s, %s, %s, %s)"
        val = (nombre, dni, domicilio, email)
        cursor.execute(sql, val)

        conexion.commit()

        print(cursor.rowcount, "registro insertado.")

#EDITAR UN DATO

    cursor = conexion.cursor()
    dni_para_consultar = input("Ingrese el DNI del registro que desea consultar: ")

    cursor.execute("SELECT * FROM alumno WHERE dni = %s", (dni_para_consultar,) )
    result = cursor.fetchone()

    if result:
        print("Registro encontrado:")
        print(result)
        decision = input("¿Desea editar este registro? (si/no): ")

        if decision.lower() == "si":
            nombre = input("Ingrese el nuevo nombre: ")
            domicilio = input("Ingrese el nuevo domicilio: ")
            email = input("Ingrese el nuevo correo electrónico: ")

            sql = "UPDATE alumno SET nombre = %s, domicilio = %s, email = %s WHERE dni = %s"
            val = (nombre, domicilio, email, dni_para_consultar)

            cursor.execute(sql, val)
            conexion.commit()

            print(cursor.rowcount, "registro(s) actualizado(s).")
        else:
            print("No se realizaron cambios en el registro.")
    else:
        print("Registro no encontrado.")

#ELIMINAR
    cursor = conexion.cursor()
    dni_para_eliminar = input("Ingrese el DNI del registro que desea eliminar: ")

    sql = "DELETE FROM alumno WHERE Dni = %s"
    val = (dni_para_eliminar,)

    cursor.execute(sql, val)

    conexion.commit()
    print(cursor.rowcount, "registro eliminado.")

#MOSTRAR TODO

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM alumno")
    result = cursor.fetchall()

    for x in result:
        print(x)

#-----------------------
#NO TOCAR------------------------------
except Error as ex:
    print("error de conexion: ", ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion ha finalizadoo")
#--------------------------------------
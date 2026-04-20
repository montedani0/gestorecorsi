from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO():

    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select codins
                    from corso"""

        cursor.execute(query)


        res = []
        for row in cursor:
            res.append(row["codins"])

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                        from corso"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                nome=row["nome"],
                crediti=row["crediti"],
                pd=row["pd"]
            ))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                   from corso c
                   where c.pd = %s"""

        cursor.execute(query, (pd,))

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getCorsiPDwIscritti(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select c.codins ,c.crediti ,c.nome,c.pd, count(*) as n
                    from corso c, iscrizione i
                    where c.codins = i.codins and c.pd = %s
                    group by c.codins ,c.crediti ,c.nome, c.pd"""

        cursor.execute(query, (pd,))

        res = []
        for row in cursor:
            res.append( (Corso(codins=row["codins"],
                nome=row["nome"],
                crediti=row["crediti"],
                pd=row["pd"]), row["n"]))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT s.* 
                    FROM studente s, iscrizione i
                    WHERE s.matricola = i.matricola and i.codins = %s """

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select s.CDS , count(*) as n
                    from studente s, iscrizione i
                    where s.matricola = i.matricola and i.codins = %s and s.CDS != ""
                    group by s.CDS  """

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append((row["CDS"], row["n"]))

        cursor.close()
        cnx.close()

        return res








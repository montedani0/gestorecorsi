from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()


    def getAllCorsi(self):
        return DAO.getAllCorsi()


    def getCorsiPd(self,pd):
        return DAO.getCorsiPD(pd)


    def getCorsiPDwIscritti(self,pd):
        res = DAO.getCorsiPDwIscritti(pd)
        res.sort(key=lambda s: s[1], reverse=True)
        return res

    def getStudentiCorso (self, codins):
        res =  DAO.getStudentiCorso(codins)
        res.sort(key=lambda s: s.cognome)
        return res


    def getCDSofCorso(self, codins):
        cds = DAO.getCDSofCorso(codins)
        cds.sort(key=lambda c: c[1], reverse=True)
        return cds



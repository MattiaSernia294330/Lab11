from database.DB_connect import DBConnect
from model.Prodotti import Prodotto
from model.Collegamento import Collegamento


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_color():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct(gp.Product_color)
                from go_products gp """

        cursor.execute(query)

        for row in cursor:
            result.append(row['Product_color'])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_Nodi(colore):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
            from go_products gp 
            where gp.Product_color = %s"""

        cursor.execute(query,(colore,))

        for row in cursor:
            result.append(Prodotto(row['Product_number'], row['Product']))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_edge(anno,colore):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT gds1.Product_number AS p1, gds2.Product_number AS p2, gds2.Date AS data
                    FROM go_daily_sales gds1
                    JOIN go_daily_sales gds2 ON gds1.Date = gds2.Date AND gds1.Retailer_code = gds2.Retailer_code
                    JOIN go_products gp1 ON gds1.Product_number = gp1.Product_number
                    JOIN go_products gp2 ON gds2.Product_number = gp2.Product_number
                    WHERE gds1.Product_number < gds2.Product_number 
                    AND YEAR(gds2.Date) = %s
                    AND gp1.Product_color = %s
                    AND gp2.Product_color = gp1.Product_color;"""

        cursor.execute(query, (anno,colore))

        for row in cursor:
            result.append(Collegamento(row['p1'], row['p2'],row['data']))

        cursor.close()
        conn.close()
        return result

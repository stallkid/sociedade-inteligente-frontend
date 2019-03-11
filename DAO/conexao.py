# Importa o modulo de conexao com o mysql
import MySQLdb
#Gera a string de conexao ex.: seu host, seu usuario, sua senha e seu db
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="inteligenciaArtificialDB")



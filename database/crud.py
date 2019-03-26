from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Product

engine = create_engine('sqlite:///products.db')
DBSession = sessionmaker(bind=engine)

###############################################
# FUNCIONES PARA MANEJAR LA BASE DE DATOS

def insert_product(data):
    """ Función que inserta un producto a la Tabla Producto de base de datos.
        Se hace uso de la instancia de una sesión. Commit y Close al final para
        guardar los cambios.
    """
    session = DBSession()
    #
    #
    #
    session.commit()
    session.close()


def get_products():
    """ Función que obtiene todos los productos de la Tabla Producto de la base
        de datos. Se hace uso de la instancia de una sesión. Close cuando ya termina
        el uso de la sesión.
    """
    session = DBSession()
    #
    #
    #
    session.close()

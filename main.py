# TRABAJO EN EQUIPO PARA TALLER DE GIT Y GITHUB
# AAII

# FUNCIONES DE GUI
from interfaz.graficas import (
    gui_presentation,
    gui_confirm_product_registered,
    gui_list_products,
    gui_register_products,
    gui_show_products_list,
    gui_input_error
)

# FUNCIONES DE INPUTS
from interfaz.inputs import (
    input_chosen_option,
    input_register_product
)

# FUNCIONES PARA MANEJO DE BASES DE DATOS
from database.crud import (
    get_products,
    insert_product,
)

def main():
    """ Función principal, pregunta al usuario qué desea realizar:
        - agregar nuevos productos (pedir todos los datos y guardar en base de datos)
        - listar todos los productos (imprimir todo)
    """
    # Presentación
    
    # opción 1
    
    # opción 2

    # error
    
    pass



if __name__ == "__main__":
    main()
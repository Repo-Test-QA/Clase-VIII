# Cada página va a tener su propia clase.
# Cada clase va a tener los elementos que va a utilizar
# y las interacciones que se va a tener sobre la página.

class PageIndex:

    # Al constructor le pasamos el driver, porque vamos a hacer cosas con el driver.
    def __init__(self, my_driver):
        # Asignamos los valores de los elementos por id (textbox) y name (botón) a las propiedades/variables
        self.query_top = 'search_query_top'
        self.query_button = 'submit_search'
        # Estoy pasando el parámetro my driver a driver.
        self.driver = my_driver

    def search(self, item):
        # Estoy pasando el parámetro item (el texto que se va a ingresar en la caja
        # de búsqueda 'search_query_top') a sendkeys
        self.driver.find_element_by_id(self.query_top).send_keys(item)
        self.driver.find_element_by_name(self.query_button).click()

        # Con esto le estamos pasando la responsabilidad al que tiene que realizar las
        # interacciones, es decir mi page object

        # Vamos a crear otro archivo, el cual va a tener una clase, la cual es la página
        # que obtiene los resultados, se va  llamar pageItems.py

# Página que obtiene los resultados, se va a llamar pageItems.py

class PageItems:

    # Al constructor le pasamos el driver, porque vamos a hacer cosas con el driver.
    def __init__(self, my_driver):
        self.no_results_banner = '//*[@id="center_column"]/p'
        self.title_banner = '//*[@id="center_column"]/h1/span[1]'
        self.driver = my_driver

    # Vamos a retornar los Textos y que el Caso de Prueba sea quien verifique las cosas.
    def return_no_element_text(self):
        return self.driver.find_element_by_xpath(self.no_results_banner).text

    def return_section_title(self):
        return self.driver.find_element_by_xpath(self.title_banner).text



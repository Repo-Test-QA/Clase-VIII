from selenium import webdriver

# Librerías de python
import unittest
import time

# Del archivo pageIndex, importame la clase PageIndex,
# Entonces ya puedo crear objetos en esta clase de tipo PageIndex.
from pageIndex import PageIndex

# Del archivo pageItems, importame la clase PageItems,
# Entonces ya puedo crear objetos en esta clase de tipo PageItems.
from pageItems import PageItems

class SearchCases(unittest.TestCase):

    # Método que tiene las Precondiciones
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        # Abrir el browser
        self.driver.get('http://automationpractice.com/index.php')

        # Creamos un objeto de la clase PageIndex, le vamos a pasar el parámetro driver.
        self.indexPage = PageIndex(self.driver)

        # Creamos un objeto de la clase PageItems, le vamos a pasar el parámetro driver.
        self.itemsPage = PageItems(self.driver)


    def test_search_no_elements(self):
        self.indexPage.search('hola')
        # Vamos a esperar dos segundos, para que cargue la página
        # con sus elementos.
        time.sleep(2)

        self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "hola"')

        # Verificamos que si ingreso un texto que no existe,
        # se muestre el mensaje en la página  => No results were found for your search "hola"
        # Mediante el assertEqual, comparamos si las dos variables son iguales.
        # Cuando encontremos el xpath, vamos a extraer el texto, para asignarlo a la variable
        # result y así compararla con el texto de la variable expected_result
        # result = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        # expected_result = 'No results were found for your search "hola"'

        # Comentamos las dos variables de arriba, en el assert reemplazamos los valores de las
        # variables y nos ahorramos dos lineas de código
        #self.assertEqual(self.driver.find_element_by_xpath('//*[@id="center_column"]/p').text, 'No results were found for your search "hola"')


    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        time.sleep(2)

        self.assertTrue("DRESS" in self.itemsPage.return_section_title())

        # Mediante el assertTrue.
        # cuando encontremos el xpath, vamos a extraer el texto, para asignarlo a la variable
        # result y así compararla con el texto de la variable expected_result
        #result = driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text
        #expected_result = "DRESS"

        # el texto DRESS se encuentra en el texto que tiene la variable result.
        # Comentamos las dos variables de arriba, en el assert reemplazamos los valores de las
        # variables y nos ahorramos dos lineas de código
        #self.assertTrue("DRESS" in self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text)


    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirts')
        time.sleep(2)

        self.assertTrue('T-SHIRTS' in self.itemsPage.return_section_title(), self.itemsPage.return_section_title())

        # El 3er parámetro es un mensaje, el cual muestra lo que tiene como texto encontrado
        # mediante el xpath.
        # Si no se encuentra el texto que ingresamos "T-SHIRTS" en el texto que encuentra el xpath
        # muestra el texto que ha encontrado.
        # Este es el error que se muestra => AssertionError: False is not true : "T-SHIRT"
        #self.assertTrue('T-SHIRTS' in self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text, self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text)


    # Método que tiene las Postcondiciones, que quiero que pase, cuando termina una prueba.
    def tearDown(self):
        # Cerrar el browser
        self.driver.close()
        # Cerrar la sesión del webdriver
        self.driver.quit()





if __name__ == '__main__':
    # Las pruebas que encuentre acá, las va a ir ejecutando.
    unittest.main()

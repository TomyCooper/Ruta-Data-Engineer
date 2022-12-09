import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('/Users/tomycooper/Documents/Ruta Data Engineer/Curso de Python: Comprehensions, Funciones y Manejo de Errores/app/data.csv')

    country = input('Ingresa el país:')
    
    country_dict = utils.population_by_country(data, country)

    if len(country_dict) > 0:
        country = country_dict[0]
        labels,values = utils.get_population(country)

        charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
    run()
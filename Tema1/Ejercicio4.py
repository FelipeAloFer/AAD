import csv
import json

class FileConverter:
    def json_to_csv(self, csv_file, json_file):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                with open(csv_file, mode='w', newline='') as f:
                    claves = list(data[0].keys())
                    writer = csv.DictWriter(f, fieldnames=claves)
                    writer.writeheader()
                    for row in data: 
                        writer.writerow(row)
                    print(f'Conversión de {json_file} a {csv_file} completada.')
        except Exception as e:
            print(f"Error en la conversión: {e}")
# Uso
converter = FileConverter()
converter.json_to_csv('data.csv', 'data.json')

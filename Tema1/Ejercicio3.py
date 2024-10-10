import json;

class JSONFileHandler:
    def read_json(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error leyendo JSON: {e}")

    def write_json(self, file_path, data):
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Error escribiendo JSON: {e}")

#Uso
json_handler = JSONFileHandler()

data = {
    "DNI": "77852571",
    "fecha_nacimiento": "04/05/2005"
}

json_handler.write_json('data2.json', data)
data2 = json_handler.read_json('data2.json')
print(data2)

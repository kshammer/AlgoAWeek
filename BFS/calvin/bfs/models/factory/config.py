class ConfigFactory:

    def createGraphConfig(self, data):
        lines = data.splitlines()
        for line in lines:
            print(f'line={line}')
            node_config = line.split("=",1)
            key = node_config[0]
            value = node_config[1].strip("{}")
            print(f'key={key} value={value}')
            



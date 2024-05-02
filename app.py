from zeep import Client

client = Client('http://localhost/soap-web-service/calculator.wsdl')
print(client.service.add(1, 2))
from ejemplo.models import Familiar

Familiar(nombre="Osvaldo", direccion="Toluca, México", numero_pasaporte=428300).save()
Familiar(nombre="Margarte", direccion="Guadalajara, México", numero_pasaporte=123123).save()
Familiar(nombre="Adriana", direccion="Monterrey, México", numero_pasaporte=890890).save()
Familiar(nombre="Francisca", direccion="Ciudad de México, México", numero_pasaporte=345345).save()
Familiar(nombre="Oscar", direccion="Baja California Sur, Mexico", numero_pasaporte=567567).save()

print("Se cargo con éxito los usuarios de pruebas")
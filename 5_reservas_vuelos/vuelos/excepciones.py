class OverbookingError(Exception):
    """Excepción lanzada cuando la lista de asientos ocupados iguala la capacidad total del vuelo."""
    pass

class ReservaInvalidaError(Exception):
    """Excepción lanzada cuando los datos del pasajero (ID o Nombre) están corruptos o incompletos."""
    pass

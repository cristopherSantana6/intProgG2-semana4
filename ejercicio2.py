#tipos de datos numericos
cantidad=10
precio=130
total= cantidad*precio


def ftexto(texto):
    return f"{texto:<10}"

print(f"{ftexto("cantidad: ")} {cantidad:>6}")
print(f"{ftexto('precio: ')} {precio:>6}")
print(f"{ftexto('total: ')} {total:>6}")
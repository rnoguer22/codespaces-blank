from setuptools import setup

setup(
    name="paquete",
    version="1.0",
    description="Paquete de prueba",
    author="Moyis",
    package=["paquete", "paquete.hola", "paquete.adios"],
    scripts = [""]
)
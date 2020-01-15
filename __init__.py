# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""


import ctypes


"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")


if module == "dialog_":

    title_ = GetParams('title_')
    msg_ = GetParams('msg_')
    var_ = GetParams('var_')

    res = ctypes.windll.user32.MessageBoxW(0,msg_, title_, 1)

    if res == 1:
        res = True
    else:
        res = False

    SetVar(var_,res)


import aima3.utils
import aima3.logic
from aima3.logic import pl_resolution


def getClauses():
    clauses = []


    # clausulas del usuario a BC

    #1 - En que pais o Ciudad le gustaria trabajar?
    #KB.tell(aima3.utils.expr("PaisUser(Unlugar)"))
    #KB.tell(aima3.utils.expr("CiudadUser(Unlugar)"))

    #2 - En que Leguaje o framework ha trabajado?
    # KB.tell(aima3.utils.expr("LengUser(unLenguaje)"))
    # KB.tell(aima3.utils.expr("CiudadUser(UnFramewok)"))

    # 3 - que nivel de señority / experiencia posee en el lenguaje o framework? (Pasante /Junior / Semi-senior / Senior)
    # KB.tell(aima3.utils.expr("ExpLengUser(unLenguaje)"))
    # KB.tell(aima3.utils.expr("ExpFrameUser(UnFramewok)"))

    # 4 - Posee manejo de alguna lengua extranjera?
    # KB.tell(aima3.utils.expr("IdiomasUser(unIdioma)"))

    # 5 - Posemos 3 tipos de modalidad de trabajo, Presencial, remoto o Mixto, cual es de su preferencia?
    # KB.tell(aima3.utils.expr("ModalidadUser(unaModalidad)"))

    # 6 - Que Disponibilidad horaria posee para el trabajo? (Part-time / Full-time / Freelance)
    # KB.tell(aima3.utils.expr("DisponibilidadUser(unaDisponibilidad)"))

    # 7 - Participó en algún equipo de trabajo? Cual fue su rolo en el mismo? (Lider/ Referente/ Colaborador)
    # KB.tell(aima3.utils.expr("RolEquipoUser(unRol)"))

    # 8 - Ha Gestionado multiples equipos de trabajo? (Lider/ Colaborador)
    # KB.tell(aima3.utils.expr("RolMultiEquipoUser(unRol)"))

    # 9 - En cuanto a desarrollo, con que tipos de optimizaciones esta familiarizado? (Cpu/ Memoria / Db /Navegador)
    # KB.tell(aima3.utils.expr("OptimizaUser(unRol)"))

    # 10 - Está familiarizado con las arquitecturas Cloud y/o On-premise? (Cloud / On-premise)
    # KB.tell(aima3.utils.expr("arquitecUser(unaArquitec)"))

    # 11 - Que nivel se sueldo espera percibir? (Bajo/Medio/Alto)
    # KB.tell(aima3.utils.expr("SueldoUser(unSueldo)"))

    #12 - Durante su carrera en IT, ha tenido que tomar desiciones estatégias y/o técnicas a nivel departamental y/o organizacional? ( Si/No)
    # KB.tell(aima3.utils.expr("MetasUser(unaMeta)"))





    clauses.append(aima3.utils.expr("LengUser(x) & LengOrientado(x,Backend) ==> Orientacionuser(Backend)"))
    clauses.append(aima3.utils.expr("LengUser(x) & LengOrientado(x,Frontend) ==> Orientacionuser(Frontend)"))
    clauses.append(aima3.utils.expr("LengUser(x) & LengOrientado(x,Dba) ==> Orientacionuser(Dba)"))



    # PUESTOS DISPONIBLES

    # Puestos FrontEnd
    clauses.append(aima3.utils.expr(
        "Orientacionuser(Frontend) & ExpFrameUser(Junior) & ExpLengUser(Junior) & ModalidadUser(Presencial) & SueldoUser(Bajo) ==> Puesto(Frontend)"))

    clauses.append(aima3.utils.expr(
        "Orientacionuser(Frontend) & ExpFrameUser(Senior) & ExpLengUser(Senior) & ModalidadUser(Remoto) & SueldoUser(Medio) & IdiomasUser(Ingles) ==> Puesto(Frontend)"))


    # Puestos Backend
    clauses.append(aima3.utils.expr(
        "Orientacionuser(Backend) & ExpFrameUser(Senior) & ExpLengUser(Senior)  & ModalidadUser(Remoto) & SueldoUser(Medio) & IdiomasUser(x)  ==> Puesto(Backend)"))

    # Puestos Fullstack
    clauses.append(aima3.utils.expr(
        "Orientacionuser(Backend) & Orientacionuser(Frontend) & ExpFrameUser(Semi_senior) & ExpLengUser(Senior)  & ModalidadUser(Remoto) & SueldoUser(Medio) & OptimizaUser(x) & IdiomasUser(Ingles) ==> Puesto(Fullstack)"))

    # Puestos DBA
    clauses.append(aima3.utils.expr(
        "Orientacionuser(Dba) & ExpLengUser(Junior) & ModalidadUser(Presencial) & OptimizaUser(Db) ==> Puesto(Dba)"))

    # Puestos TeamLeader
    clauses.append(aima3.utils.expr(
        "Orientacionuser(X) & ExpFrameUser(Senior) & ExpLengUser(Senior) & ModalidadUser(Presencial) & IdiomasUser(Ingles) & RolEquipoUser(Lider) & SueldoUser(Medio)==> Puesto(TeamLeader)"))

    # Puestos SoftwareEngineerManager
    clauses.append(aima3.utils.expr(
        "Orientacionuser(Backend) & Orientacionuser(Frontend) & ExpLengUser(Semi_senior) & OptimizaUser(x) & IdiomasUser(Ingles) & ModalidadUser(Mixto) & RolMultiEquipoUser(Lider) & SueldoUser(Alto) ==> Puesto(Softwareengineermanager)"))


    # Puestos Cto
    clauses.append(aima3.utils.expr("Puesto(SoftwareEngineerManager) & MetasUser(Si) & SueldoUser(Alto) ==> Puesto(Cto)"))


    #-------------------

    clauses.append(aima3.utils.expr("Lenguaje(Python)"))
    clauses.append(aima3.utils.expr("Lenguaje(Java)"))
    clauses.append(aima3.utils.expr("Lenguaje(Ruby)"))
    clauses.append(aima3.utils.expr("Lenguaje(Swift)"))
    clauses.append(aima3.utils.expr("Lenguaje(Go)"))
    clauses.append(aima3.utils.expr("Lenguaje(Rust)"))
    clauses.append(aima3.utils.expr("Lenguaje(PHP)"))
    clauses.append(aima3.utils.expr("Lenguaje(Haskell)"))
    clauses.append(aima3.utils.expr("Lenguaje(Perl)"))
    clauses.append(aima3.utils.expr("Lenguaje(Objective_c)"))
    clauses.append(aima3.utils.expr("Lenguaje(Kotlin)"))
    clauses.append(aima3.utils.expr("Lenguaje(Scala)"))
    clauses.append(aima3.utils.expr("Lenguaje(R)"))
    clauses.append(aima3.utils.expr("Lenguaje(Lua)"))
    clauses.append(aima3.utils.expr("Lenguaje(Matlab)"))
    clauses.append(aima3.utils.expr("Lenguaje(Groovy)"))
    clauses.append(aima3.utils.expr("Lenguaje(Clojure)"))
    clauses.append(aima3.utils.expr("Lenguaje(Shell)"))
    clauses.append(aima3.utils.expr("Lenguaje(Assembly)"))
    clauses.append(aima3.utils.expr("Lenguaje(Elixir)"))
    clauses.append(aima3.utils.expr("Lenguaje(Julia)"))
    clauses.append(aima3.utils.expr("Lenguaje(Racket)"))
    clauses.append(aima3.utils.expr("Lenguaje(Fortran)"))
    clauses.append(aima3.utils.expr("Lenguaje(JavaScript)"))
    clauses.append(aima3.utils.expr("Lenguaje(TypeScript)"))
    clauses.append(aima3.utils.expr("Lenguaje(Html)"))
    clauses.append(aima3.utils.expr("Lenguaje(Css)"))
    clauses.append(aima3.utils.expr("Lenguaje(Dart)"))
    clauses.append(aima3.utils.expr("Lenguaje(Mysql)"))
    clauses.append(aima3.utils.expr("Lenguaje(Mongodb)"))
    clauses.append(aima3.utils.expr("Lenguaje(Mariadb)"))
    clauses.append(aima3.utils.expr("Lenguaje(Sql)"))

    clauses.append(aima3.utils.expr("Framework(React)"))
    clauses.append(aima3.utils.expr("Framework(Angular)"))
    clauses.append(aima3.utils.expr("Framework(Django)"))
    clauses.append(aima3.utils.expr("Framework(Rubyonrails)"))
    clauses.append(aima3.utils.expr("Framework(Laravel)"))
    clauses.append(aima3.utils.expr("Framework(Spring)"))
    clauses.append(aima3.utils.expr("Framework(Flask)"))
    clauses.append(aima3.utils.expr("Framework(Symfony)"))
    clauses.append(aima3.utils.expr("Framework(Flutter)"))
    clauses.append(aima3.utils.expr("Framework(Meteor)"))
    clauses.append(aima3.utils.expr("Framework(Playframework)"))
    clauses.append(aima3.utils.expr("Framework(Cakephp)"))
    clauses.append(aima3.utils.expr("Framework(Codeigniter)"))
    clauses.append(aima3.utils.expr("Framework(Playframework)"))
    clauses.append(aima3.utils.expr("Framework(Angular)"))

    clauses.append(aima3.utils.expr("Utiliza(Angular,JavaScript)"))
    clauses.append(aima3.utils.expr("Utiliza(Angular,TypeScript)"))
    clauses.append(aima3.utils.expr("Utiliza(Cakephp,php)"))
    clauses.append(aima3.utils.expr("Utiliza(Codeigniter,php)"))
    clauses.append(aima3.utils.expr("Utiliza(Django,Python)"))
    clauses.append(aima3.utils.expr("Utiliza(Flask,Python)"))
    clauses.append(aima3.utils.expr("Utiliza(Flutter,Dart)"))
    clauses.append(aima3.utils.expr("Utiliza(Laravel,Php)"))
    clauses.append(aima3.utils.expr("Utiliza(Meteor,Javascript)"))
    clauses.append(aima3.utils.expr("Utiliza(Play_framework,Java)"))
    clauses.append(aima3.utils.expr("Utiliza(Play_framework,Scala)"))
    clauses.append(aima3.utils.expr("Utiliza(React,Javascript)"))
    clauses.append(aima3.utils.expr("Utiliza(Ruby_on_rails,Ruby)"))
    clauses.append(aima3.utils.expr("Utiliza(Spring,Java)"))
    clauses.append(aima3.utils.expr("Utiliza(Symfony,Php)"))

    clauses.append(aima3.utils.expr("LengOrientado(Python,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Java,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Ruby,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Swift,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Go,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Rust,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Php,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Haskell,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Perl,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Objective_c,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Kotlin,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Scala,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(R,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Lua,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Matlab,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Groovy,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Clojure,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Shell,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(MySQL,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Mongodb,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(mariadb,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Sql,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Assembly,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Elixir,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Julia,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Racket,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Fortran,Backend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Javascript,Frontend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Typescript,Frontend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Html,Frontend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Css,Frontend)"))
    clauses.append(aima3.utils.expr("LengOrientado(Dart,Frontend)"))

    clauses.append(aima3.utils.expr("Pais(Estados_unidos)"))
    clauses.append(aima3.utils.expr("Pais(Argentina)"))
    clauses.append(aima3.utils.expr("Pais(Brasil)"))
    clauses.append(aima3.utils.expr("Pais(Uruguay)"))
    clauses.append(aima3.utils.expr("Pais(Paraguay)"))
    clauses.append(aima3.utils.expr("Pais(Chile)"))
    clauses.append(aima3.utils.expr("Pais(Bolivia)"))
    clauses.append(aima3.utils.expr("Pais(México)"))
    clauses.append(aima3.utils.expr("Pais(Inglaterra)"))
    clauses.append(aima3.utils.expr("Pais(Francia)"))
    clauses.append(aima3.utils.expr("Pais(Alemania)"))

    clauses.append(aima3.utils.expr("Ciudad(Berlín)"))
    clauses.append(aima3.utils.expr("Ciudad(Múnich)"))
    clauses.append(aima3.utils.expr("Ciudad(Hamburgo)"))
    clauses.append(aima3.utils.expr("Ciudad(Fráncfort)"))
    clauses.append(aima3.utils.expr("Ciudad(Colonia)"))
    clauses.append(aima3.utils.expr("Ciudad(Buenos_Aires)"))
    clauses.append(aima3.utils.expr("Ciudad(Córdoba)"))
    clauses.append(aima3.utils.expr("Ciudad(Rosario)"))
    clauses.append(aima3.utils.expr("Ciudad(Mendoza)"))
    clauses.append(aima3.utils.expr("Ciudad(Mar_del_Plata)"))
    clauses.append(aima3.utils.expr("Ciudad(La_Paz)"))
    clauses.append(aima3.utils.expr("Ciudad(Santa_Cruz_de_la_Sierra)"))
    clauses.append(aima3.utils.expr("Ciudad(Cochabamba)"))
    clauses.append(aima3.utils.expr("Ciudad(Sucre)"))
    clauses.append(aima3.utils.expr("Ciudad(Potosí)"))
    clauses.append(aima3.utils.expr("Ciudad(São_Paulo)"))
    clauses.append(aima3.utils.expr("Ciudad(Río_de_Janeiro)"))
    clauses.append(aima3.utils.expr("Ciudad(Brasilia)"))
    clauses.append(aima3.utils.expr("Ciudad(Salvador)"))
    clauses.append(aima3.utils.expr("Ciudad(Belo_Horizonte)"))
    clauses.append(aima3.utils.expr("Ciudad(Santiago)"))
    clauses.append(aima3.utils.expr("Ciudad(Valparaíso)"))
    clauses.append(aima3.utils.expr("Ciudad(Viña_del_mar)"))
    clauses.append(aima3.utils.expr("Ciudad(Concepción)"))
    clauses.append(aima3.utils.expr("Ciudad(La_serena)"))
    clauses.append(aima3.utils.expr("Ciudad(Nueva_york)"))
    clauses.append(aima3.utils.expr("Ciudad(Los_angeles)"))
    clauses.append(aima3.utils.expr("Ciudad(Chicago)"))
    clauses.append(aima3.utils.expr("Ciudad(Miami)"))
    clauses.append(aima3.utils.expr("Ciudad(San_francisco)"))
    clauses.append(aima3.utils.expr("Ciudad(Paris)"))
    clauses.append(aima3.utils.expr("Ciudad(Marsella)"))
    clauses.append(aima3.utils.expr("Ciudad(Lyon)"))
    clauses.append(aima3.utils.expr("Ciudad(Toulouse)"))
    clauses.append(aima3.utils.expr("Ciudad(Niza)"))
    clauses.append(aima3.utils.expr("Ciudad(Londres)"))
    clauses.append(aima3.utils.expr("Ciudad(Manchester)"))
    clauses.append(aima3.utils.expr("Ciudad(Birmingham)"))
    clauses.append(aima3.utils.expr("Ciudad(Liverpool)"))
    clauses.append(aima3.utils.expr("Ciudad(Bristol)"))
    clauses.append(aima3.utils.expr("Ciudad(Ciudad_de_méxico)"))
    clauses.append(aima3.utils.expr("Ciudad(Cancún)"))
    clauses.append(aima3.utils.expr("Ciudad(Guadalajara)"))
    clauses.append(aima3.utils.expr("Ciudad(Monterrey)"))
    clauses.append(aima3.utils.expr("Ciudad(Tijuana)"))
    clauses.append(aima3.utils.expr("Ciudad(Asunción)"))
    clauses.append(aima3.utils.expr("Ciudad(Ciudad_del_este)"))
    clauses.append(aima3.utils.expr("Ciudad(Encarnación)"))
    clauses.append(aima3.utils.expr("Ciudad(Luque)"))
    clauses.append(aima3.utils.expr("Ciudad(San_Lorenzo)"))
    clauses.append(aima3.utils.expr("Ciudad(Montevideo)"))
    clauses.append(aima3.utils.expr("Ciudad(Punta_del_este)"))
    clauses.append(aima3.utils.expr("Ciudad(Colonia_del_Sacramento)"))
    clauses.append(aima3.utils.expr("Ciudad(Salto)"))
    clauses.append(aima3.utils.expr("Ciudad(Piriápolis)"))

    clauses.append(aima3.utils.expr("CiudadPais(Berlín,Alemania)"))
    clauses.append(aima3.utils.expr("CiudadPais(Múnich,Alemania)"))
    clauses.append(aima3.utils.expr("CiudadPais(Hamburgo,Alemania)"))
    clauses.append(aima3.utils.expr("CiudadPais(Fráncfort,Alemania)"))
    clauses.append(aima3.utils.expr("CiudadPais(Colonia,Alemania)"))
    clauses.append(aima3.utils.expr("CiudadPais(BuenosAires,Argentina)"))
    clauses.append(aima3.utils.expr("CiudadPais(Córdoba,Argentina)"))
    clauses.append(aima3.utils.expr("CiudadPais(Rosario,Argentina)"))
    clauses.append(aima3.utils.expr("CiudadPais(Mendoza,Argentina)"))
    clauses.append(aima3.utils.expr("CiudadPais(Mar_del_plata,Argentina)"))
    clauses.append(aima3.utils.expr("CiudadPais(La_Paz,Bolivia)"))
    clauses.append(aima3.utils.expr("CiudadPais(Santa_cruz_de_la_sierra,Bolivia)"))
    clauses.append(aima3.utils.expr("CiudadPais(Cochabamba,Bolivia)"))
    clauses.append(aima3.utils.expr("CiudadPais(Sucre,Bolivia)"))
    clauses.append(aima3.utils.expr("CiudadPais(Potosí,Bolivia)"))
    clauses.append(aima3.utils.expr("CiudadPais(São_Paulo,Brasil)"))
    clauses.append(aima3.utils.expr("CiudadPais(Río_de_janeiro,Brasil)"))
    clauses.append(aima3.utils.expr("CiudadPais(Brasilia,Brasil)"))
    clauses.append(aima3.utils.expr("CiudadPais(Salvador,Brasil)"))
    clauses.append(aima3.utils.expr("CiudadPais(Belo_horizonte,Brasil)"))
    clauses.append(aima3.utils.expr("CiudadPais(Santiago,Chile)"))
    clauses.append(aima3.utils.expr("CiudadPais(Valparaíso,Chile)"))
    clauses.append(aima3.utils.expr("CiudadPais(Viña_del_mar,Chile)"))
    clauses.append(aima3.utils.expr("CiudadPais(Concepción,Chile)"))
    clauses.append(aima3.utils.expr("CiudadPais(La_serena,Chile)"))
    clauses.append(aima3.utils.expr("CiudadPais(NuevaYork,Estados_unidos)"))
    clauses.append(aima3.utils.expr("CiudadPais(Los_angeles,Estados_unidos)"))
    clauses.append(aima3.utils.expr("CiudadPais(Chicago,Estados_unidos)"))
    clauses.append(aima3.utils.expr("CiudadPais(Miami,Estados_unidos)"))
    clauses.append(aima3.utils.expr("CiudadPais(San_francisco,Estados_unidos)"))
    clauses.append(aima3.utils.expr("CiudadPais(Paris,Francia)"))
    clauses.append(aima3.utils.expr("CiudadPais(Marsella,Francia)"))
    clauses.append(aima3.utils.expr("CiudadPais(Lyon,Francia)"))
    clauses.append(aima3.utils.expr("CiudadPais(Toulouse,Francia)"))
    clauses.append(aima3.utils.expr("CiudadPais(Niza,Francia)"))
    clauses.append(aima3.utils.expr("CiudadPais(Londres,Inglaterra)"))
    clauses.append(aima3.utils.expr("CiudadPais(Manchester,Inglaterra)"))
    clauses.append(aima3.utils.expr("CiudadPais(Birmingham,Inglaterra)"))
    clauses.append(aima3.utils.expr("CiudadPais(Liverpool,Inglaterra)"))
    clauses.append(aima3.utils.expr("CiudadPais(Bristol,Inglaterra)"))
    clauses.append(aima3.utils.expr("CiudadPais(Ciudad_de_méxico,Mexico)"))
    clauses.append(aima3.utils.expr("CiudadPais(Cancún,Mexico)"))
    clauses.append(aima3.utils.expr("CiudadPais(Guadalajara,Mexico)"))
    clauses.append(aima3.utils.expr("CiudadPais(Monterrey,Mexico)"))
    clauses.append(aima3.utils.expr("CiudadPais(Tijuana,Mexico)"))
    clauses.append(aima3.utils.expr("CiudadPais(Asunción,Paraguay)"))
    clauses.append(aima3.utils.expr("CiudadPais(Ciudad_del_este,Paraguay)"))
    clauses.append(aima3.utils.expr("CiudadPais(Encarnación,Paraguay)"))
    clauses.append(aima3.utils.expr("CiudadPais(Luque,Paraguay)"))
    clauses.append(aima3.utils.expr("CiudadPais(SanLorenzo,Paraguay)"))
    clauses.append(aima3.utils.expr("CiudadPais(Montevideo,Uruguay)"))
    clauses.append(aima3.utils.expr("CiudadPais(Punta_del_este,Uruguay)"))
    clauses.append(aima3.utils.expr("CiudadPais(Colonia_del_sacramento,Uruguay)"))
    clauses.append(aima3.utils.expr("CiudadPais(Salto,Uruguay)"))
    clauses.append(aima3.utils.expr("CiudadPais(Piriápolis,Uruguay)"))

    clauses.append(aima3.utils.expr("Experiencia(Senior)"))
    clauses.append(aima3.utils.expr("Experiencia(Semi_senior)"))
    clauses.append(aima3.utils.expr("Experiencia(Junior)"))
    clauses.append(aima3.utils.expr("Experiencia(Pasante)"))

    clauses.append(aima3.utils.expr("Idioma(Inglés)"))
    clauses.append(aima3.utils.expr("Idioma(Español)"))
    clauses.append(aima3.utils.expr("Idioma(Italiano)"))
    clauses.append(aima3.utils.expr("Idioma(Portugués)"))
    clauses.append(aima3.utils.expr("Idioma(Francés)"))
    clauses.append(aima3.utils.expr("Idioma(Alemán)"))

    clauses.append(aima3.utils.expr("Modalidad(Presencial)"))
    clauses.append(aima3.utils.expr("Modalidad(Virtual)"))
    clauses.append(aima3.utils.expr("Modalidad(Mixta)"))

    clauses.append(aima3.utils.expr("Disponibilidad(Part-time)"))
    clauses.append(aima3.utils.expr("Disponibilidad(Full-time)"))
    clauses.append(aima3.utils.expr("Disponibilidad(Freelance)"))

    clauses.append(aima3.utils.expr("TrabajoenEquipo(Lider)"))
    clauses.append(aima3.utils.expr("TrabajoenEquipo(Referente)"))
    clauses.append(aima3.utils.expr("TrabajoenEquipo(Colaborador)"))

    clauses.append(aima3.utils.expr("CoordinacionEquipos(Colaborador)"))
    clauses.append(aima3.utils.expr("CoordinacionEquipos(Lider)"))

    clauses.append(aima3.utils.expr("Optimizaciones(Cpu)"))
    clauses.append(aima3.utils.expr("Optimizaciones(Memoria)"))
    clauses.append(aima3.utils.expr("Optimizaciones(Db)"))
    clauses.append(aima3.utils.expr("Optimizaciones(Navegador)"))

    clauses.append(aima3.utils.expr("OptimizaOrientacion(Cpu,Backend)"))
    clauses.append(aima3.utils.expr("OptimizaOrientacion(Memoria,Frontend)"))
    clauses.append(aima3.utils.expr("OptimizaOrientacion(Navegador,Frontend)"))
    clauses.append(aima3.utils.expr("OptimizaOrientacion(Db,Backend)"))
    clauses.append(aima3.utils.expr("OptimizaOrientacion(Cpu,Dba)"))

    clauses.append(aima3.utils.expr("Sueldo(Bajo)"))
    clauses.append(aima3.utils.expr("Sueldo(Medio)"))
    clauses.append(aima3.utils.expr("Sueldo(Alto)"))

    clauses.append(aima3.utils.expr("Arquitectura(Cloud)"))
    clauses.append(aima3.utils.expr("Arquitectura(Onpremise)"))




    return clauses


def initKB():
    KB = aima3.logic.FolKB(getClauses())
    return KB


if __name__ == '__main__':
    KB = initKB()

    #consulta = aima3.utils.expr("LengUser(Java)")
    #La afirmación es falsa(no esta explicita en la BC). KB.ask = {v_5: Java}

    #consulta = aima3.utils.expr("LengUser(Pepe)")
    #La afirmación es falsa.(no esta explicita en la BC) KB.ask = False ( no se deduce de las reglas)




    consulta = aima3.utils.expr("Puesto(Backend)")



    if pl_resolution(KB, consulta):
        print("Esta en la BC")
    else:
        print("No esta en la BC")

    print("KB.ask= ", KB.ask(consulta))


# TEST
    print("KB.ask= ", KB.ask(aima3.utils.expr("Puesto(Frontend)")))
    print("KB.ask= ", KB.ask(aima3.utils.expr("Puesto(Backend)")))
    print("KB.ask= ", KB.ask(aima3.utils.expr("Puesto(Fullstack)")))
    print("KB.ask= ", KB.ask(aima3.utils.expr("Puesto(TeamLeader)")))
    print("KB.ask= ", KB.ask(aima3.utils.expr("Puesto(Softwareengineermanager)")))
    print("KB.ask= ", KB.ask(aima3.utils.expr("Puesto(Cto)")))



import aima3.utils


def getClausses():
    clausses = []

    # clausulas del usuario a BC

    # 1 - En que pais o Ciudad le gustaria trabajar?
    # KB.tell(aima3.utils.expr("PaisUser(Unlugar)"))
    # KB.tell(aima3.utils.expr("CiudadUser(Unlugar)"))

    # 2 - En que Leguaje o framework ha trabajado?
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

    # 12 - Durante su carrera en IT, ha tenido que tomar desiciones estatégias y/o técnicas a nivel departamental y/o organizacional? ( Si/No)
    # KB.tell(aima3.utils.expr("MetasUser(unaMeta)"))

    clausses.append(aima3.utils.expr("LengUser(x) & LengOrientado(x,Backend) ==> Orientacionuser(Backend)"))
    clausses.append(aima3.utils.expr("LengUser(x) & LengOrientado(x,Frontend) ==> Orientacionuser(Frontend)"))
    clausses.append(aima3.utils.expr("LengUser(x) & LengOrientado(x,Dba) ==> Orientacionuser(Dba)"))

    # PUESTOS DISPONIBLES

    clausses.append(aima3.utils.expr(
        "Orientacionuser(Backend) & ModalidadUser(Presencial) & UserPais(Argentina) & DisponibilidadUser(Full-time) & TrabajoenEquipo(Lider)  ==> Puesto(TeamLeader)"))



    # Puestos FrontEnd


    clausses.append(aima3.utils.expr(
        "Orientacionuser(Frontend) & ExpFrameUser(Junior) & ExpLengUser(Junior) & ModalidadUser(Presencial) & SueldoUser(Bajo) ==> Puesto(Frontend)"))


    clausses.append(aima3.utils.expr(
        "Orientacionuser(Frontend) & ExpFrameUser(Senior) & ExpLengUser(Senior) & ModalidadUser(Remoto) & SueldoUser(Medio) & IdiomasUser(Ingles) ==> Puesto(Frontend)"))

    # Puestos Backend
    clausses.append(aima3.utils.expr(
        "Orientacionuser(Backend) & ExpFrameUser(Senior) & ExpLengUser(Senior)  & ModalidadUser(Remoto) & SueldoUser(Medio) & IdiomasUser(x)  ==> Puesto(Backend)"))

    # Puestos Fullstack
    clausses.append(aima3.utils.expr(
        "Orientacionuser(Backend) & Orientacionuser(Frontend) & ExpFrameUser(Semi_senior) & ExpLengUser(Senior)  & ModalidadUser(Remoto) & SueldoUser(Medio) & OptimizaUser(x) & IdiomasUser(Ingles) ==> Puesto(Fullstack)"))

    # Puestos DBA
    clausses.append(aima3.utils.expr(
        "Orientacionuser(Dba) & ExpLengUser(Junior) & ModalidadUser(Presencial) & OptimizaUser(Db) ==> Puesto(Dba)"))

    # Puestos TeamLeader


    clausses.append(aima3.utils.expr(
        "Orientacionuser(X) & ExpFrameUser(Senior) & ExpLengUser(Senior) & ModalidadUser(Presencial) & IdiomasUser(Ingles) & RolEquipoUser(Lider) & SueldoUser(Medio)==> Puesto(TeamLeader)"))

    # Puestos SoftwareEngineerManager
    clausses.append(aima3.utils.expr(
        "Orientacionuser(Backend) & Orientacionuser(Frontend) & ExpLengUser(Semi_senior) & OptimizaUser(x) & IdiomasUser(Ingles) & ModalidadUser(Mixto) & RolMultiEquipoUser(Lider) & SueldoUser(Alto) ==> Puesto(Softwareengineermanager)"))

    # Puestos Cto
    clausses.append(
        aima3.utils.expr("Puesto(SoftwareEngineerManager) & MetasUser(Si) & SueldoUser(Alto) ==> Puesto(Cto)"))

    # -------------------

    clausses.append(aima3.utils.expr("Lenguaje(Python)"))
    clausses.append(aima3.utils.expr("Lenguaje(Java)"))
    clausses.append(aima3.utils.expr("Lenguaje(Ruby)"))
    clausses.append(aima3.utils.expr("Lenguaje(Swift)"))
    clausses.append(aima3.utils.expr("Lenguaje(Go)"))
    clausses.append(aima3.utils.expr("Lenguaje(Rust)"))
    clausses.append(aima3.utils.expr("Lenguaje(PHP)"))
    clausses.append(aima3.utils.expr("Lenguaje(Haskell)"))
    clausses.append(aima3.utils.expr("Lenguaje(Perl)"))
    clausses.append(aima3.utils.expr("Lenguaje(Objective_c)"))
    clausses.append(aima3.utils.expr("Lenguaje(Kotlin)"))
    clausses.append(aima3.utils.expr("Lenguaje(Scala)"))
    clausses.append(aima3.utils.expr("Lenguaje(R)"))
    clausses.append(aima3.utils.expr("Lenguaje(Lua)"))
    clausses.append(aima3.utils.expr("Lenguaje(Matlab)"))
    clausses.append(aima3.utils.expr("Lenguaje(Groovy)"))
    clausses.append(aima3.utils.expr("Lenguaje(Clojure)"))
    clausses.append(aima3.utils.expr("Lenguaje(Shell)"))
    clausses.append(aima3.utils.expr("Lenguaje(Assembly)"))
    clausses.append(aima3.utils.expr("Lenguaje(Elixir)"))
    clausses.append(aima3.utils.expr("Lenguaje(Julia)"))
    clausses.append(aima3.utils.expr("Lenguaje(Racket)"))
    clausses.append(aima3.utils.expr("Lenguaje(Fortran)"))
    clausses.append(aima3.utils.expr("Lenguaje(JavaScript)"))
    clausses.append(aima3.utils.expr("Lenguaje(TypeScript)"))
    clausses.append(aima3.utils.expr("Lenguaje(Html)"))
    clausses.append(aima3.utils.expr("Lenguaje(Css)"))
    clausses.append(aima3.utils.expr("Lenguaje(Dart)"))
    clausses.append(aima3.utils.expr("Lenguaje(Mysql)"))
    clausses.append(aima3.utils.expr("Lenguaje(Mongodb)"))
    clausses.append(aima3.utils.expr("Lenguaje(Mariadb)"))
    clausses.append(aima3.utils.expr("Lenguaje(Sql)"))

    clausses.append(aima3.utils.expr("Framework(React)"))
    clausses.append(aima3.utils.expr("Framework(Angular)"))
    clausses.append(aima3.utils.expr("Framework(Django)"))
    clausses.append(aima3.utils.expr("Framework(Rubyonrails)"))
    clausses.append(aima3.utils.expr("Framework(Laravel)"))
    clausses.append(aima3.utils.expr("Framework(Spring)"))
    clausses.append(aima3.utils.expr("Framework(Flask)"))
    clausses.append(aima3.utils.expr("Framework(Symfony)"))
    clausses.append(aima3.utils.expr("Framework(Flutter)"))
    clausses.append(aima3.utils.expr("Framework(Meteor)"))
    clausses.append(aima3.utils.expr("Framework(Playframework)"))
    clausses.append(aima3.utils.expr("Framework(Cakephp)"))
    clausses.append(aima3.utils.expr("Framework(Codeigniter)"))
    clausses.append(aima3.utils.expr("Framework(Playframework)"))
    clausses.append(aima3.utils.expr("Framework(Angular)"))

    clausses.append(aima3.utils.expr("Utiliza(Angular,JavaScript)"))
    clausses.append(aima3.utils.expr("Utiliza(Angular,TypeScript)"))
    clausses.append(aima3.utils.expr("Utiliza(Cakephp,php)"))
    clausses.append(aima3.utils.expr("Utiliza(Codeigniter,php)"))
    clausses.append(aima3.utils.expr("Utiliza(Django,Python)"))
    clausses.append(aima3.utils.expr("Utiliza(Flask,Python)"))
    clausses.append(aima3.utils.expr("Utiliza(Flutter,Dart)"))
    clausses.append(aima3.utils.expr("Utiliza(Laravel,Php)"))
    clausses.append(aima3.utils.expr("Utiliza(Meteor,Javascript)"))
    clausses.append(aima3.utils.expr("Utiliza(Play_framework,Java)"))
    clausses.append(aima3.utils.expr("Utiliza(Play_framework,Scala)"))
    clausses.append(aima3.utils.expr("Utiliza(React,Javascript)"))
    clausses.append(aima3.utils.expr("Utiliza(Ruby_on_rails,Ruby)"))
    clausses.append(aima3.utils.expr("Utiliza(Spring,Java)"))
    clausses.append(aima3.utils.expr("Utiliza(Symfony,Php)"))

    clausses.append(aima3.utils.expr("LengOrientado(Python,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Java,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Ruby,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Swift,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Go,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Rust,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Php,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Haskell,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Perl,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Objective_c,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Kotlin,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Scala,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(R,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Lua,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Matlab,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Groovy,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Clojure,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Shell,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(MySQL,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Mongodb,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(mariadb,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Sql,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Assembly,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Elixir,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Julia,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Racket,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Fortran,Backend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Javascript,Frontend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Typescript,Frontend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Html,Frontend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Css,Frontend)"))
    clausses.append(aima3.utils.expr("LengOrientado(Dart,Frontend)"))

    clausses.append(aima3.utils.expr("Pais(Estados_unidos)"))
    clausses.append(aima3.utils.expr("Pais(Argentina)"))
    clausses.append(aima3.utils.expr("Pais(Brasil)"))
    clausses.append(aima3.utils.expr("Pais(Uruguay)"))
    clausses.append(aima3.utils.expr("Pais(Paraguay)"))
    clausses.append(aima3.utils.expr("Pais(Chile)"))
    clausses.append(aima3.utils.expr("Pais(Bolivia)"))
    clausses.append(aima3.utils.expr("Pais(México)"))
    clausses.append(aima3.utils.expr("Pais(Inglaterra)"))
    clausses.append(aima3.utils.expr("Pais(Francia)"))
    clausses.append(aima3.utils.expr("Pais(Alemania)"))

    clausses.append(aima3.utils.expr("Ciudad(Berlín)"))
    clausses.append(aima3.utils.expr("Ciudad(Múnich)"))
    clausses.append(aima3.utils.expr("Ciudad(Hamburgo)"))
    clausses.append(aima3.utils.expr("Ciudad(Fráncfort)"))
    clausses.append(aima3.utils.expr("Ciudad(Colonia)"))
    clausses.append(aima3.utils.expr("Ciudad(Buenos_Aires)"))
    clausses.append(aima3.utils.expr("Ciudad(Córdoba)"))
    clausses.append(aima3.utils.expr("Ciudad(Rosario)"))
    clausses.append(aima3.utils.expr("Ciudad(Mendoza)"))
    clausses.append(aima3.utils.expr("Ciudad(Mar_del_Plata)"))
    clausses.append(aima3.utils.expr("Ciudad(La_Paz)"))
    clausses.append(aima3.utils.expr("Ciudad(Santa_Cruz_de_la_Sierra)"))
    clausses.append(aima3.utils.expr("Ciudad(Cochabamba)"))
    clausses.append(aima3.utils.expr("Ciudad(Sucre)"))
    clausses.append(aima3.utils.expr("Ciudad(Potosí)"))
    clausses.append(aima3.utils.expr("Ciudad(São_Paulo)"))
    clausses.append(aima3.utils.expr("Ciudad(Río_de_Janeiro)"))
    clausses.append(aima3.utils.expr("Ciudad(Brasilia)"))
    clausses.append(aima3.utils.expr("Ciudad(Salvador)"))
    clausses.append(aima3.utils.expr("Ciudad(Belo_Horizonte)"))
    clausses.append(aima3.utils.expr("Ciudad(Santiago)"))
    clausses.append(aima3.utils.expr("Ciudad(Valparaíso)"))
    clausses.append(aima3.utils.expr("Ciudad(Viña_del_mar)"))
    clausses.append(aima3.utils.expr("Ciudad(Concepción)"))
    clausses.append(aima3.utils.expr("Ciudad(La_serena)"))
    clausses.append(aima3.utils.expr("Ciudad(Nueva_york)"))
    clausses.append(aima3.utils.expr("Ciudad(Los_angeles)"))
    clausses.append(aima3.utils.expr("Ciudad(Chicago)"))
    clausses.append(aima3.utils.expr("Ciudad(Miami)"))
    clausses.append(aima3.utils.expr("Ciudad(San_francisco)"))
    clausses.append(aima3.utils.expr("Ciudad(Paris)"))
    clausses.append(aima3.utils.expr("Ciudad(Marsella)"))
    clausses.append(aima3.utils.expr("Ciudad(Lyon)"))
    clausses.append(aima3.utils.expr("Ciudad(Toulouse)"))
    clausses.append(aima3.utils.expr("Ciudad(Niza)"))
    clausses.append(aima3.utils.expr("Ciudad(Londres)"))
    clausses.append(aima3.utils.expr("Ciudad(Manchester)"))
    clausses.append(aima3.utils.expr("Ciudad(Birmingham)"))
    clausses.append(aima3.utils.expr("Ciudad(Liverpool)"))
    clausses.append(aima3.utils.expr("Ciudad(Bristol)"))
    clausses.append(aima3.utils.expr("Ciudad(Ciudad_de_méxico)"))
    clausses.append(aima3.utils.expr("Ciudad(Cancún)"))
    clausses.append(aima3.utils.expr("Ciudad(Guadalajara)"))
    clausses.append(aima3.utils.expr("Ciudad(Monterrey)"))
    clausses.append(aima3.utils.expr("Ciudad(Tijuana)"))
    clausses.append(aima3.utils.expr("Ciudad(Asunción)"))
    clausses.append(aima3.utils.expr("Ciudad(Ciudad_del_este)"))
    clausses.append(aima3.utils.expr("Ciudad(Encarnación)"))
    clausses.append(aima3.utils.expr("Ciudad(Luque)"))
    clausses.append(aima3.utils.expr("Ciudad(San_Lorenzo)"))
    clausses.append(aima3.utils.expr("Ciudad(Montevideo)"))
    clausses.append(aima3.utils.expr("Ciudad(Punta_del_este)"))
    clausses.append(aima3.utils.expr("Ciudad(Colonia_del_Sacramento)"))
    clausses.append(aima3.utils.expr("Ciudad(Salto)"))
    clausses.append(aima3.utils.expr("Ciudad(Piriápolis)"))

    clausses.append(aima3.utils.expr("CiudadPais(Berlín,Alemania)"))
    clausses.append(aima3.utils.expr("CiudadPais(Múnich,Alemania)"))
    clausses.append(aima3.utils.expr("CiudadPais(Hamburgo,Alemania)"))
    clausses.append(aima3.utils.expr("CiudadPais(Fráncfort,Alemania)"))
    clausses.append(aima3.utils.expr("CiudadPais(Colonia,Alemania)"))
    clausses.append(aima3.utils.expr("CiudadPais(BuenosAires,Argentina)"))
    clausses.append(aima3.utils.expr("CiudadPais(Córdoba,Argentina)"))
    clausses.append(aima3.utils.expr("CiudadPais(Rosario,Argentina)"))
    clausses.append(aima3.utils.expr("CiudadPais(Mendoza,Argentina)"))
    clausses.append(aima3.utils.expr("CiudadPais(Mar_del_plata,Argentina)"))
    clausses.append(aima3.utils.expr("CiudadPais(La_Paz,Bolivia)"))
    clausses.append(aima3.utils.expr("CiudadPais(Santa_cruz_de_la_sierra,Bolivia)"))
    clausses.append(aima3.utils.expr("CiudadPais(Cochabamba,Bolivia)"))
    clausses.append(aima3.utils.expr("CiudadPais(Sucre,Bolivia)"))
    clausses.append(aima3.utils.expr("CiudadPais(Potosí,Bolivia)"))
    clausses.append(aima3.utils.expr("CiudadPais(São_Paulo,Brasil)"))
    clausses.append(aima3.utils.expr("CiudadPais(Río_de_janeiro,Brasil)"))
    clausses.append(aima3.utils.expr("CiudadPais(Brasilia,Brasil)"))
    clausses.append(aima3.utils.expr("CiudadPais(Salvador,Brasil)"))
    clausses.append(aima3.utils.expr("CiudadPais(Belo_horizonte,Brasil)"))
    clausses.append(aima3.utils.expr("CiudadPais(Santiago,Chile)"))
    clausses.append(aima3.utils.expr("CiudadPais(Valparaíso,Chile)"))
    clausses.append(aima3.utils.expr("CiudadPais(Viña_del_mar,Chile)"))
    clausses.append(aima3.utils.expr("CiudadPais(Concepción,Chile)"))
    clausses.append(aima3.utils.expr("CiudadPais(La_serena,Chile)"))
    clausses.append(aima3.utils.expr("CiudadPais(NuevaYork,Estados_unidos)"))
    clausses.append(aima3.utils.expr("CiudadPais(Los_angeles,Estados_unidos)"))
    clausses.append(aima3.utils.expr("CiudadPais(Chicago,Estados_unidos)"))
    clausses.append(aima3.utils.expr("CiudadPais(Miami,Estados_unidos)"))
    clausses.append(aima3.utils.expr("CiudadPais(San_francisco,Estados_unidos)"))
    clausses.append(aima3.utils.expr("CiudadPais(Paris,Francia)"))
    clausses.append(aima3.utils.expr("CiudadPais(Marsella,Francia)"))
    clausses.append(aima3.utils.expr("CiudadPais(Lyon,Francia)"))
    clausses.append(aima3.utils.expr("CiudadPais(Toulouse,Francia)"))
    clausses.append(aima3.utils.expr("CiudadPais(Niza,Francia)"))
    clausses.append(aima3.utils.expr("CiudadPais(Londres,Inglaterra)"))
    clausses.append(aima3.utils.expr("CiudadPais(Manchester,Inglaterra)"))
    clausses.append(aima3.utils.expr("CiudadPais(Birmingham,Inglaterra)"))
    clausses.append(aima3.utils.expr("CiudadPais(Liverpool,Inglaterra)"))
    clausses.append(aima3.utils.expr("CiudadPais(Bristol,Inglaterra)"))
    clausses.append(aima3.utils.expr("CiudadPais(Ciudad_de_méxico,Mexico)"))
    clausses.append(aima3.utils.expr("CiudadPais(Cancún,Mexico)"))
    clausses.append(aima3.utils.expr("CiudadPais(Guadalajara,Mexico)"))
    clausses.append(aima3.utils.expr("CiudadPais(Monterrey,Mexico)"))
    clausses.append(aima3.utils.expr("CiudadPais(Tijuana,Mexico)"))
    clausses.append(aima3.utils.expr("CiudadPais(Asunción,Paraguay)"))
    clausses.append(aima3.utils.expr("CiudadPais(Ciudad_del_este,Paraguay)"))
    clausses.append(aima3.utils.expr("CiudadPais(Encarnación,Paraguay)"))
    clausses.append(aima3.utils.expr("CiudadPais(Luque,Paraguay)"))
    clausses.append(aima3.utils.expr("CiudadPais(SanLorenzo,Paraguay)"))
    clausses.append(aima3.utils.expr("CiudadPais(Montevideo,Uruguay)"))
    clausses.append(aima3.utils.expr("CiudadPais(Punta_del_este,Uruguay)"))
    clausses.append(aima3.utils.expr("CiudadPais(Colonia_del_sacramento,Uruguay)"))
    clausses.append(aima3.utils.expr("CiudadPais(Salto,Uruguay)"))
    clausses.append(aima3.utils.expr("CiudadPais(Piriápolis,Uruguay)"))

    clausses.append(aima3.utils.expr("Experiencia(Senior)"))
    clausses.append(aima3.utils.expr("Experiencia(Semi_senior)"))
    clausses.append(aima3.utils.expr("Experiencia(Junior)"))
    clausses.append(aima3.utils.expr("Experiencia(Pasante)"))

    clausses.append(aima3.utils.expr("Idioma(Ingles)"))
    clausses.append(aima3.utils.expr("Idioma(Español)"))
    clausses.append(aima3.utils.expr("Idioma(Italiano)"))
    clausses.append(aima3.utils.expr("Idioma(Portugues)"))
    clausses.append(aima3.utils.expr("Idioma(Frances)"))
    clausses.append(aima3.utils.expr("Idioma(Alemán)"))

    clausses.append(aima3.utils.expr("Modalidad(Presencial)"))
    clausses.append(aima3.utils.expr("Modalidad(Remoto)"))
    clausses.append(aima3.utils.expr("Modalidad(Virtual)"))
    clausses.append(aima3.utils.expr("Modalidad(Mixto)"))

    clausses.append(aima3.utils.expr("Disponibilidad(Part-time)"))
    clausses.append(aima3.utils.expr("Disponibilidad(Full-time)"))
    clausses.append(aima3.utils.expr("Disponibilidad(Freelance)"))

    clausses.append(aima3.utils.expr("TrabajoenEquipo(Lider)"))
    clausses.append(aima3.utils.expr("TrabajoenEquipo(Referente)"))
    clausses.append(aima3.utils.expr("TrabajoenEquipo(Colaborador)"))

    clausses.append(aima3.utils.expr("CoordinacionEquipos(Colaborador)"))
    clausses.append(aima3.utils.expr("CoordinacionEquipos(Lider)"))

    clausses.append(aima3.utils.expr("Optimizaciones(Cpu)"))
    clausses.append(aima3.utils.expr("Optimizaciones(Memoria)"))
    clausses.append(aima3.utils.expr("Optimizaciones(Db)"))
    clausses.append(aima3.utils.expr("Optimizaciones(Navegador)"))

    clausses.append(aima3.utils.expr("OptimizaOrientacion(Cpu,Backend)"))
    clausses.append(aima3.utils.expr("OptimizaOrientacion(Memoria,Frontend)"))
    clausses.append(aima3.utils.expr("OptimizaOrientacion(Navegador,Frontend)"))
    clausses.append(aima3.utils.expr("OptimizaOrientacion(Db,Backend)"))
    clausses.append(aima3.utils.expr("OptimizaOrientacion(Cpu,Dba)"))

    clausses.append(aima3.utils.expr("Sueldo(Bajo)"))
    clausses.append(aima3.utils.expr("Sueldo(Medio)"))
    clausses.append(aima3.utils.expr("Sueldo(Alto)"))

    clausses.append(aima3.utils.expr("Arquitectura(Cloud)"))
    clausses.append(aima3.utils.expr("Arquitectura(Onpremise)"))

    clausses.append(aima3.utils.expr("Metas(Si)"))
    clausses.append(aima3.utils.expr("Metas(No)"))

    # Clausses de nombre de usuario
    clausses.append(aima3.utils.expr("Usuario(x)"))
    clausses.append(aima3.utils.expr("Pais(y) & Usuario(x) ==> EsDe(x,y)"))
    clausses.append(aima3.utils.expr("Ciudad(y) & Usuario(x) ==> EsDe(x,y)"))

    return clausses


def presentationClausses():
    clausses = list()
    clausses.append("Usuario")
    clausses.append("Pais")
    clausses.append("Ciudad")
    clausses.append("EsDe")
    return clausses


def locationClausses():
    clausses = list()
    clausses.append("Pais")
    clausses.append("Ciudad")
    clausses.append("EsDe")
    return clausses

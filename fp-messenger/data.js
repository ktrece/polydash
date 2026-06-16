// Datos de Formación Profesional en Castilla y León.
// Información de carácter orientativo basada en las familias profesionales
// de FP del sistema educativo (Educacyl / Junta de Castilla y León).
// Cada "casa" del planeta representa una familia/ciclo de FP.

export const FP_BUILDINGS = [
  {
    id: "sanidad",
    type: "hospital",
    nombre: "Hospital · Sanidad",
    familia: "Familia Profesional: Sanidad",
    color: "#e7eef5",
    icono: "🏥",
    niveles: ["Grado Medio", "Grado Superior"],
    ciclos: [
      "GM Cuidados Auxiliares de Enfermería",
      "GM Emergencias Sanitarias",
      "GS Higiene Bucodental",
      "GS Laboratorio Clínico y Biomédico",
      "GS Imagen para el Diagnóstico y Medicina Nuclear",
    ],
    duracion: "2.000 horas (2 cursos), incluye FCT en centros sanitarios",
    salidas:
      "Hospitales, centros de salud, laboratorios, clínicas dentales, servicios de emergencias (112/061).",
    descripcion:
      "Forma profesionales para la atención sanitaria y el apoyo al diagnóstico. En Castilla y León se imparte en numerosos IES y centros integrados, con prácticas en la red de hospitales de SACYL.",
  },
  {
    id: "automocion",
    type: "taller",
    nombre: "Taller · Transporte y Vehículos",
    familia: "Familia Profesional: Transporte y Mantenimiento de Vehículos",
    color: "#cfd6dd",
    icono: "🔧",
    niveles: ["Grado Básico", "Grado Medio", "Grado Superior"],
    ciclos: [
      "GB Mantenimiento de Vehículos",
      "GM Electromecánica de Vehículos Automóviles",
      "GM Carrocería",
      "GS Automoción",
    ],
    duracion: "2.000 horas (2 cursos), con prácticas en talleres y concesionarios",
    salidas:
      "Talleres de reparación, concesionarios, flotas de transporte, peritación y diagnosis.",
    descripcion:
      "Capacita para el mantenimiento, diagnosis y reparación de vehículos. Muy demandada en el tejido industrial y de automoción de Castilla y León.",
  },
  {
    id: "informatica",
    type: "tech",
    nombre: "Centro TIC · Informática",
    familia: "Familia Profesional: Informática y Comunicaciones",
    color: "#dfe9ff",
    icono: "💻",
    niveles: ["Grado Medio", "Grado Superior"],
    ciclos: [
      "GM Sistemas Microinformáticos y Redes (SMR)",
      "GS Desarrollo de Aplicaciones Web (DAW)",
      "GS Desarrollo de Aplicaciones Multiplataforma (DAM)",
      "GS Administración de Sistemas Informáticos en Red (ASIR)",
    ],
    duracion: "2.000 horas (2 cursos); ofertas presencial, dual y a distancia",
    salidas:
      "Desarrollo de software, administración de sistemas y redes, soporte técnico, ciberseguridad.",
    descripcion:
      "Una de las familias con mayor empleabilidad. En Castilla y León hay amplia oferta, incluida FP a distancia y proyectos de FP Dual con empresas tecnológicas.",
  },
  {
    id: "hosteleria",
    type: "restaurante",
    nombre: "Restaurante · Hostelería",
    familia: "Familia Profesional: Hostelería y Turismo",
    color: "#ffe3c2",
    icono: "🍽️",
    niveles: ["Grado Básico", "Grado Medio", "Grado Superior"],
    ciclos: [
      "GB Cocina y Restauración",
      "GM Cocina y Gastronomía",
      "GM Servicios en Restauración",
      "GS Dirección de Cocina",
      "GS Gestión de Alojamientos Turísticos",
    ],
    duracion: "2.000 horas (2 cursos), con prácticas en hoteles y restaurantes",
    salidas:
      "Cocina, sala, gestión de alojamientos, agencias y empresas de turismo rural.",
    descripcion:
      "Clave para el turismo y la gastronomía de Castilla y León (enoturismo, turismo rural y patrimonio). Forma desde cocineros hasta gestores de alojamientos.",
  },
  {
    id: "agraria",
    type: "granja",
    nombre: "Granja · Agraria",
    familia: "Familia Profesional: Agraria",
    color: "#d7f0c2",
    icono: "🌾",
    niveles: ["Grado Básico", "Grado Medio", "Grado Superior"],
    ciclos: [
      "GM Producción Agropecuaria",
      "GM Aprovechamiento y Conservación del Medio Natural",
      "GS Ganadería y Asistencia en Sanidad Animal",
      "GS Gestión Forestal y del Medio Natural",
    ],
    duracion: "2.000 horas (2 cursos), con prácticas en explotaciones agrarias",
    salidas:
      "Explotaciones agrícolas y ganaderas, gestión forestal, cooperativas, medio ambiente.",
    descripcion:
      "Fundamental en una comunidad eminentemente agraria y forestal. Conecta con el sector agroalimentario y el reto demográfico del medio rural.",
  },
  {
    id: "electricidad",
    type: "electrica",
    nombre: "Subestación · Electricidad",
    familia: "Familia Profesional: Electricidad y Electrónica",
    color: "#fff3b0",
    icono: "⚡",
    niveles: ["Grado Básico", "Grado Medio", "Grado Superior"],
    ciclos: [
      "GB Electricidad y Electrónica",
      "GM Instalaciones Eléctricas y Automáticas",
      "GS Sistemas Electrotécnicos y Automatizados",
      "GS Automatización y Robótica Industrial",
    ],
    duracion: "2.000 horas (2 cursos), con prácticas en empresas del sector",
    salidas:
      "Instalaciones eléctricas, automatización industrial, energías renovables, mantenimiento.",
    descripcion:
      "Vinculada a la industria, las renovables y la automatización. Alta inserción laboral y presencia en proyectos de FP Dual en Castilla y León.",
  },
];

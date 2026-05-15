# Syntropyc Quantum Solutions — Sitio Web

Sitio web oficial de **Syntropyc Quantum Solutions (SQS)**, firma de Tecnología Profunda (Deep Tech) con sede en Cartagena, Colombia.

## Estructura del Proyecto

```
SQS/
├── index.html          # Página principal (single-page)
├── README.md           # Este archivo
├── .gitignore          # Archivos excluidos del repositorio
└── assets/
    └── img/            # Imágenes del sitio
        ├── logo.jpeg               ← Logo principal de Syntropyc
        ├── hero_deep_tech.png      ← Imagen hero (sección principal)
        ├── molecular_sim.png       ← Imagen Servicio 1 (Simulación Molecular)
        ├── saas_ecosystem.png      ← Imagen Servicio 2 (SaaS Corporativos)
        └── ai_brain.png            ← Imagen Servicio 3 (Inteligencia Artificial)
```

## Imágenes requeridas

Sube las siguientes imágenes directamente a la carpeta `assets/img/` desde GitHub:

| Archivo | Uso en la página |
|---|---|
| `logo.jpeg` | Logo en navbar y footer |
| `hero_deep_tech.png` | Hero section (columna derecha) |
| `molecular_sim.png` | Tarjeta Servicio 1 |
| `saas_ecosystem.png` | Tarjeta Servicio 2 |
| `ai_brain.png` | Tarjeta Servicio 3 |

## Cómo subir las imágenes

1. Ir a `assets/img/` en el repositorio
2. Clic en **Add file → Upload files**
3. Arrastrar las imágenes con los nombres exactos indicados arriba
4. Commit directamente a `main`

## Despliegue

Este es un sitio estático listo para publicarse en:
- **GitHub Pages** (gratuito): `Settings → Pages → Branch: main → / (root)`
- **Netlify** (gratuito): Conectar el repo y hacer deploy automático
- **Vercel** (gratuito): Conectar el repo y hacer deploy automático

## Tecnologías

- HTML5 + CSS3 (sin frameworks de build)
- [Tailwind CSS](https://tailwindcss.com/) via CDN
- [AOS](https://michalsnik.github.io/aos/) — animaciones de scroll
- [tsParticles](https://particles.js.org/) — fondo de partículas
- [Vanilla Tilt](https://micku7zu.github.io/vanilla-tilt.js/) — efecto 3D en tarjetas
- [Lucide Icons](https://lucide.dev/) — íconos

---

© 2026 Syntropyc S.A.S. — Cartagena, Colombia

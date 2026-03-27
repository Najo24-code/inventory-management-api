# inventory-management-api

![CI](https://github.com/Najo24-code/inventory-management-api/workflows/CI/badge.svg)


API REST de gestión de inventario con JWT, CRUD de productos, categorías y movimientos de stock

![Python](https://img.shields.io/badge/-Python-blue) ![FastAPI](https://img.shields.io/badge/-FastAPI-blue) ![SQLite](https://img.shields.io/badge/-SQLite-blue)

## 🚀 Features

- API REST completa
- Autenticación JWT
- Base de datos SQLite

## 📦 Instalación
```bash
git clone https://github.com/Najo24-code/inventory-management-api.git
cd inventory-management-api
pip install -r requirements.txt
```

## 🔧 Uso
```bash
uvicorn main:app --reload
```

API disponible en: `http://localhost:8000/docs`

## 📁 Estructura
```
inventory-management-api/
├── main.py          # Entry point
├── models.py        # Modelos de datos
├── database.py      # Conexión DB
├── auth.py          # Autenticación
└── requirements.txt
```

## 📝 License

MIT © 2026 Najo24-code

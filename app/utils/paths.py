from pathlib import Path


# Diretório raiz do projeto
ROOT_DIR = Path(__file__).resolve().parents[2]


# App
APP_DIR = ROOT_DIR / "app"


# Assets
ASSETS_DIR = APP_DIR / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
ICONS_DIR = ASSETS_DIR / "icons"
FONTS_DIR = ASSETS_DIR / "fonts"
THEMES_DIR = ASSETS_DIR / "themes"


# Config
CONFIG_DIR = APP_DIR / "config"


# Database
DATABASE_DIR = ROOT_DIR / "data"
DATABASE_FILE = DATABASE_DIR / "database.db"


# Logs
LOGS_DIR = ROOT_DIR / "logs"
APP_LOG_FILE = LOGS_DIR / "app.log"
ERROR_LOG_FILE = LOGS_DIR / "errors.log"


# Session
SESSION_FILE = DATABASE_DIR / "session.json"


# Docs
DOCS_DIR = ROOT_DIR / "docs"


# Tests
TESTS_DIR = ROOT_DIR / "tests"


LOGIN_BANNER = IMAGES_DIR / "logo_banner.png"
APP_ICON = ICONS_DIR / "logo.ico"

SETTINGS_ICON = ICONS_DIR / "settings.png"


USER_ICON = ICONS_DIR / "user.png"

LOCK_ICON = ICONS_DIR / "lock.png"

EYE_OPEN_ICON = ICONS_DIR / "eye_open.png"
EYE_CLOSED_ICON = ICONS_DIR / "eye_closed.png"

EMAIL_ICON = ICONS_DIR / "email.png"

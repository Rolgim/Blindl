import logging
import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine, pool

logger = logging.getLogger("app.alembic")

# PATH FIX 
sys.path.insert(0, os.getcwd())

# Alembic config
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# IMPORT MODELS
from src.db.base import Base
import src.db.models  

# Metadata target
target_metadata = Base.metadata

# Debug 
logger.debug("CWD: %s", os.getcwd())
logger.debug("DATABASE_URL is set: %s", bool(os.getenv("DATABASE_URL")))
logger.info("Detected tables: %s", list(Base.metadata.tables.keys()))

POSTGIS_TABLES = {
    "spatial_ref_sys",
    "place_lookup",
    "faces",
    "edges",
    "zcta5",
    "loader_variables",
    "street_type_lookup",
    "countysub_lookup",
    "addrfeat",
    "addr",
    "featnames",
    "county_lookup",
    "direction_lookup",
    "state",
    "place",
    "topology",
    "cousub",
    "pagc_lex",
    "tract",
    "bg",
    "zip_lookup",
    "geocode_settings_default",
    "geocode_settings",
    "tabblock20",
    "zip_state_loc",
    "zip_lookup_base",
    "county",
    "secondary_unit_lookup",
    "tabblock",
    "state_lookup",
    "layer",
    "pagc_gaz",
    "loader_lookuptables",
    "pagc_rules",
    "zip_state",
    "loader_platform",
    "zip_lookup_all",
}

def include_object(obj, name, type_, reflected, compare_to):
    if type_ == "table" and name in POSTGIS_TABLES:
        return False
    return True


# OFFLINE MODE 
def run_migrations_offline() -> None:
    url = os.getenv("DATABASE_URL")

    if not url:
        logger.error("DATABASE_URL is not set")
        raise RuntimeError("DATABASE_URL is not set")

    logger.info("Running migrations in OFFLINE mode")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


# ONLINE MODE
def run_migrations_online() -> None:
    url = os.getenv("DATABASE_URL")

    if not url:
        logger.error("DATABASE_URL is not set")
        raise RuntimeError("DATABASE_URL is not set")

    logger.info("Running migrations in ONLINE mode")

    engine = create_engine(url, poolclass=pool.NullPool)

    with engine.connect() as connection:
        logger.debug("Database connection established")

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

# ENTRYPOINT
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

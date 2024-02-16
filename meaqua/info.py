import logging
import platform

import django
from django.conf import settings

logger = logging.getLogger(__name__)


def log_settings():
    """Log info about the current Django and Python environment."""
    logger.info(f"------------------------------------")
    logger.info(f"Runtime log for meaqua server (DEBUG={settings.DEBUG})")
    logger.info(f"Running meaqua on Django {django.get_version()} using Python {platform.python_version()}")
    logger.info(f"Environment : {platform.system()} {platform.release()} ({platform.version()})")
    logger.info(f"OS : {platform.platform()}")
    logger.info(f"------------------------------------")

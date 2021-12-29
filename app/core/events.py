from typing import Callable

from redis_om import Migrator

def create_start_app_handler() -> Callable:
    async def start_app() -> None:
        Migrator().run()
    return start_app

class SharedMemory:
    def __init__(self) -> None:
        self._store: dict[str, str] = {}

    def put(self, key: str, value: str) -> None:
        self._store[key] = value

    def get(self, key: str, default: str = "") -> str:
        return self._store.get(key, default)

from a_synthetic_data.memory import SharedMemory

def test_memory_roundtrip() -> None:
    m = SharedMemory()
    m.put("k", "v")
    assert m.get("k") == "v"

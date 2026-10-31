from agent.autopilot import AutoPilot


def test_success_rate_counts_csv_boolean_strings_case_insensitively() -> None:
    autopilot = AutoPilot()
    row = {"id": "memory-1"}
    history = [
        {"memory_id": "memory-1", "success": "True"},
        {"memory_id": "memory-1", "success": "False"},
        {"memory_id": "memory-2", "success": "True"},
    ]

    assert autopilot._calculate_success_rate(row, history) == 0.5


def test_success_rate_accepts_boolean_values_and_ignores_other_memory_ids() -> None:
    autopilot = AutoPilot()
    row = {"id": "memory-1"}
    history = [
        {"memory_id": "memory-1", "success": True},
        {"memory_id": "memory-1", "success": False},
        {"memory_id": "memory-2", "success": True},
    ]

    assert autopilot._calculate_success_rate(row, history) == 0.5


def test_success_rate_is_zero_when_no_history_matches_memory() -> None:
    autopilot = AutoPilot()
    row = {"id": "memory-1"}
    history = [{"memory_id": "memory-2", "success": "True"}]

    assert autopilot._calculate_success_rate(row, history) == 0.0

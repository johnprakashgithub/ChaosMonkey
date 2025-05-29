import pytest
from chaos_monkey import ChaosMonkey

@pytest.fixture
def chaos_monkey(request):
    source = request.param['source']
    destination = request.param['destination']
    port = request.param['port']
    protocol = request.param['protocol']
    return ChaosMonkey(source, destination, port, protocol)

@pytest.mark.parametrize("chaos_monkey", [
    {"source": "ANY", "destination": "NTP Server", "port": 123, "protocol": "NTP"},
    # Add more test cases here
], indirect=True)
def test_disable_communication(chaos_monkey):
    chaos_monkey.disable_communication()
    assert not chaos_monkey.verify_communication(), "Communication should be disabled"

@pytest.mark.parametrize("chaos_monkey", [
    {"source": "ANY", "destination": "NTP Server", "port": 123, "protocol": "NTP"},
    # Add more test cases here
], indirect=True)
def test_enable_communication(chaos_monkey):
    chaos_monkey.enable_communication()
    assert chaos_monkey.verify_communication(), "Communication should be enabled"

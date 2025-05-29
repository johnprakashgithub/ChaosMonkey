import subprocess

class ChaosMonkey:
    def __init__(self, source, destination, port, protocol):
        self.source = source
        self.destination = destination
        self.port = port
        self.protocol = protocol

    def disable_communication(self):
        command = f"sudo iptables -A INPUT -s {self.source} -d {self.destination} -p {self.protocol} --dport {self.port} -j DROP"
        subprocess.run(command, shell=True)

    def enable_communication(self):
        command = f"sudo iptables -D INPUT -s {self.source} -d {self.destination} -p {self.protocol} --dport {self.port} -j DROP"
        subprocess.run(command, shell=True)

    def verify_communication(self):
        # Implement your logic to verify communication here
        # Return True if communication is successful, False otherwise
        pass

# Receiver
class Engine:
    def start(self):
        print("Silnik uruchomiony")
    
    def stop(self):
        print("Silnik zatrzymany")

# Invoker
class ControlPanel:
    def __init__(self):
        self._commands = {}

    def register(self, name, command):
        self._commands[name] = command

    def execute(self, name):
        if name in self._commands:
            self._commands[name]()


engine = Engine()
panel = ControlPanel()
panel.register("start_engine", engine.start)
panel.register("stop_engine", engine.stop)

panel.execute("stop_engine")
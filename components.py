import os
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

class Component:
    """Base class for dashboard components"""
    def __init__(self, name):
        self.name = name

    def render(self):
        """Render the component"""
        console.print(Panel(self.name, title="Component"))

class SystemStatus(Component):
    """System status component"""
    def __init__(self):
        super().__init__("System Status")

    def render(self):
        """Render the system status component"""
        console.print(Panel("System is online", title="System Status"))

class UserInput(Component):
    """User input component"""
    def __init__(self):
        super().__init__("User Input")

    def render(self):
        """Render the user input component"""
        console.print(Panel("Enter a command: ", title="User Input"))

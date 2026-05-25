class WidgetManager:
    def __init__(self):
        self.widgets = []

    def add_widget(self, widget):
        self.widgets.append(widget)

    def update_widgets(self):
        for widget in self.widgets:
            widget.update()

widget_manager = WidgetManager()

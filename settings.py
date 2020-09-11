import json

class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (75, 75, 75)

    def load_settings(self):

        with open('src/settings.json') as fs:
            file_content = fs.read()
            templates = json.loads(file_content)

        print(templates)

        for section, commands in templates.items():
            print(section)
            print(commands)


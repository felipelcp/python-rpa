"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the Hashtag treinamento website.
        self.browse("https://www.hashtagtreinamentos.com")

        #Procura a aba "Curso de Python"
        if not self.find( "CursoPython", matching=0.97, waiting_time=10000):
            self.not_found("CursoPython")
        self.click()

        #Procura um elemento para confirmar que a página carregou
        if not self.find( "PaginaCarregou", matching=0.97, waiting_time=10000):
            self.not_found("PaginaCarregou")

        #Aperta Page Down
        self.page_down(1000)

        self.page_down(1000)

        #Clica no campo Nome
        if not self.find( "CampoNome", matching=0.97, waiting_time=10000):
            self.not_found("CampoNome")
        self.click()

        #Digita o Nome
        self.paste("Nome")

        #Clica no campo Email
        if not self.find( "CampoEmail", matching=0.97, waiting_time=10000):
            self.not_found("CampoEmail")
        self.click()

        #Digita email
        self.paste("email@email.com")

        #Clica no campo WhatsApp
        if not self.find( "CampoWhatsApp", matching=0.97, waiting_time=10000):
            self.not_found("CampoWhatsApp")
        self.click()

        #Digita o número de Celular
        self.paste("41999999999")
        #Clica em Enviar
        if not self.find( "Enviar", matching=0.97, waiting_time=10000):
            self.not_found("Enviar")
        self.click()
             

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()



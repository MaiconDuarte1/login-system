from app.core.app import LoginSystem
from app.utils.logger import Logger



try:
    
    app = LoginSystem()

    app.mainloop()

except Exception as error:
    
    Logger.error(str(error))

    raise
import logging
import pyrogram
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "Bot",
        bot_token="5016166355:AAEKxdlkF7ofJNW_bHKZRxl1iRHZlaR519A",
        api_id=2171111,
        api_hash="fd7acd07303760c52dcc0ed8b2f73086",
        plugins=plugins
    )
    app.run()

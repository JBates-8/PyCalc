"""
File: main.py
Author: Jackson Bates
Created: 5/14/2019 3:20 PM 
"""
if __name__ == '__main__':
    import sys
    import logging
    mode = sys.argv[1]
    format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename="main.log", filemode='w', level=logging.DEBUG, format=format)
    logger = logging.getLogger('')
    output_stream = logging.StreamHandler(sys.stdout)
    output_stream.setLevel(level=logging.INFO)
    logger.addHandler(output_stream)

    if mode == 'CLI':   #CLI
        logger.info("Mode selected ({})".format(mode))
        from Console import Console
        console = Console()
        console.run()

    elif mode == 'GUI': #GUI
        logger.info("Mode selected ({})".format(mode))
        from PyQt5.QtWidgets import QApplication, QMainWindow
        from ui.mainWindow import Ui_MainWindow


        app = QApplication(sys.argv)
        logger.info("QApp initialized...")
        MainWindow = QMainWindow()
        logger.info("QMainWindow Initialized")
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        logger.info("ui setup with MainWindow as parent...")
        MainWindow.show()
        logger.info("MainWindow shown...")
        sys.exit(app.exec_())

    elif mode == 'TEST': #Debug mode in CLI
        output_stream.setLevel(logging.DEBUG)
        logger.info("Mode selected ({})".format(mode))

        from Console import Console
        console = Console()
        console.test_run()
    else:
        logger.error("Incorrect main parameter: {}".format(mode))

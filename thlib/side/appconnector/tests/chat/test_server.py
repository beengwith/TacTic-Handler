import sys
import os

module_location = os.path.abspath(__file__).replace("\\", "/").rsplit("/", 4)[0]
sys.path.append(module_location)


def test(start=False):

    from appconnector.server import Server, logger
    logger.setLevel(10)

    server = Server("127.0.0.1", 55300)

    from thlib.side.Qt import QtWidgets, QtCore, QtGui
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("server")
    layout = QtWidgets.QVBoxLayout()
    window.setLayout(layout)

    plain_text = QtWidgets.QPlainTextEdit()
    plain_text.setMinimumHeight(180)
    plain_text.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
    layout.addWidget(plain_text)

    text = QtWidgets.QLineEdit()
    text.setPlaceholderText("Insert message and press enter")
    layout.addWidget(text)

    def test_send():

        data = text.text()
        text.clear()
        server.broadcast(data.encode("utf-8"))

        plain_text.moveCursor(QtGui.QTextCursor.End)
        plain_text.appendHtml("<font color=\"red\">" + str(data) + "</font>")

    def test_receive(*args):

        plain_text.moveCursor(QtGui.QTextCursor.End)

        con = args[0]
        con.send("system:hello, it`s me".encode("utf-8"))

        datab = bytes(args[1])
        datas = datab.decode("utf-8")
        if datas.startswith("system:"):
            plain_text.appendHtml("<font color=\"gray\">" + str(datas) + "</font>")
        else:
            plain_text.appendHtml("<font color=\"black\">" + str(datas) + "</font>")

            for key in server:
                if key == con.key:
                    continue

                server[key].send(datab)

    server.received.connect(test_receive)

    text.returnPressed.connect(test_send)

    sbutton = QtWidgets.QPushButton("START")
    layout.addWidget(sbutton)

    ebutton = QtWidgets.QPushButton("STOP")
    layout.addWidget(ebutton)

    def test_finished():

        ebutton.setVisible(False)
        sbutton.setVisible(True)

    def test_started():

        ebutton.setVisible(True)
        sbutton.setVisible(False)

    server.started.connect(test_started)
    server.finished.connect(test_finished)

    def test_stop():

        server.stop()

    def test_start():

        server.start()

    sbutton.released.connect(test_start)
    ebutton.released.connect(test_stop)

    window.show()

    if start:
        test_start()

    sys.exit(app.exec_())


if __name__ == "__main__":
    test()
from PyQt5 import QtGui, QtWidgets
import sys
import design
#import re
import os
import shutil
def change_setting(set_name, TF):
    afile ="prefs.js"
    shutil.copy( afile, afile+"~" )
    destination= open( afile, "w" )
    source= open( afile+"~", "r" )
    for line in source:
        
        if set_name in line:
            
            destination.write("user_pref(\""+set_name+"\", "+TF+");\n")
        else:
            destination.write( line )
    source.close()
    destination.close()
    os.remove(afile+"~")
    

class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ischeckboxchecked)
        
    def ischeckboxchecked(self):
        settings = {}
        #if self.content_blocking.isChecked():
        #    settings.update({self.content_blocking:( "", True)})
        if self.do_not_track.isChecked():
            settings.update({self.do_not_track:[("privacy.trackingprotection.enabled", "true")]})
        if self.cookies_and_site_data.isChecked():
            settings.update({self.cookies_and_site_data:[("network.cookie.cookieBehavior", "1"),
                                                         ("network.cookie.lifetimePolicy", "2")]})
        #print(settings)
        
        
        for i in settings.values():
            for j in i:
                a=j[0]
                b=j[1]

                change_setting(a,b)
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
    


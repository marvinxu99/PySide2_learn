# https://doc.qt.io/qtforpython/tutorials/datavisualize/add_tableview.html
# Usually, a QWidget is used to display data in most data-driven applications. 
# Use a table view to display your data.

'''
You could also use the default item model that comes with a QTableWidget instead. 
QTableWidget is a convenience class that reduces your codebase considerably as you 
don’t need to implement a data model. However, it’s less flexible than a QTableView, 
as QTableWidget cannot be used with just any data. For more insight about Qt’s model-view 
framework, refer to the Model View Programming <http://doc.qt.io/qt-5/model-view-programming.html> documentation
'''

import sys
import argparse
import pandas as pd

from PySide2.QtCore import QDateTime, QTimeZone
from PySide2.QtWidgets import QApplication

from main_window import MainWindow
from main_widget import Widget


def transform_date(utc, timezone=None):
    utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
    new_date = QDateTime().fromString(utc, utc_fmt)
    if timezone:
        new_date.setTimeZone(timezone)
    return new_date


def read_data(fname):
    # Read the CSV content
    df = pd.read_csv(fname)

    # Remove wrong magnitudes
    df = df.drop(df[df.mag < 0].index)
    magnitudes = df["mag"]

    # My local timezone
    # timezone = QTimeZone(b"Europe/Berlin")   
    timezone = QTimeZone(b"America/Vancouver")   

    # Get timestamp transformed to our timezone
    times = df["time"].apply(lambda x: transform_date(x, timezone))

    return times, magnitudes


if __name__ == "__main__":
    options = argparse.ArgumentParser(description="A tool to visualize data contained in a CSV  file.")
    options.add_argument("-f", "--file", type=str, required=True, 
                        help='CSV file to be processed' )
    args = options.parse_args()
    data = read_data(args.file)

    # Qt Application
    app = QApplication(sys.argv)

    widget = Widget(data)
    window = MainWindow(widget)
    window.show()
    sys.exit(app.exec_())

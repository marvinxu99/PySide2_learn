import QtQuick 2.0


Rectangle {
    width: 200
    height: 200
    color: "green"

   /* 
    Text {
        text: "Hello World"
        anchors.centerIn: parent
    }
*/
    Row {
        Button {
            text: "Ok"
            onClicked: model.submit()
        }
        Button {
            text: "Cancel"
            onClicked: model.revert()
        }
    }

}
/*

RowLayout {
    Button {
        text: "Ok"
        onClicked: model.submit()
    }
    Button {
        text: "Cancel"
        onClicked: model.revert()
    }
}
*/



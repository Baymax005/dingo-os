/**
 * Dingo OS SDDM Theme
 * Custom login screen for Dingo OS - Arch Edition
 * 
 * Based on breeze with custom branding
 */

import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls 2.15
import org.kde.plasma.core 2.0 as PlasmaCore
import org.kde.plasma.components 3.0 as PlasmaComponents
import org.kde.plasma.extras 2.0 as PlasmaExtras
import "components"

Image {
    id: root
    
    property int sessionIndex
    property string sessionName: ""
    
    source: "background.jpg"
    fillMode: Image.PreserveAspectCrop
    
    // Blur effect on background
    layer.enabled: true
    layer.effect: FastBlur {
        radius: 50
    }
    
    // Dark overlay
    Rectangle {
        anchors.fill: parent
        color: "#000000"
        opacity: 0.4
    }
    
    // Dingo Logo
    Image {
        id: logo
        source: "dingo-logo.png"
        width: 200
        height: 200
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 80
        fillMode: Image.PreserveAspectFit
    }
    
    // OS Name
    Text {
        id: osName
        text: "Dingo OS"
        font.family: "Noto Sans"
        font.pixelSize: 48
        font.weight: Font.Light
        color: "#ffffff"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: logo.bottom
        anchors.topMargin: 20
    }
    
    Text {
        id: osTagline
        text: "Arch Edition • KDE Plasma 6"
        font.family: "Noto Sans"
        font.pixelSize: 16
        color: "#cccccc"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: osName.bottom
        anchors.topMargin: 8
    }
    
    // Login box
    Rectangle {
        id: loginBox
        width: 400
        height: 300
        anchors.centerIn: parent
        color: "#1a1a1a"
        radius: 16
        opacity: 0.95
        
        border.color: "#333333"
        border.width: 1
        
        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 30
            spacing: 16
            
            // Username field
            PlasmaComponents.TextField {
                id: usernameField
                Layout.fillWidth: true
                Layout.preferredHeight: 48
                placeholderText: "Username"
                font.pixelSize: 16
                
                background: Rectangle {
                    color: "#2a2a2a"
                    radius: 8
                    border.color: usernameField.focus ? "#0078d4" : "#404040"
                    border.width: 2
                }
            }
            
            // Password field
            PlasmaComponents.TextField {
                id: passwordField
                Layout.fillWidth: true
                Layout.preferredHeight: 48
                placeholderText: "Password"
                font.pixelSize: 16
                echoMode: TextInput.Password
                
                background: Rectangle {
                    color: "#2a2a2a"
                    radius: 8
                    border.color: passwordField.focus ? "#0078d4" : "#404040"
                    border.width: 2
                }
                
                Keys.onEnterPressed: loginButton.clicked()
                Keys.onReturnPressed: loginButton.clicked()
            }
            
            // Login button
            PlasmaComponents.Button {
                id: loginButton
                Layout.fillWidth: true
                Layout.preferredHeight: 48
                text: "Log In"
                font.pixelSize: 16
                
                background: Rectangle {
                    color: parent.pressed ? "#0056a3" : (parent.hovered ? "#1a86d9" : "#0078d4")
                    radius: 8
                }
                
                contentItem: Text {
                    text: parent.text
                    color: "#ffffff"
                    font.pixelSize: 16
                    font.weight: Font.Medium
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
                
                onClicked: {
                    sddm.login(usernameField.text, passwordField.text, sessionIndex)
                }
            }
            
            // Session selector
            RowLayout {
                Layout.fillWidth: true
                
                PlasmaComponents.Label {
                    text: "Session:"
                    color: "#888888"
                }
                
                PlasmaComponents.ComboBox {
                    id: sessionSelector
                    Layout.fillWidth: true
                    model: sessionModel
                    currentIndex: 0
                    
                    onCurrentIndexChanged: {
                        sessionIndex = currentIndex
                        sessionName = sessionModel.data(sessionModel.index(currentIndex, 0), Qt.DisplayRole)
                    }
                }
            }
        }
    }
    
    // Bottom bar with power controls
    Row {
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottomMargin: 40
        spacing: 20
        
        PlasmaComponents.Button {
            text: "⏻ Shutdown"
            font.pixelSize: 14
            
            background: Rectangle {
                color: parent.hovered ? "#333333" : "transparent"
                radius: 8
            }
            
            contentItem: Text {
                text: parent.text
                color: "#ffffff"
                font.pixelSize: 14
            }
            
            onClicked: sddm.powerOff()
        }
        
        PlasmaComponents.Button {
            text: "↻ Restart"
            font.pixelSize: 14
            
            background: Rectangle {
                color: parent.hovered ? "#333333" : "transparent"
                radius: 8
            }
            
            contentItem: Text {
                text: parent.text
                color: "#ffffff"
                font.pixelSize: 14
            }
            
            onClicked: sddm.reboot()
        }
        
        PlasmaComponents.Button {
            text: "⏾ Sleep"
            font.pixelSize: 14
            
            background: Rectangle {
                color: parent.hovered ? "#333333" : "transparent"
                radius: 8
            }
            
            contentItem: Text {
                text: parent.text
                color: "#ffffff"
                font.pixelSize: 14
            }
            
            onClicked: sddm.suspend()
        }
    }
    
    // Clock
    Text {
        id: clock
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        anchors.margins: 40
        font.family: "Noto Sans"
        font.pixelSize: 36
        font.weight: Font.Light
        color: "#ffffff"
        text: Qt.formatDateTime(new Date(), "hh:mm")
        
        Timer {
            interval: 1000
            running: true
            repeat: true
            onTriggered: parent.text = Qt.formatDateTime(new Date(), "hh:mm")
        }
    }
    
    // Date
    Text {
        anchors.bottom: clock.top
        anchors.right: parent.right
        anchors.margins: 40
        anchors.bottomMargin: 5
        font.family: "Noto Sans"
        font.pixelSize: 16
        color: "#cccccc"
        text: Qt.formatDateTime(new Date(), "dddd, MMMM d")
    }
    
    Component.onCompleted: {
        usernameField.focus = true
    }
}

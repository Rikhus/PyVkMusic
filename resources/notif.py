import plyer
def sendNotification(message,appName,title,appIcon=""):
    if(appIcon!=""):
        try:
            plyer.notification.notify(message=message,app_name=appName,app_icon=appIcon,title=title)
        except:
            plyer.notification.notify(message=message,app_name=appName,title=title)
    else:
        plyer.notification.notify(message=message,app_name=appName,title=title)

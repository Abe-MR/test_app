from screeninfo import get_monitors

def get_screen_resolution():
    width = 0
    height = 0
    for m in get_monitors():
        item = str(m).replace("(", "").replace(",", "").replace("=", " ")
        width = int(item.split(" ")[5])
        height = int(item.split(" ")[7])
        break
    return (width, height)
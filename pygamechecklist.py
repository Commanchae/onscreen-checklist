import pygame

import win32api
import win32gui
import win32con

import tkinter.simpledialog
import tkinter

root = tkinter.Tk()
root.withdraw()

pygame.init()
pygame.font.init()

w, h = pygame.display.Info().current_w, pygame.display.Info().current_h

window = pygame.display.set_mode((w, h), 1)


transparency_color = (1,2,3)
# Set transparency color.


#REMOVE QUOTES TO MAKE TRANSPARENT

hwnd = pygame.display.get_wm_info()["window"]
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency_color), 0, win32con.LWA_COLORKEY)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

'''
ADD TO UI
        # Copy Paste into UI
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.showMaximized()

        self.exitButton.clicked.connect(lambda: exit())
        self.listWidget.addItem("hiffffffffffffffffffffffffffqdqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqffffffffffffffff")
        self.listWidget.addItem("Titel2")

        def setAATDFrame(value):
                self.frame_2.setHidden(value)

        def addToDo():
                print(self.titleInput.text())

        setAATDFrame(True)
        self.addButton.clicked.connect(lambda: setAATDFrame(False))
        self.aatdCancelButton.clicked.connect(lambda: addToDo())

'''


development_mouse_pos = [[0,0], [0,0]]
text_list = []

add_button = pygame.image.load("addpng.png")
add_button = pygame.transform.scale(add_button, (64,64))

#TEST
FONT = pygame.font.SysFont("Helvetica", 20)
test_text = "• Get recommendations"

test_surface = FONT.render(test_text, True, (255,255,255))
text_width, text_height = test_surface.get_size()
test_rect = pygame.Rect((0,500,text_width+10, text_height+5))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                development_mouse_pos[0] = list(pygame.mouse.get_pos())
            if event.key == pygame.K_f:
                development_mouse_pos[1] = list(pygame.mouse.get_pos())
                print("LEFT TOP WIDTH HEIGHT: ", development_mouse_pos[0][0], " " , development_mouse_pos[0][1], " ", development_mouse_pos[1][0]-development_mouse_pos[0][0], " ", development_mouse_pos[1][1] - development_mouse_pos[0][1])
            if event.key == pygame.K_q:
                exit()

    
    window.fill(transparency_color)
    # Blit here
    pygame.draw.rect(window, (0,0,0), test_rect)
    window.blit(test_surface, (0,500))
    window.blit(add_button, (w-70,h-70))
    pygame.display.update()
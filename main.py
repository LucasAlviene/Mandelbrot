import sdl2
import math
from Mandelbrot import Mandelbrot

colors = [
    (0, 0, 0, 255),
    (255, 0, 0, 255),
    (255, 100, 100, 255),
    (0, 255, 0, 255),
    (100, 255, 100, 255),
    (255, 165, 0, 255),
    (255, 255, 0, 255),
    (0, 0, 255, 255),
    (100, 100, 255, 255),
    (255, 0, 255, 255),
    (255, 224, 255, 255),
    (0, 255, 255, 255),
    (224, 255, 255, 255),
    (200, 200, 200, 255),
    (255,255,255, 255)
]

class CanvasObject:
    def __init__(self, title = None,width = 800, height = 600):
        self.scale = 3
        self.title = title.encode() if title else b"Canvas"
        self.width = width
        self.height = height
        sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
        self.window = sdl2.SDL_CreateWindow(self.title, sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, self.width, self.height, sdl2.SDL_WINDOW_SHOWN)
        self.renderer = sdl2.SDL_CreateRenderer(self.window, -1, 0)

        self.running = True 
        self.factor = 1.0
        self.isDraw = False

    def _draw(self,size,x, y,color = (255, 0, 100, 255)):
        sdl2.SDL_SetRenderDrawColor(self.renderer, color[0], color[1], color[2], color[3])

        self.rect = sdl2.SDL_FRect(x * size,y * size, size,size)

        sdl2.SDL_RenderDrawRectF(self.renderer, self.rect)
        sdl2.SDL_RenderFillRectF(self.renderer, self.rect)

        self.rect = sdl2.SDL_FRect(x * size,y * size, size,size)
    
    def color(self,index):
        return colors[index]

    def draw(self):
        self.isDraw = True
        sdl2.SDL_RenderClear(self.renderer)
        sdl2.SDL_SetRenderDrawColor(self.renderer, 255, 255 , 255 , 255)

        width = math.floor(self.width/self.scale)
        height = math.floor(self.height/self.scale)
        vector = Mandelbrot(width, height,self.factor)
        for i in range(0,width):
            for j in range(0,height):
                self._draw(self.scale,i,j,self.color(vector[i * height + j]))

        sdl2.SDL_SetRenderDrawColor(self.renderer, 255, 255 , 255 , 255)
        sdl2.SDL_RenderPresent(self.renderer)
        print("Renderizado")
        
        self.isDraw = False
      

    def loop(self):
        sdl2.SDL_ShowWindow(self.window)

        event = sdl2.SDL_Event()
        self.draw()

        while self.running:
            if sdl2.SDL_PollEvent(event) != 0:
                if event.type == sdl2.SDL_QUIT:
                    self.running = False
                if event.type == sdl2.SDL_KEYDOWN:
                    if self.isDraw == False:
                        if event.key.keysym.sym == 61: #+
                            self.factor /= 1.3
                            self.draw()
                        elif event.key.keysym.sym == 45: # -
                            self.factor *= 1.3
                            self.draw()
                    if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                        self.running = False
        
        sdl2.SDL_DestroyRenderer(self.renderer)
        sdl2.SDL_DestroyWindow(self.window)
        sdl2.SDL_Quit()
    
panel = CanvasObject("Trabalho de CLP",1080,720)
panel.loop()
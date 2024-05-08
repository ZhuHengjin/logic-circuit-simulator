from cmu_graphics import *
import copy, string, itertools, random

class logicGate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.selected = False
        self.outputGates = []
        self.output = False

### AND

class andGate(logicGate):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.left1XY = (x-30, y-7)
        self.left2XY = (x-30, y+7)
        self.rightXY = (x+30, y)
        self.left1, self.left2, self.right = False, False, False
        
        self.inputGate1 = None
        self.inputGate2 = None

    def connect(self, other):
        if self.left1 == True:
            self.inputGate1 = other
            other.outputGates.append(self)
        elif self.left2 == True:
            self.inputGate2 = other
            other.outputGates.append(self)
        elif self.right == True:
            if not isinstance(other, outGate) and other.right == True:
                self.right, other.right = False, False
            else:
                other.connect(self)
    
    def disconnect(self, other=None):
        if self.left1 == True:
            self.inputGate1.outputGates.remove(self)
            self.inputGate1 = None
        elif self.left2 == True:
            self.inputGate2.outputGates.remove(self)
            self.inputGate2 = None
        elif (other==self.inputGate1) and (other!=None):
            self.inputGate1 = None
        elif (other==self.inputGate2) and (other!=None):
            self.inputGate2 = None
        elif self.right ==True:
            for gate in self.outputGates:
                gate.disconnect(self)
            self.outputGates = []
    
    def disconnectAll(self):
        if self.inputGate1 != None:
            self.inputGate1.outputGates.remove(self)
        if self.inputGate2 != None:
            self.inputGate2.outputGates.remove(self)
        for gate in self.outputGates:
            gate.disconnect(self)
    
    def deselectAllDots(self):
        self.left1, self.left2, self.right = False, False, False
        
    def evaluate(self):
        if self.inputGate1 != None:
            input1 = self.inputGate1.output
        else:
            input1 = False
        
        if self.inputGate2 != None:
            input2 = self.inputGate2.output
        else:
            input2 = False
        
        self.output = input1 and input2
    
    def draw(self, editMode=True):
        x,y = self.x, self.y
        if editMode:
            fill = 'lightGreen' if self.selected else None
            left1 = 'gold' if self.left1 else 'black'
            left2 = 'gold' if self.left2 else 'black'
            right = 'gold' if self.right else 'black'
        else:
            fill = 'pink' if self.output else 'lightGrey'
            left1 = left2 = right = 'black'
        drawRect(x, y, 60, 40, fill=fill, border='black', align='center')
        drawLabel('And', x, y,  size=16, bold=True)
        drawCircle(*self.left1XY, 5, fill=left1)
        drawCircle(*self.left2XY, 5, fill=left2)
        drawCircle(*self.rightXY, 5, fill=right)
    
    def drawLine(self):
        if not self.inputGate1 == None:
            drawLine(*self.left1XY, *self.inputGate1.rightXY, 
                     fill='black', lineWidth=2)
        if not self.inputGate2 == None:
            drawLine(*self.left2XY, *self.inputGate2.rightXY, 
                     fill='black', lineWidth=2)
    
    def updateCoordinate(self, x, y):
        self.x = x
        self.y = y
        self.left1XY = (x-30, y-7)
        self.left2XY = (x-30, y+7)
        self.rightXY = (x+30, y)
    
    def dotSelected(self, mx, my): # if the mouse clicked on the dot
        (x, y) = self.left1XY
        if (x-5<=mx<=x+5) and (y-5<=my<=y+5):
            self.left1 = True
            return True
        (x, y) = self.left2XY
        if (x-5<=mx<=x+5) and (y-5<=my<=y+5):
            self.left2 = True
            return True
        (x, y) = self.rightXY
        if (x-5<=mx<=x+5) and (y-5<=my<=y+5):
            self.right = True
            return True
    
    def gateSelected(self, mx, my):
        x, y = self.x, self.y
        if (x-30<=mx<=x+30) and (y-20<=my<=y+20):
            self.selected = True
            return True

### OR

class orGate(logicGate):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.left1XY = (x-30, y-7)
        self.left2XY = (x-30, y+7)
        self.rightXY = (x+30, y)
        self.left1, self.left2, self.right = False, False, False
        
        self.inputGate1 = None
        self.inputGate2 = None

    def connect(self, other):
        if self.left1 == True:
            self.inputGate1 = other
            other.outputGates.append(self)
        elif self.left2 == True:
            self.inputGate2 = other
            other.outputGates.append(self)
        elif self.right == True:
            if not isinstance(other, outGate) and other.right == True:
                self.right, other.right = False, False
            else:
                other.connect(self)
    
    def disconnect(self, other=None):
        if self.left1 == True:
            self.inputGate1.outputGates.remove(self)
            self.inputGate1 = None
        elif self.left2 == True:
            self.inputGate2.outputGates.remove(self)
            self.inputGate2 = None
        elif (other==self.inputGate1) and (other!=None):
            self.inputGate1 = None
        elif (other==self.inputGate2) and (other!=None):
            self.inputGate2 = None
        elif self.right ==True:
            for gate in self.outputGates:
                gate.disconnect(self)
            self.outputGates = []
    
    def disconnectAll(self):
        if self.inputGate1 != None:
            self.inputGate1.outputGates.remove(self)
        if self.inputGate2 != None:
            self.inputGate2.outputGates.remove(self)
        for gate in self.outputGates:
            gate.disconnect(self)
    
    def deselectAllDots(self):
        self.left1, self.left2, self.right = False, False, False
        
    def evaluate(self):
        if self.inputGate1 != None:
            input1 = self.inputGate1.output
        else:
            input1 = False
        
        if self.inputGate2 != None:
            input2 = self.inputGate2.output
        else:
            input2 = False
        
        self.output = input1 or input2
    
    def draw(self, editMode=True):
        x,y = self.x, self.y
        if editMode:
            fill = 'lightGreen' if self.selected else None
            left1 = 'gold' if self.left1 else 'black'
            left2 = 'gold' if self.left2 else 'black'
            right = 'gold' if self.right else 'black'
        else:
            fill = 'pink' if self.output else 'lightGrey'
            left1 = left2 = right = 'black'
        drawRect(x, y, 60, 40, fill=fill, border='black', align='center')
        drawLabel('Or', x, y,  size=16, bold=True)
        drawCircle(*self.left1XY, 5, fill=left1)
        drawCircle(*self.left2XY, 5, fill=left2)
        drawCircle(*self.rightXY, 5, fill=right)
    
    def drawLine(self):
        if not self.inputGate1 == None:
            drawLine(*self.left1XY, *self.inputGate1.rightXY, 
                     fill='black', lineWidth=2)
        if not self.inputGate2 == None:
            drawLine(*self.left2XY, *self.inputGate2.rightXY, 
                     fill='black', lineWidth=2)
    
    def updateCoordinate(self, x, y):
        self.x = x
        self.y = y
        self.left1XY = (x-30, y-7)
        self.left2XY = (x-30, y+7)
        self.rightXY = (x+30, y)
    
    def dotSelected(self, mx, my): # if the mouse clicked on the dot
        (x, y) = self.left1XY
        if (x-5<=mx<=x+5) and (y-5<=my<=y+5):
            self.left1 = True
            return True
        (x, y) = self.left2XY
        if (x-5<=mx<=x+5) and (y-5<=my<=y+5):
            self.left2 = True
            return True
        (x, y) = self.rightXY
        if (x-5<=mx<=x+5) and (y-5<=my<=y+5):
            self.right = True
            return True
    
    def gateSelected(self, mx, my):
        x, y = self.x, self.y
        if (x-30<=mx<=x+30) and (y-20<=my<=y+20):
            self.selected = True
            return True

### NOT

class notGate(logicGate):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.left1XY = (x-30, y)
        self.rightXY = (x+30, y)
        self.left1, self.right = False, False
        
        self.inputGate1 = None

    def connect(self, other):
        if self.left1 == True:
            self.inputGate1 = other
            other.outputGates.append(self)
        elif self.right == True:
            if not isinstance(other, outGate) and other.right == True:
                self.right, other.right = False, False
            else:
                other.connect(self)
    
    def disconnect(self, other=None):
        if self.left1 == True:
            self.inputGate1.outputGates.remove(self)
            self.inputGate1 = None
        elif (other==self.inputGate1) and (other!=None):
            self.inputGate1 = None
        elif self.right ==True:
            for gate in self.outputGates:
                gate.disconnect(self)
            self.outputGates = []
    
    def disconnectAll(self):
        if self.inputGate1 != None:
            self.inputGate1.outputGates.remove(self)
        for gate in self.outputGates:
            gate.disconnect(self)
    
    def deselectAllDots(self):
        self.left1, self.right = False, False
        
    def evaluate(self):
        if self.inputGate1 != None:
            input1 = self.inputGate1.output
        else:
            input1 = False
        
        self.output = not input1
    
    def draw(self, editMode=True):
        x,y = self.x, self.y
        if editMode:
            fill = 'lightGreen' if self.selected else None
            left1 = 'gold' if self.left1 else 'black'
            right = 'gold' if self.right else 'black'
        else:
            fill = 'pink' if self.output else 'lightGrey'
            left1 = right = 'black'
        drawRect(x, y, 60, 40, fill=fill, border='black', align='center')
        drawLabel('Not', x, y,  size=16, bold=True)
        drawCircle(*self.left1XY, 5, fill=left1)
        drawCircle(*self.rightXY, 5, fill=right)
    
    def drawLine(self):
        if not self.inputGate1 == None:
            drawLine(*self.left1XY, *self.inputGate1.rightXY, 
                     fill='black', lineWidth=2)
    
    def updateCoordinate(self, x, y):
        self.x = x
        self.y = y
        self.left1XY = (x-30, y)
        self.rightXY = (x+30, y)
    
    def dotSelected(self, mx, my): # if the mouse clicked on the dot
        (x, y) = self.left1XY
        if (x-5<=mx<=x+5) and (y-5<=my<=y+5):
            self.left1 = True
            return True
        (x, y) = self.rightXY
        if (x-5<=mx<=x+5) and (y-5<=my<=y+5):
            self.right = True
            return True
    
    def gateSelected(self, mx, my):
        x, y = self.x, self.y
        if (x-30<=mx<=x+30) and (y-20<=my<=y+20):
            self.selected = True
            return True

### IN

class inGate(logicGate):
    gateList = []
    def __init__(self, x, y):
        super().__init__(x, y)
        self.rightXY = (x+30, y)
        self.right = False
        
        inGate.gateList.append(self)
        
    def connect(self, other):
        if self.right == True:
            if not isinstance(other, outGate) and other.right == True:
                self.right, other.right = False, False
            else:
                other.connect(self)
    
    def disconnect(self, other=None):
        if self.right == True:
            for gate in self.outputGates:
                gate.disconnect(self)
            self.outputGates = []
    
    def disconnectAll(self):
        for gate in self.outputGates:
            gate.disconnect(self)
    
    def deselectAllDots(self):
        self.right = False
        
    def evaluate(self):
        pass
    
    def draw(self, editMode=True):
        x,y = self.x, self.y
        index = inGate.gateList.index(self)+65-1
        if index == 64:
            letter = 'Input'
        elif 65<=index<127:
            letter = chr(index)
        else:
            letter = ''
        if editMode:
            fill = 'lightGreen' if self.selected else None
            right = 'gold' if self.right else 'black'
        else:
            fill = 'pink' if self.output else 'lightGrey'
            right = 'black'
        drawRect(x, y, 60, 40, fill=fill, border='black', align='center')
        drawLabel(f'{letter}', x, y, size=16, bold=True)
        drawCircle(*self.rightXY, 5, fill=right)
    
    def drawLine(self):
        pass
    
    def updateCoordinate(self, x, y):
        self.x = x
        self.y = y
        self.rightXY = (x+30, y)
    
    def dotSelected(self, mx, my): # if the mouse clicked on the dot
        (x, y) = self.rightXY
        if (x-5<=mx<=x+5) and (y-5<=my<=y+5):
            self.right = True
            return True
    
    def gateSelected(self, mx, my):
        x, y = self.x, self.y
        if (x-30<=mx<=x+30) and (y-20<=my<=y+20):
            self.selected = True
            return True

### OUT    

class outGate(logicGate):
    gateList = []
    def __init__(self, x, y):
        super().__init__(x, y)
        self.leftXY = (x-30, y)
        self.left = False
        
        self.inputGate = None
        outGate.gateList.append(self)

    def connect(self, other):
        if self.left == True:
            self.inputGate = other
            other.outputGates.append(self)
    
    def disconnect(self, other=None):
        if self.left == True:
            self.inputGate.outputGates.remove(self)
            self.inputGate = None
        elif other==self.inputGate!=None:
            self.inputGate = None
    
    def disconnectAll(self):
        if self.inputGate != None:
            self.inputGate.outputGates.remove(self)
    
    def deselectAllDots(self):
        self.left = False
        
    def evaluate(self):
        if self.inputGate != None: #self.inputGate.output != None:
            self.output = self.inputGate.output
    
    def draw(self, editMode=True):
        x,y = self.x, self.y
        index = outGate.gateList.index(self)+65-1
        if index == 64:
            letter = 'Output'
        elif 65<=index<127:
            letter = chr(index)
        else:
            letter = ''
        if editMode:
            fill = 'lightGreen' if self.selected else None
            left = 'gold' if self.left else 'black'
        else:
            fill = 'pink' if self.output else 'lightGrey'
            left = 'black'
        drawRect(x, y, 60, 40, fill=fill, border='black', align='center')
        drawLabel(f'{letter}', x, y, size=16, bold=True)
        drawCircle(*self.leftXY, 5, fill=left)
    
    def drawLine(self):
        if not self.inputGate == None:
            drawLine(*self.leftXY, *self.inputGate.rightXY, 
                     fill='black', lineWidth=2)
    
    def updateCoordinate(self, x, y):
        self.x = x
        self.y = y
        self.leftXY = (x-30, y)
    
    def dotSelected(self, mx, my): # if the mouse clicked on the dot
        (x, y) = self.leftXY
        if (x-5<=mx<=x+5) and (y-5<=my<=y+5):
            self.left = True
            return True
    
    def gateSelected(self, mx, my):
        x, y = self.x, self.y
        if (x-30<=mx<=x+30) and (y-20<=my<=y+20):
            self.selected = True
            return True

### functions
            
def updateCircuits(gateList=inGate.gateList):
    for gate in gateList:
        gate.evaluate()
    for gate in gateList:
        for outputGate in gate.outputGates:
            return updateCircuit(outputGate)

def updateCircuit(inputGate): # helper for updateCircuits
    if isinstance(inputGate, outGate): #change
        inputGate.evaluate()
        return
    else:
        inputGate.evaluate()
        for outputGate in inputGate.outputGates:
            outputGate.evaluate()
            updateCircuit(outputGate)
        
#########################################
# gate class and functions
#########################################

def onAppStart(app):
    app.gateList = [] # for drawing and selection (input also goes here)
    app.offBoardGateList = [andGate(55, 70), orGate(55, 130), notGate(55, 190), 
                            inGate(55, 250), outGate(55, 310)]
    app.pickingStatus = False 
    app.pickedItem = None # 1:and, 2:or, 3:not, 4:input, 5:output
    app.selectedGate = None
    app.selectedDots = None
    app.editMode = True
    app.dragging = False
    app.placing = False
    app.dx, app.dy = 0, 0
    

def onMousePress(app, mx, my):
    if app.editMode:
        handleEditMouse(app, mx, my)
    else:
        handleRunMouse(app, mx, my)

def onMouseRelease(app, mX, mY):
    app.placing = False
    app.dragging = False

def handleEditMouse(app, mx, my):
    if app.pickingStatus == False:
        if mx <= 100: # picked from the left
            handleMouseSelectNew(app, mx, my)
            
        elif mx >= 100: # drag gate or connect gate
            handleMouseSelecting(app, mx, my)
            
    elif app.pickingStatus == True:
        if handleMouseSelecting(app, mx, my)==True:
            app.pickingStatus = False
            return None
        elif (mx >= 100):
            mx=150 if mx<150 else mx # make sure not too left
            if app.pickedItem == 0:
                app.gateList.append(andGate(mx, my))
            elif app.pickedItem == 1:
                app.gateList.append(orGate(mx, my))
            elif app.pickedItem == 2:
                app.gateList.append(notGate(mx, my))
            elif app.pickedItem == 3:
                app.gateList.append(inGate(mx, my))
            elif app.pickedItem == 4:
                app.gateList.append(outGate(mx, my))
            app.placing = True
            app.pickedItem = None
            resetSelectedGates(app)
            app.selectedGate = app.gateList[-1]
            app.gateList[-1].gateSelected(mx, my)
            app.pickingStatus = False
        elif mx <= 100:
            handleMouseSelectNew(app, mx, my)

def handleMouseSelecting(app, mx, my):
    for i in range(len(app.gateList)):
        gate = app.gateList[i]
        if gate.dotSelected(mx, my): # dot selected
            resetSelectedGates(app)
            if not app.selectedDots == None: # a gate's dot is already selected
                gate.connect(app.selectedDots)
                gate.deselectAllDots()
                resetSelectedDots(app)
            else:
                app.selectedDots = gate
            return True
        else:
            if gate.gateSelected(mx, my): #gate selected
                resetSelectedDots(app)
                if app.selectedGate != None and app.selectedGate != gate:
                    resetSelectedGates(app)
                app.selectedGate = gate
                app.dx, app.dy = mx-app.selectedGate.x, my-app.selectedGate.y
                return True
    if app.selectedGate == None and app.selectedDots != None:
        resetSelectedDots(app)
        return False
    return False
    

def handleMouseSelectNew(app, mx, my):
    for i in range(len(app.offBoardGateList)):
        gate = app.offBoardGateList[i]
        if gate.gateSelected(mx, my):
            resetSelectedDots(app)
            if app.selectedGate != None and app.selectedGate != gate:
                resetSelectedGates(app)
            app.selectedGate = gate
            app.pickedItem = i
            app.pickingStatus = True
            return

def handleRunMouse(app, mx, my):
    if mx >= 100:
        for i in range(len(app.gateList)):
            gate = app.gateList[i]
            if gate.gateSelected(mx, my) and isinstance(gate, inGate):
                gate.output = not gate.output
        updateCircuits(app.gateList)

def onMouseDrag(app, mx, my):
    if ((not app.selectedGate == None) and 
        (app.selectedGate in app.gateList) and
        (not app.placing) and
        ((app.selectedGate.gateSelected(mx, my)) or
         (app.dragging))):
        app.selectedGate.updateCoordinate(mx-app.dx, my-app.dy)
        app.dragging = True

def onKeyPress(app, key):
    if key == 'e':
        app.editMode = True
        resetAllGatesFromRunning(app)
    if key == 'r':
        app.editMode = False
        resetAllSelections(app)
        updateCircuits(app.gateList)
    if key == 'backspace':
        if not app.selectedGate == None:
            handleDelete(app, app.selectedGate)
            app.gateList.remove(app.selectedGate)
            app.selectedGate = None
        if not app.selectedDots == None:
            app.selectedDots.disconnect()

def handleDelete(app, gate): #delete them from the class list
    gate.disconnectAll()
    if isinstance(gate, inGate):
        inGate.gateList.remove(gate)
    elif isinstance(gate, outGate):
        outGate.gateList.remove(gate)
        

def resetAllSelections(app):
    resetSelectedDots(app)
    resetSelectedGates(app)

def resetSelectedDots(app): # only handle dots in one gate
    if not app.selectedDots == None:
        app.selectedDots.deselectAllDots()
        app.selectedDots = None

def resetSelectedGates(app):
    if not app.selectedGate == None:
        app.selectedGate.selected = False
        app.selectedGate = None

def resetAllGatesFromRunning(app):
    for gate in app.gateList:
        gate.selected = False
        gate.output = False

def redrawAll(app):
    drawLabels(app)
    drawLeftGates(app)
    drawOnBoardGates(app)
    drawLine(100, 50, 100, 600)

def drawLeftGates(app):
    for gate in app.offBoardGateList:
        gate.draw()

def drawOnBoardGates(app):
    for gate in app.gateList:
        gate.draw(app.editMode)
        if not isinstance(gate, inGate):
            gate.drawLine()

def drawLabels(app):
    mode = 'Edit Mode' if app.editMode else 'Run Mode'
    drawLabel('Logic Circuit Simulator', 400, 20, bold=True, size=16)
    drawLabel('Press e to edit or r to run', 400, 40, size=14)
    drawLabel(mode, 400, 60, bold=True, size=14)

def main():
    runApp(width = 800, height = 600)

main()
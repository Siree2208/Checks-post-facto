
def screen4(inputs):
    
    full=[]
    import tkinter
    import pygame
    player=inputs[-1]
    moves=[]
    for i in range(0,len(inputs)-1):
        moves.append(inputs[i])
    
    WIDTH, HEIGHT = 900, 400
    SQUARE_SIZE = WIDTH // 8
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Checkerboard before moves")
    board=['.','.','.','.',
           '.','.','.','.',
           '.','.','.','.',
           '.','.','.','.',
           '.','.','.','.',
           '.','.','.','.',
           '.','.','.','.',
           '.','.','.','.'
          ]
    def Print(board):
        print("\n")
        k = 0
        while k < 32:
            for i in range(0, 8):
                for j in range(0, 4):
                    if i % 2 == 0:
                        print('-', board[k], end="")
                        k = k + 1
                    else:
                        print(board[k], '-', end="")
                        k = k + 1
                print('\t')
   
    
    movements = []
    x = 0
    for i in moves:
        for j in i:
            if j == '-':
                x = i.split('-')
            if j == '*':
                x = i.split('*')
        movements.append(x)
    
    for i in range(len(movements)):
        for j in range(len(movements[i])):
            movements[i][j] = (int(movements[i][j])) - 1
    movements.reverse()
    def convert(board):
        list1=[]
        k = 0
        while k < 32:
            for i in range(0,8):
                row=[]
                for j in range(0,4):
                    if i % 2 == 0:
                        row.append('-')
                        row.append(board[k])
                    else:
                        row.append(board[k])
                        row.append("-")
                    k = k + 1
                list1.append(row)
        return list1
    def before_checker(board, movements):
        if player == "m":
            player1 = 'm'
            player2 = 'b'
        else:
            player1 = 'b'
            player2 = 'm'
        
        for i in movements:
            jumps = len(i) - 1
            if jumps == 1:
                if i[0] <= 31 and i[1] <= 31:
                    if (i[1] == i[0] + 3) or (i[1] == i[0] + 4) or (i[1] == i[0] + 5) or(i[1] == i[0] - 3) or (i[1] == i[0] - 4) or (i[1] == i[0] - 5):
                        if (len(movements) - 1 - movements.index(i)) % 2 == 0:
                            current = player1
                        else:
                            current = player2
                        before_simply(current , i)
                    if (i[1] == i[0] + 7) or (i[1] == i[0] + 9) or (i[1] == i[0] - 7) or (i[1] == i[0] - 9):
                        if (movements.index(i)) % 2 == 0:
                            current = player1
                        else:
                            current = player2
                        before_double(current , i)
                else:
                    print('Invalid1')
            if jumps >= 2:
                if (movements.index(i)) % 2 == 0:
                    current = player1
                else:
                    current = player2
                before_multiple(current , i)
    
    def before_simply(current , i):
        if current == 'm':
            if i[1] < i[0]:
                board[i[0]] = current
                board[i[1]] = '.'
            else:
                board[i[0]] = capital(current)
                board[i[1]] = '.'
        else:
            if i[1] > i[0]:
                board[i[0]] = current
                board[i[1]] = '.'
            else:
                board[i[0]] = capital(current)
                board[i[1]] = '.'
    
    def before_double(current , i):
        if current == 'm':
            if i[1] < i[0]:
                board[i[0]] = current
                board[i[1]] = '.'
            else:
                board[i[0]] = capital(current)
                board[i[1]] = '.'
        else:
            if i[1] > i[0]:
                board[i[0]] = current
                board[i[1]] = '.'
            else:
                board[i[0]] = capital(current)
                board[i[1]] = '.'
        place_in_middle(current , i)
    
    def before_multiple(current , i):
        if current == 'b':
            for a in range(0 , len(i) - 1):
                if i[a] < i[a+1]:
                    board[i[0]] = current
                else:
                    board[i[0]] = capital(current)
        if current == 'm':
            for a in range(0 , len(i) - 1):
                if i[a] > i[a+1]:
                    board[i[0]] = current
                else:
                    board[i[0]] =  capital(current)
        for a in range(1 , len(i)):
            board[i[a]] = '.'
        split = []
        for index in range(0 , len(i) - 1):
            splits = []
            for index1 in range(1 , len(i)):
                a = i[index]
                b = i[index+1]
                splits.append(a)
                splits.append(b)
                split.append(splits)
        for a in split:
            place_in_middle(current , a)
    
    def place_in_middle(current , i):
        if i[0] in [28,29,30,31]:
            if i[1] == i[0] - 7:
                board[i[0] - 4] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = opp(current)
            else:
                print('Invalid2')
        elif i[0] in [24,25,26,27]:
            if i[1] == i[0] - 7:
                board[i[0] - 3] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0] - 4] = opp(current)
            else:
                print('Invalid3')
        elif i[0] in [20,21,22,23]:
            if i[1] == i[0] - 7:
                board[i[0] - 4] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = opp(current)
            elif i[1] == i[0] + 7:
                board[i[0] + 3] = opp(current)
            elif i[1] == i[0] + 9:
                board[i[0] + 4] = opp(current)
            else:
                print('Invalid4')
        elif i[0] in [16,17,18,19]:
            if i[1] == i[0] + 9:
                board[i[0] + 5] = opp(current)
            elif i[1] == i[0] + 7:
                board[i[0] + 4] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0] - 4] = opp(current)
            elif i[1] == i[0] - 7:
                board[i[0] - 3]=opp(current)
        elif i[0] in [12,13,14,15]:
            if i[1] == i[0] + 9:
                board[i[0] + 4] = opp(current)
            elif i[1] == i[0] + 7:
                board[i[0] + 3] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = opp(current)
            elif i[1] == i[0] - 7:
                board[i[0] - 4] = opp(current)
            else:
                print('Invalid5')
        elif i[0] in [8,9,10,11]:
            if i[1] == i[0] + 9:
                board[i[0] + 5]=opp(current)
            elif i[1] == i[0] + 7:
                board[i[0] + 4] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0]  - 4] = opp(current)
            elif i[1] == i[0] - 7:

                board[i[0] - 3] = opp(current)
            else:
                print('Invalid6')
        elif i[0] in [4,5,6,7]:
            if i[1] == i[0] + 7:
                board[i[0]+3] = opp(current)
            elif i[1] == i[0] + 9:
                board[i[0] + 4] = opp(current)
            else:
                print('Invalid7')
        elif i[0] in [0,1,2,3]:
            if i[1] == i[0]+7:
                board[i[0] + 4] = opp(current)
            elif i[1] == i[0] + 9:
                board[i[0] + 5] = opp(current)
            else:
                print('Invalid8')
        else:
            print('invalid9')
    def capital(current):
        if current == 'm':
            return 'M'
        else:
            return 'B' 
    def opp(current):
        if current == 'm':
            return 'b'
        else:
            return 'm'
    before_checker(board , movements)
    before_board = board
    list1=convert(before_board)
    full.append(list1)
    if player == "m":
        player1 = 'm'
        player2 = 'b'
    else:
        player1 = 'b'
        player2 = 'm'
    movements.reverse()
    def after_checker(board,jumps):
            print(movements)
            if jumps == 1:
                if (i[1] == i[0] + 3) or (i[1] == i[0] + 4) or (i[1] == i[0] + 5) or (i[1] == i[0] - 3) or (i[1] == i[0] - 4) or (i[1] == i[0] - 5):
                    if (movements.index(i)) % 2 == 0:
                        current = player1
                    else:
                        current = player2
                    
                    after_simply(current, i)
                if (i[1] == i[0] + 7) or (i[1] == i[0] + 9) or (i[1] == i[0] - 7) or (i[1] == i[0] - 9):
                    
                    if (movements.index(i)) % 2 == 0:
                        current = player1
                    else:
                        current = player2
                    after_double(current, i)
            if jumps >= 2:
                if (movements.index(i)) % 2 == 0:
                    current = player1
                else:
                    current = player2
                
                after_multiple(current, i)

    def after_simply(current, i):
        
        if current == 'm':
            if board[i[0]] == 'm':
                if (i[0] in [4, 5, 6, 7]):
                    board[i[1]] = 'M'
                    board[i[0]] = '.'
                elif i[0] >= 8 and i[0] <= 31:
                    board[i[1]] = 'm'
                    board[i[0]] = '.'
                else:
                    print('invalid10')
            if board[i[0]] == 'M':
                if i[0] >= 0 and i[0] <= 31:
                    board[i[1]] = 'M'
                    board[i[0]] = '.'
            
        if current == 'b':
            if board[i[0]] == 'b':
                if (i[0] in [24, 25, 26, 27]) and (i[1] > i[0]):
                    board[i[1]] = 'B'
                    board[i[0]] = '.'
                elif i[0] >= 0 and i[0] <= 23:
                    board[i[1]] = 'b'
                    board[i[0]] = '.'
                else:
                    print('invalid')
            if board[i[0]] == 'B':
                if i[0] >= 0 and i[0] <= 31:
                    board[i[1]] = 'B'
                    board[i[0]] ='.'
        Print(board)
    def after_double(current, i):
        if current == "m":
            if board[i[0]] == "m":
                if i[0] >= 12 and i[0] <= 31:
                    board[i[1]] = "m"
                    board[i[0]] = "."
                elif i[0] in [8, 9, 10, 11]:
                    board[i[1]] = "M"
                    board[i[0]] = "."
                else:
                    print("invalid11")
            if board[i[0]] == "M":
                board[i[1]] = "M"
                board[i[0]] = "."
        if current == "b":
            if board[i[0]] == "b":
                if i[0] >= 0 and i[0] <= 19:
                    board[i[1]] = "b"
                    board[i[0]] = "."
                elif i[0] in [20, 21, 22, 23]:
                    board[i[1]] = "B"
                    board[i[0]] = "."
                else:
                    print("invalid12")
            if board[i[0]] == "B":
                board[i[1]] = "B"
                board[i[0]] = "."
        remove_in_middle(current, i)
        Print(board)
    def after_multiple(current, i):
        x = board[i[0]]
        board[i[-1]] = x
        board[i[0]] = '.'
        split = []
        for index in range(0, len(i) - 1):
            splits = []
            for index1 in range(1, len(i)):
                a = i[index]
                b = i[index + 1]
            splits.append(a)
            splits.append(b)
            split.append(splits)
        for a in split:
            remove_in_middle(current, a)
        Print(board)
    def remove_in_middle(current, i):
        if i[0] in [28, 29, 30, 31]:
            if i[1] == i[0] - 7:
                board[i[0] - 4] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = '.'
            else:
                print('Invalid13')
        elif i[0] in [24, 25, 26, 27]:
            if i[1] == i[0] - 7:
                board[i[0] - 3] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 4] = '.'
            else:
                print('Invalid14')
        elif i[0] in [20, 21, 22, 23]:
            
            if i[1] == i[0] - 7:
                board[i[0] - 4] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = '.'
            elif i[1] == i[0] + 7:
                board[i[0] + 3] = '.'
            elif i[1] == i[0] + 9:
                board[i[0] + 4] = '.'
            else:
                print('Invalid15')
        elif i[0] in [16, 17, 18, 19]:
            if i[1] == i[0] + 9:
                board[i[0] + 5] = '.'
            elif i[1] == i[0] + 7:
                board[i[0] + 4] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 4] = '.'
            elif i[1] == i[0] - 7:
                board[i[0] - 3] = '.'
            else:
                print('Invalid16')
        elif i[0] in [12,13,14,15]:
            if i[1] == i[0] + 9:
                board[i[0] + 4] = '.'
            elif i[1] == i[0] + 7:
                board[i[0] + 3] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = '.'
            elif i[1] == i[0] - 7:
                board[i[0] - 4] = '.'
            else:
                print('Invalid17')
        elif i[0] in [8,9,10,11]:
            if i[1] == i[0] + 9:
                board[i[0] + 5]='.'
            elif i[1] == i[0] + 7:
                board[i[0]+4] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 4] = '.'
            elif i[1] == i[0] - 7:
                board[i[0] - 3] = '.'
            else:
                print('Invalid18')
        elif i[0] in [4,5,6,7]:
            if i[1] == i[0] + 7:
                board[i[0] + 3] = '.'
            elif i[1] == i[0] + 9:
                board[i[0] + 4] = '.'
            else:
                print('Invalid19')
        elif i[0] in [0,1,2,3]:
            if i[1] == i[0] + 7:
                board[i[0] + 4] = '.'
            elif i[1] == i[0] + 9:
                board[i[0] + 5]='.'
            else:
                print('Invalid20')
        else:
            print('invalid21')

    for i in movements:
        after_checker(board,(len(i)-1))
        list1=convert(board)
        full.append(list1)
    print(full)
    def display(checkerboard,i):
        import tkinter as tk
        from tkinter import Canvas
    
        WHITE = "#FFFFFF"
        GRAY = "#969696"
        RED = "#FF0000"
        MAROON = "#800000"
        BLACK="#000000"
    
        WIDTH, HEIGHT = 800, 400  # Adjusted height to make space for the start button
        SQUARE_SIZE = WIDTH // 16
    
        def draw_checkerboard(canvas):
            for row in range(8):
                for col in range(8):
                    square_color = WHITE if (row + col) % 2 == 0 else GRAY
                    canvas.create_rectangle(col * SQUARE_SIZE, row * SQUARE_SIZE, (col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, fill=square_color)
    
            for row in range(8):
                for col in range(8):
                    coin = checkerboard[row][col]
                    if coin == 'm':
                        canvas.create_oval(col * SQUARE_SIZE + SQUARE_SIZE // 5, row * SQUARE_SIZE + SQUARE_SIZE // 5,
                                       (col + 1) * SQUARE_SIZE - SQUARE_SIZE // 5, (row + 1) * SQUARE_SIZE - SQUARE_SIZE // 5,
                                       fill=MAROON, outline="")
                    elif coin == 'M':
                        canvas.create_oval(col * SQUARE_SIZE , row * SQUARE_SIZE ,
                                       (col + 1) * SQUARE_SIZE , (row + 1) * SQUARE_SIZE ,
                                       fill=MAROON, outline="gold")
                    elif coin == 'b':
                        canvas.create_oval(col * SQUARE_SIZE + SQUARE_SIZE // 5, row * SQUARE_SIZE + SQUARE_SIZE // 5,
                                       (col + 1) * SQUARE_SIZE - SQUARE_SIZE // 5, (row + 1) * SQUARE_SIZE - SQUARE_SIZE // 5,
                                       fill=BLACK, outline="")
                    elif coin == 'B':
                        canvas.create_oval(col * SQUARE_SIZE , row * SQUARE_SIZE ,
                                       (col + 1) * SQUARE_SIZE , (row + 1) * SQUARE_SIZE,
                                       fill=BLACK, outline="gold")
    
        def start_game():
            if i<len(list1):
                fun(i+1)
            else:
                root.quit()
        def quit_game():
            if i>=len(list1):
               root.quit()
        root = tk.Tk()
        root.geometry('600x500+30+30')
        root.title(f"Checkerboard after move{i}")

        canvas = Canvas(root, width=WIDTH, height=HEIGHT)

        canvas.pack()
    
        draw_checkerboard(canvas)
        quit_button= tk.Button(root,text="Quit",command=quit_game)
        start_button = tk.Button(root, text="Next move", command=start_game)
        start_button.pack(side="top")
        quit_button.pack(side="top")
    
        root.mainloop()
        start_game()
        return i
    i=0
    def fun(i):
        while i<len(full):
            list=full[i]
            display(list,i)
    
    fun(i)
def screen3(inputs):
    import pygame
    import tkinter as tk
    input1=inputs
    
    def display_boards(screen,board1,board2):
        import pygame
        import tkinter as tk
        def start_game():
            screen4(input1)
        root=tk.Tk()
        root.title("")
        start_button=tk.Button(root,text="DETAIL",command=start_game)
        
        start_button.pack()
        WHITE=(255,255,255)
        BLACK=(0,0,0)
        GRAY=(150,150,150)
        MAROON=(128,0,0)
        WIDTH,HEIGHT=400,400
        SQUARE_SIZE=WIDTH//8
        pygame.init()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   running = False
            screen.fill((0, 0, 0))
            for row in range(8):
                for col in range(8):
                    square_color = WHITE if (row + col) % 2 == 0 else GRAY
                    pygame.draw.rect(screen, square_color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                    coin = board1[row][col]
                    if coin == 'm':
                        pygame.draw.circle(screen, MAROON, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)
                    elif coin == 'M':
                        pygame.draw.circle(screen, MAROON, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2)
                    elif coin == 'b':
                        pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)
                    elif coin == 'B':
                        pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2)
            x_offset = WIDTH +50
            for row in range(8):
                for col in range(8):
                    square_color = WHITE if (row + col) % 2 == 0 else GRAY
                    pygame.draw.rect(screen, square_color, pygame.Rect(x_offset + col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                    coin = board2[row][col]
                    if coin == 'm':
                        pygame.draw.circle(screen, MAROON, (x_offset + col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)
                    elif coin == 'M':
                        pygame.draw.circle(screen, MAROON, (x_offset + col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2)
                    elif coin == 'b':
                        pygame.draw.circle(screen, BLACK, (x_offset + col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)
                    elif coin == 'B':
                        pygame.draw.circle(screen, BLACK, (x_offset + col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2)
            
            pygame.display.flip()
            root.mainloop()
        pygame.quit()
    WIDTH, HEIGHT = 850, 500
    SQUARE_SIZE = WIDTH // 8
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Checkerboard before and after")
    board=['.','.','.','.',
           '.','.','.','.',
           '.','.','.','.',
           '.','.','.','.',
           '.','.','.','.',
           '.','.','.','.',
           '.','.','.','.',
           '.','.','.','.'
          ]
    def Print(board):
        k = 0
        while k < 32:
            for i in range(0, 8):
                for j in range(0, 4):
                    if i % 2 == 0:
                        print('-', board[k], end="")
                        k = k + 1
                    else:
                        print(board[k], '-', end="")
                        k = k + 1
                print('\t')
   
    player=inputs[-1]
    moves=[]
    for i in range(0,len(inputs)-1):
        moves.append(inputs[i])
    
    movements = []
    x = 0
    for i in moves:
        for j in i:
            if j == '-':
                x = i.split('-')
            if j == '*':
                x = i.split('*')
        movements.append(x)
    
    for i in range(len(movements)):
        for j in range(len(movements[i])):
            movements[i][j] = (int(movements[i][j])) - 1
    movements.reverse()
    def convert(board):
        list1=[]
        k = 0
        while k < 32:
            for i in range(0,8):
                row=[]
                for j in range(0,4):
                    if i % 2 == 0:
                        row.append('-')
                        row.append(board[k])
                    else:
                        row.append(board[k])
                        row.append("-")
                    k = k + 1
                list1.append(row)
        return list1
    def before_checker(board, movements):
        if player == "m":
            player1 = 'm'
            player2 = 'b'
        else:
            player1 = 'b'
            player2 = 'm'
        
        for i in movements:
            jumps = len(i) - 1
            if jumps == 1:
                if i[0] <= 31 and i[1] <= 31:
                    if (i[1] == i[0] + 3) or (i[1] == i[0] + 4) or (i[1] == i[0] + 5) or(i[1] == i[0] - 3) or (i[1] == i[0] - 4) or (i[1] == i[0] - 5):
                        if (len(movements) - 1 - movements.index(i)) % 2 == 0:
                            current = player1
                        else:
                            current = player2
                        before_simply(current , i)
                    if (i[1] == i[0] + 7) or (i[1] == i[0] + 9) or (i[1] == i[0] - 7) or (i[1] == i[0] - 9):
                        if (movements.index(i)) % 2 == 0:
                            current = player1
                        else:
                            current = player2
                        before_double(current , i)
                else:
                    print('Invalid1')
            if jumps >= 2:
                if (movements.index(i)) % 2 == 0:
                    current = player1
                else:
                    current = player2
                before_multiple(current , i)
    
    def before_simply(current , i):
        if current == 'm':
            if i[1] < i[0]:
                board[i[0]] = current
                board[i[1]] = '.'
            else:
                board[i[0]] = capital(current)
                board[i[1]] = '.'
        else:
            if i[1] > i[0]:
                board[i[0]] = current
                board[i[1]] = '.'
            else:
                board[i[0]] = capital(current)
                board[i[1]] = '.'
    
    def before_double(current , i):
        if current == 'm':
            if i[1] < i[0]:
                board[i[0]] = current
                board[i[1]] = '.'
            else:
                board[i[0]] = capital(current)
                board[i[1]] = '.'
        else:
            if i[1] > i[0]:
                board[i[0]] = current
                board[i[1]] = '.'
            else:
                board[i[0]] = capital(current)
                board[i[1]] = '.'
        place_in_middle(current , i)
    
    def before_multiple(current , i):
        if current == 'b':
            for a in range(0 , len(i) - 1):
                if i[a] < i[a+1]:
                    board[i[0]] = current
                else:
                    board[i[0]] = capital(current)
        if current == 'm':
            for a in range(0 , len(i) - 1):
                if i[a] > i[a+1]:
                    board[i[0]] = current
                else:
                    board[i[0]] = capital(current)
        for a in range(1 , len(i)):
            board[i[a]] = '.'
        split = []
        for index in range(0 , len(i) - 1):
            splits = []
            for index1 in range(1 , len(i)):
                a = i[index]
                b = i[index+1]
                splits.append(a)
                splits.append(b)
                split.append(splits)
        for a in split:
            place_in_middle(current , a)
    
    def place_in_middle(current , i):
        if i[0] in [28,29,30,31]:
            if i[1] == i[0] - 7:
                board[i[0] - 4] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = opp(current)
            else:
                print('Invalid2')
        elif i[0] in [24,25,26,27]:
            if i[1] == i[0] - 7:
                board[i[0] - 3] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0] - 4] = opp(current)
            else:
                print('Invalid3')
        elif i[0] in [20,21,22,23]:
            if i[1] == i[0] - 7:
                board[i[0] - 4] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = opp(current)
            elif i[1] == i[0] + 7:
                board[i[0] + 3] = opp(current)
            elif i[1] == i[0] + 9:
                board[i[0] + 4] = opp(current)
            else:
                print('Invalid4')
        elif i[0] in [16,17,18,19]:
            if i[1] == i[0] + 9:
                board[i[0] + 5] = opp(current)
            elif i[1] == i[0] + 7:
                board[i[0] + 4] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0] - 4] = opp(current)
            elif i[1] == i[0] - 7:
                board[i[0] - 3]=opp(current)
        elif i[0] in [12,13,14,15]:
            if i[1] == i[0] + 9:
                board[i[0] + 4] = opp(current)
            elif i[1] == i[0] + 7:
                board[i[0] + 3] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = opp(current)
            elif i[1] == i[0] - 7:
                board[i[0] - 4] = opp(current)
            else:
                print('Invalid5')
        elif i[0] in [8,9,10,11]:
            if i[1] == i[0] + 9:
                board[i[0] + 5]=opp(current)
            elif i[1] == i[0] + 7:
                board[i[0] + 4] = opp(current)
            elif i[1] == i[0] - 9:
                board[i[0]  - 4] = opp(current)
            elif i[1] == i[0] - 7:

                board[i[0] - 3] = opp(current)
            else:
                print('Invalid6')
        elif i[0] in [4,5,6,7]:
            if i[1] == i[0] + 7:
                board[i[0]+3] = opp(current)
            elif i[1] == i[0] + 9:
                board[i[0] + 4] = opp(current)
            else:
                print('Invalid7')
        elif i[0] in [0,1,2,3]:
            if i[1] == i[0]+7:
                board[i[0] + 4] = opp(current)
            elif i[1] == i[0] + 9:
                board[i[0] + 5] = opp(current)
            else:
                print('Invalid8')
        else:
            print('invalid9')
    def capital(current):
        if current == 'm':
            return 'M'
        else:
            return 'B' 
    def opp(current):
        if current == 'm':
            return 'b'
        else:
            return 'm'
    before_checker(board , movements)
    before_board = board
    list1=convert(before_board)
    print("list1",list1)
    if player == "m":
        player1 = 'm'
        player2 = 'b'
    else:
        player1 = 'b'
        player2 = 'm'
    movements.reverse()
    def after_checker(board, movements):
        for i in movements:
            jumps = len(i) - 1
            if jumps == 1:
                if (i[1] == i[0] + 3) or (i[1] == i[0] + 4) or (i[1] == i[0] + 5) or (i[1] == i[0] - 3) or (i[1] == i[0] - 4) or (i[1] == i[0] - 5):
                    if (movements.index(i)) % 2 == 0:
                        current = player1
                    else:
                        current = player2
                    
                    after_simply(current, i)
                if (i[1] == i[0] + 7) or (i[1] == i[0] + 9) or (i[1] == i[0] - 7) or (i[1] == i[0] - 9):
                    
                    if (movements.index(i)) % 2 == 0:
                        current = player1
                    else:
                        current = player2
                    after_double(current, i)
            if jumps >= 2:
                if (movements.index(i)) % 2 == 0:
                    current = player1
                else:
                    current = player2
                
                after_multiple(current, i)

    def after_simply(current, i):
        
        if current == 'm':
            if board[i[0]] == 'm':
                if (i[0] in [4, 5, 6, 7]):
                    board[i[1]] = 'M'
                    board[i[0]] = '.'
                elif i[0] >= 8 and i[0] <= 31:
                    board[i[1]] = 'm'
                    board[i[0]] = '.'
                else:
                    print('invalid10')
            if board[i[0]] == 'M':
                if i[0] >= 0 and i[0] <= 31:
                    board[i[1]] = 'M'
                    board[i[0]] = '.'

        if current == 'b':
            if board[i[0]] == 'b':
                if (i[0] in [24, 25, 26, 27]) and (i[1] > i[0]):
                    board[i[1]] = 'B'
                    board[i[0]] = '.'
                elif i[0] >= 0 and i[0] <= 23:
                    board[i[1]] = 'b'
                    board[i[0]] = '.'
                else:
                    print('invalid')
            if board[i[0]] == 'B':
                if i[0] >= 0 and i[0] <= 31:
                    board[i[1]] = 'B'
                    board[i[0]] ='.'

    def after_double(current, i):
        if current == "m":
            if board[i[0]] == "m":
                if i[0] >= 12 and i[0] <= 31:
                    board[i[1]] = "m"
                    board[i[0]] = "."
                elif i[0] in [8, 9, 10, 11]:
                    board[i[1]] = "M"
                    board[i[0]] = "."
                else:
                    print("invalid11")
            if board[i[0]] == "M":
                board[i[1]] = "M"
                board[i[0]] = "."
        if current == "b":
            if board[i[0]] == "b":
                if i[0] >= 0 and i[0] <= 19:
                    board[i[1]] = "b"
                    board[i[0]] = "."
                elif i[0] in [20, 21, 22, 23]:
                    board[i[1]] = "B"
                    board[i[0]] = "."
                else:
                    print("invalid12")
            if board[i[0]] == "B":
                board[i[1]] = "B"
                board[i[0]] = "."
        remove_in_middle(current, i)

    def after_multiple(current, i):
        x = board[i[0]]
        board[i[-1]] = x
        board[i[0]] = '.'
        split = []
        for index in range(0, len(i) - 1):
            splits = []
            for index1 in range(1, len(i)):
                a = i[index]
                b = i[index + 1]
            splits.append(a)
            splits.append(b)
            split.append(splits)
        for a in split:
            remove_in_middle(current, a)

    def remove_in_middle(current, i):
        if i[0] in [28, 29, 30, 31]:
            if i[1] == i[0] - 7:
                board[i[0] - 4] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = '.'
            else:
                print('Invalid13')
        elif i[0] in [24, 25, 26, 27]:
            if i[1] == i[0] - 7:
                board[i[0] - 3] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 4] = '.'
            else:
                print('Invalid14')
        elif i[0] in [20, 21, 22, 23]:
            
            if i[1] == i[0] - 7:
                board[i[0] - 4] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = '.'
            elif i[1] == i[0] + 7:
                board[i[0] + 3] = '.'
            elif i[1] == i[0] + 9:
                board[i[0] + 4] = '.'
            else:
                print('Invalid15')
        elif i[0] in [16, 17, 18, 19]:
            if i[1] == i[0] + 9:
                board[i[0] + 5] = '.'
            elif i[1] == i[0] + 7:
                board[i[0] + 4] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 4] = '.'
            elif i[1] == i[0] - 7:
                board[i[0] - 3] = '.'
            else:
                print('Invalid16')
        elif i[0] in [12,13,14,15]:
            if i[1] == i[0] + 9:
                board[i[0] + 4] = '.'
            elif i[1] == i[0] + 7:
                board[i[0] + 3] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 5] = '.'
            elif i[1] == i[0] - 7:
                board[i[0] - 4] = '.'
            else:
                print('Invalid17')
        elif i[0] in [8,9,10,11]:
            if i[1] == i[0] + 9:
                board[i[0] + 5]='.'
            elif i[1] == i[0] + 7:
                board[i[0]+4] = '.'
            elif i[1] == i[0] - 9:
                board[i[0] - 4] = '.'
            elif i[1] == i[0] - 7:
                board[i[0] - 3] = '.'
            else:
                print('Invalid18')
        elif i[0] in [4,5,6,7]:
            if i[1] == i[0] + 7:
                board[i[0] + 3] = '.'
            elif i[1] == i[0] + 9:
                board[i[0] + 4] = '.'
            else:
                print('Invalid19')
        elif i[0] in [0,1,2,3]:
            if i[1] == i[0] + 7:
                board[i[0] + 4] = '.'
            elif i[1] == i[0] + 9:
                board[i[0] + 5]='.'
            else:
                print('Invalid20')
        else:
            print('invalid21')
    after_checker(board,movements)
    after_board=board
    list2=convert(after_board)
    print("list2",list2)
    display_boards(screen,list1, list2)
def screen2():
    import tkinter as tk

    def get_input_count():
        try:
            count = int(input_count_entry.get())
            if count > 0:
                create_input_entries(count)
            else:
                error_label.config(text="Please enter a valid count.")
        except ValueError:
             error_label.config(text="Please enter a valid number.")

    def create_input_entries(count):


        for i in range(count):
             entry_label = tk.Label(input_entries_frame, text=f"Enter Input {i + 1}:")
             entry_label.grid(row=i, column=0, padx=5, pady=5)

             entry =tk.Entry(input_entries_frame)
             entry.grid(row=i, column=1, padx=5, pady=5)
             input_entries.append(entry)

    # Additional input for the player's name
        player_label = tk.Label(input_entries_frame, text="Enter Player Name:")
        player_label.grid(row=count, column=0, padx=5, pady=5)

        player_entry = tk.Entry(input_entries_frame)
        player_entry.grid(row=count, column=1, padx=5, pady=5)
        input_entries.append(player_entry)

     
# Create the main window
    root = tk.Tk()
    root.title("Input Collection")

# First step: Enter the number of inputs
    input_count_label = tk.Label(root, text="Enter the number of inputs:")
    input_count_label.pack(pady=10)

    input_count_entry = tk.Entry(root)
    input_count_entry.pack(pady=5)

    submit_count_button = tk.Button(root, text="Submit", command=get_input_count)
    submit_count_button.pack(pady=5)
    input_entries_frame = tk.Frame(root)
    input_entries_frame.pack(pady=20)
    input_entries = []
    error_label = tk.Label(root, fg="red")
    error_label.pack()
    def submit_inputs():
        inputs = [entry.get() for entry in input_entries]
        print(inputs)
        screen3(inputs)
    submit_inputs_button = tk.Button(root, text="Submit Inputs", command=submit_inputs)
    submit_inputs_button.pack()
    root.mainloop()
def screen1():
    import pygame
    import tkinter as tk
    import tkinter.font as font
    window =tk.Tk()
    myfont = font.Font(family='Monaco', weight='bold')


    image_path =r"C:\Users\keert\source\repos\Checks post facto\check.png"
    bg_image = tk.PhotoImage(file=image_path)
    label = tk.Label(window, image=bg_image)
    label.place(x=0, y=0)
    


    # initiating pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\Users\keert\source\repos\Checks post facto\music.mp3")
    pygame.mixer.music.play()

    class mywindow:
        def __init__(self, win):
            self.b1 = tk.Button(win, text="Start ", bg="black", fg="white", command=self.start)
            self.b2 = tk.Button(win, text=" Quit ", bg="black", fg="white", command=window.quit)
            self.b3 = tk.Button(win, text="Music:ON ", bg="black", fg="white", command=self.play_sound)
            self.b4 = tk.Button(win, text="Music:OFF", bg="black", fg='white', command=self.stop_sound)
            self.b1.place(x=100, y=500)
            self.b2.place(x=200, y=500)
            self.b3.place(x=100, y=540)
            self.b4.place(x=200, y=540)
            self.b1['font'] = myfont
            self.b2['font'] = myfont
            self.b3['font'] = myfont
            self.b4['font'] = myfont

        def start(self):
            screen2()
        def play_sound(self):
            pygame.mixer.music.load(r"music.mp3")
            pygame.mixer.music.play()

        def stop_sound(self):
            pygame.mixer.music.stop()

    win = mywindow(window)
    window.title("checks post facto")
    window.geometry("800x600+30+30")
    window.mainloop()

screen1()

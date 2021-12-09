import re
bingo_directions = []
bingo_boards = []

with open('day4_input.txt') as f:
    text = f.read()
    bingo_directions = text.split('\n')[0].split(',')
    bingo_boards_intermediate = [line.split('\n') for line in text.split('\n\n')[1:]]
    for row in bingo_boards_intermediate:
        bingo_boards.append([line.strip().split(' ') for line in row])
   

            
#print(bingo_directions)
#print(bingo_boards)
#print(bingo_boards[0][2][0])

# cleaning up white space
for board in bingo_boards:
    for row in board:
        try:
            while True:
                row.remove('')
        except ValueError:
            pass
       

# keep track of called numbers and boards
# part 1
bingo_tracking = {}

def get_bingo_stuff(bingo_directions, bingo_boards):                            
    for called_number in bingo_directions:
        for board_index, board in enumerate(bingo_boards):
            for row_index, row in enumerate(board):
                for col_index, col in enumerate(row):
                    if col == called_number:
                        if board_index in bingo_tracking:
                            bingo_tracking[board_index].append((called_number, row_index, col_index))
                        else:
                            bingo_tracking[board_index] = [(called_number, row_index, col_index)]
                        
                        for board_i, values in bingo_tracking.items():
                            row_dict = {}
                            col_dict = {}
                            for num, row_i, col_i in values:
                                if row_i in row_dict:
                                    row_dict[row_i].append(col_i)
                                else:
                                    row_dict[row_i] = [col_i]
                                if col_i in col_dict:
                                    col_dict[col_i].append(row_i)
                                else:
                                    col_dict[col_i] = [row_i]
                                
                                if len(row_dict[row_i]) > 4 or len(col_dict[col_i]) > 4:
                                    sum_of_unmarked = 0
                                    for row_i, row in enumerate(bingo_boards[board_i]):
                                        for col_i, col in enumerate(row):
                                            if (col, row_i, col_i) not in bingo_tracking[board_i]:
                                                sum_of_unmarked += int(col)
                                            else:
                                                continue
                                    
                                    return int(called_number) * sum_of_unmarked
            
print(get_bingo_stuff(bingo_directions, bingo_boards))

# part 2
bingo_tracking = {}
# track every bingo winner for the entire game, and then just check the last one
bingo_winners = {}

def get_bingo_stuff(bingo_directions, bingo_boards):                            
    for called_number in bingo_directions:
        for board_index, board in enumerate(bingo_boards):
            for row_index, row in enumerate(board):
                for col_index, col in enumerate(row):
                    if col == called_number:
                        if board_index in bingo_tracking:
                            bingo_tracking[board_index].append((called_number, row_index, col_index))
                        else:
                            bingo_tracking[board_index] = [(called_number, row_index, col_index)]
                        
                        for board_i, values in bingo_tracking.items():
                            row_dict = {}
                            col_dict = {}
                            for num, row_i, col_i in values:
                                if row_i in row_dict:
                                    row_dict[row_i].append(col_i)
                                else:
                                    row_dict[row_i] = [col_i]
                                if col_i in col_dict:
                                    col_dict[col_i].append(row_i)
                                else:
                                    col_dict[col_i] = [row_i]
                                
                                if (len(row_dict[row_i]) > 4 or len(col_dict[col_i]) > 4) and board_i not in bingo_winners:
                                    sum_of_unmarked = 0
                                    for row_i, row in enumerate(bingo_boards[board_i]):
                                        for col_i, col in enumerate(row):
                                            if (col, row_i, col_i) not in bingo_tracking[board_i]:
                                                sum_of_unmarked += int(col)
                                            else:
                                                continue
                                    bingo_winners[board_i] = int(called_number) * sum_of_unmarked


get_bingo_stuff(bingo_directions, bingo_boards)
print(bingo_winners)
def leaderboard_sort(leaderboard, changes):
    lb = leaderboard.copy()
    for x in changes:
        holder = x.split(' ')
        target = holder[0]
        mv = holder[1]
        moves = int(mv[-1])
        direction = mv[0]
        for i in range(moves):
            t = lb.index(target)
            if direction == "+":
                lb[t-1], lb[t] = lb[t], lb[t-1]
            if direction == "-":
                lb[t], lb[t+1] = lb[t+1], lb[t]

    return lb

        
# Itterate over the changes list 
# Split changes list string allong the " "  
# Find the target in the leaderboard list
# def move_up def move_down based on + or - in string
# for x in range(last number of changes string)

    



leaderboard_sort(['John', 'Brian', 'Jim', 'Dave', 'Fred'], ['Dave +1', 'Fred +4', 'Brian -1'])
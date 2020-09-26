# ///// THE LONG SOLUTION

# def beggars(values, n):
#     v = values.copy()
#     if n == 0: return []
#     else:
#         earnings = [0]*n
#         while len(v) > 0:
#             beggar = n
#             count = 0
#             while beggar > 0 and len(v) > 0:
#                 earnings[count] = earnings[count] + v[0]
#                 v.pop(0)
#                 beggar -= 1
#                 count += 1
#     return earnings


#//// A MUCH SIMPLER SOLUTION 
def beggars(values, n):
    result = []
    for i in range(n):
        result.append(sum(values[i::n]))
    return result    


# # //// SHORTEST SOLUTION but not as easy to read


# def beggars(values, n):
#     return [sum(values[i::n]) for i in range(n)]

#    some extra code will go down here

print(beggars([11,2,3,4,5,3,2,1,1,1,7,2],4))

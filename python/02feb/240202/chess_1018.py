
'''
어케하지... 답도없네
1. 진짜 체스판 구현 2가지 종류 다
2. input값으로 만드는 체스판이랑 같은지 비교 -> 어케함?
3. 왼쪽 위 인덱스를 기준으로 반복문돌려서 같은지 비교? -> 될거 같기도 하고
3-1 -> for문 두개 돌려서 왼쪽위 인덱스 기준으로 다 돌림 -> 범위 잘잡아야지 out of range안뜰듯
3-2 -> 기준 잡은 왼쪽위 인덱스부터 8x8만큼의 for문 다시 돌림 -> 각각을 진짜 체스판과 비교해서 다르면 cnt에 1씩 추가
4. 하나당 두개의 진짜 체스판과 비교해서 cnt가 더 작은걸로 fix
5. 3-1로 다 돌린것들 비교
'''

import pprint

n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

# pprint.pprint(board)

# 원래 체스판 구현
chess_1 = ['B', 'W'] * 5
chess_2 = ['W', 'B'] * 5

# 체스판 ver1
chess_board_1 = [chess_1, chess_2] * 4

# 체스판 ver2
chess_board_2 = [chess_2, chess_1] * 4

# pprint.pprint(chess_board_1)
# pprint.pprint(chess_board_2)

def chess_comparison(real_chess, input_board, n, m):

    cnt_ls = []
    # 실제 체스판의 크기가 8이므로 n-8+1만큼 돌림
    for row in range(n-8+1):
        # 실제 체스판의 크기가 8이므로 m-8+1만큼 돌림
        for col in range(m-8+1):
            # 기준은 board[row][col]임

            # 몇개 고쳐야할지 셀 변수
            cnt = 0

            # 다시 여기서 부터 for문으로 기준잡은곳 부터 비교
            for i in range(8):
                for j in range(8):
                    if input_board[row+i][col+j] != real_chess[i][j]:
                        cnt += 1

            cnt_ls.append(cnt)

    return cnt_ls

# print(chess_comparison(chess_board_1, board, n, m))
# print(chess_comparison(chess_board_2, board, n, m))

chess_board_1_min = min(chess_comparison(chess_board_1, board, n, m))
chess_board_2_min = min(chess_comparison(chess_board_2, board, n, m))

# 최종 제일 작은 값
print(min(chess_board_1_min, chess_board_2_min))

import random

class Mine:
    def __init__(self, width, height, mine_count):
        self.width = width
        self.height = height
        self.mine_count = mine_count

    # 마인의 좌표인 (x, y)가 모여 있는 리스트 만들어주는 함수
    def create_mine_list(self):
        mine_list = []
        # 지뢰 랜덤 생성
        for i in range(self.mine_count):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            # print('x : ', x, '/ y : ', y)

            # 지뢰 위치가 중복되지 않도록 처리하는 로직
            for j in range(len(mine_list)):
                while (x == mine_list[j][0]) and (y == mine_list[j][1]):
                    x = random.randint(0, self.width - 1)  ## 인덱스 (0부터 시작)
                    y = random.randint(0, self.height - 1)  ## 인덱스 (0부터 시작)

            # 중복되지 않는 경우 mine_list에 지뢰 위치를 나타내는 (x, y)를 추가
            mine_list.append((x, y))

        return mine_list

    # mine_count_nearby_button_double_list를 width, height만큼 버튼들을 이중리스트로 생성
    def create_mine_count_nearby_button_double_list(self, mine_list):
        mine_count_nearby_button_double_list = []  # 버튼 주변에 있는 지뢰의 개수를 모아놓은 이중 리스트

        for j in range(self.height):
            # temp_row = []
            # for i in range(self.width):
            #     temp_row.append(0)
            #     mine_count_nearby_button_double_list.append(temp_row)
            mine_count_nearby_button_double_list.append([0] * self.width)



        # 버튼 주변에 위치한 지뢰 개수를 표현해주는 이중 리스트 만들기
        for i in range(len(mine_list)):
            x = mine_list[i][0]
            y = mine_list[i][1]

            # 지뢰를 기준으로 주변 면에 벽이 없는 경우
            if x == 0:
                # print('테스트1 : ', x, ',', y)
                # mine_count_nearby_button_double_list[y][x - 1] += 1
                mine_count_nearby_button_double_list[y][x + 1] += 1
                if y == 0:
                    # mine_count_nearby_button_double_list[y + 1][x - 1] += 1
                    mine_count_nearby_button_double_list[y + 1][x + 1] += 1
                    mine_count_nearby_button_double_list[y + 1][x] += 1
                elif y == self.height - 1:
                    # mine_count_nearby_button_double_list[y - 1][x - 1] += 1
                    mine_count_nearby_button_double_list[y - 1][x + 1] += 1
                    mine_count_nearby_button_double_list[y - 1][x] += 1
                else:
                    mine_count_nearby_button_double_list[y + 1][x + 1] += 1
                    mine_count_nearby_button_double_list[y + 1][x] += 1
                    mine_count_nearby_button_double_list[y - 1][x + 1] += 1
                    mine_count_nearby_button_double_list[y - 1][x] += 1

            elif x == self.width - 1:
                # print('테스트2 : ', x, ',', y)
                mine_count_nearby_button_double_list[y][x - 1] += 1
                # mine_count_nearby_button_double_list[y][x + 1] += 1
                if y == 0:
                    mine_count_nearby_button_double_list[y + 1][x - 1] += 1
                    # mine_count_nearby_button_double_list[y + 1][x + 1] += 1
                    mine_count_nearby_button_double_list[y + 1][x] += 1

                elif y == self.height - 1:
                    mine_count_nearby_button_double_list[y - 1][x - 1] += 1
                    # mine_count_nearby_button_double_list[y - 1][x + 1] += 1
                    mine_count_nearby_button_double_list[y - 1][x] += 1

                else:
                    mine_count_nearby_button_double_list[y + 1][x - 1] += 1
                    mine_count_nearby_button_double_list[y + 1][x] += 1
                    mine_count_nearby_button_double_list[y - 1][x - 1] += 1
                    mine_count_nearby_button_double_list[y - 1][x] += 1

            elif 0 < x < self.width - 1:
                # print('테스트3 : ', x, ',', y)
                mine_count_nearby_button_double_list[y][x - 1] += 1
                mine_count_nearby_button_double_list[y][x + 1] += 1
                if y == 0:
                    mine_count_nearby_button_double_list[y + 1][x - 1] += 1
                    mine_count_nearby_button_double_list[y + 1][x + 1] += 1
                    mine_count_nearby_button_double_list[y + 1][x] += 1

                elif y == self.height - 1:
                    mine_count_nearby_button_double_list[y - 1][x - 1] += 1
                    mine_count_nearby_button_double_list[y - 1][x + 1] += 1
                    mine_count_nearby_button_double_list[y - 1][x] += 1

                else:
                    mine_count_nearby_button_double_list[y + 1][x - 1] += 1
                    mine_count_nearby_button_double_list[y + 1][x + 1] += 1
                    mine_count_nearby_button_double_list[y + 1][x] += 1
                    mine_count_nearby_button_double_list[y - 1][x - 1] += 1
                    mine_count_nearby_button_double_list[y - 1][x + 1] += 1
                    mine_count_nearby_button_double_list[y - 1][x] += 1


        for i in range(len(mine_list)):
            # print(len(mine_list))
            # print('마인리스트 : ', mine_list)
            # print('mine_count_nearby_button_double_list', mine_count_nearby_button_double_list)
            x = mine_list[i][0]
            y = mine_list[i][1]
            # print('테스트 : ', mine_count_nearby_button_double_list[y])
            # print('테스트2 : ', mine_count_nearby_button_double_list[y][x])
            mine_count_nearby_button_double_list[y][x] = '지뢰'

        return mine_count_nearby_button_double_list


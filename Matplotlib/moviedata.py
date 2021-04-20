# import re
# import pandas as pd
# from collections import deque

# movie = "TITANIC" #영화 이름 및 txt파일명
# character = "JACK" #분석 캐릭터 이름
# source_file = f"./script/{movie}.txt" 

# def make_list(filename, character):
#     user_to_titles = []

#     with open(filename) as file:
#         for line in file:

#             user_to_titles.append(line)

#     # print(user_to_titles)

#     dq = deque(user_to_titles)
#     script_data = ""
#     sett = []
#     while dq:
#         e = dq.popleft()
#         p = re.compile(character+"\n$")
#         if p.search(e) != None:

#             while dq:
#                 script = dq.popleft().lstrip()
#                 # sett.append(script)
#                 if re.fullmatch(re.escape(script), '') != None:
#                     break
#                 else:
#                     text = script.lstrip().replace('\n','')
#                     if re.search('\)', text) == None and re.match('^[0-9]*.$',text) == None:
#                         script_data += text + " "

#     print(script_data)
#     dct = {character: script_data}

#     df = pd.DataFrame(dct, index = [0])

#     df.to_csv(f"{movie}_{character}.csv", mode='a', header=False)

#     return script_data

# print(make_list(source_file, character))

## v.01

import re
import pandas as pd
from collections import deque

movie = "TITANIC" #영화 이름 및 txt파일명
character = "JACK" #분석 캐릭터 이름
source_file = f"./script/{movie}.txt" 

def make_list(filename, character):
    user_to_titles = []

    with open(filename) as file:
        for line in file:

            user_to_titles.append(line)

    # print(user_to_titles)

    dq = deque(user_to_titles)
    script_data = ""
    sett = []
    while dq:
        e = dq.popleft()
        p = re.compile(character+"\n$")
        if p.search(e) != None:
            # print("e:", e)
            while dq:
                script = dq.popleft()
                sett.append(script)
                # print(script)
                if re.fullmatch(script, '\n') != None:
                    break
                # else:
                #     text = script.replace('\n','')
                #     print("text:", text)
                #     # print("text", script)
                #     if re.search('\)', text) == None and re.match('^[0-9]*.$',text) == None:
                #         script_data += text + " "
    print(sett)
    # print(script_data)
    dct = {character: script_data}

    df = pd.DataFrame(dct, index = [0])

    df.to_csv(f"{movie}_{character}.csv", mode='a', header=False)

    # return script_data

print(make_list(source_file, character))



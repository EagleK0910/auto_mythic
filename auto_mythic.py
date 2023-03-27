import yaml
import zhconv
import sys
import time
import datetime
import logging
import os

log_dir = "log"
log_file = os.path.join(log_dir, "auto_mythic_{}.log".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))

if not os.path.isdir(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(format='%(asctime)s %(message)s', filename='auto_mythic.log', level=logging.DEBUG, encoding='utf-8')

zh_tw_data = {}
en_us_data = {}

class SingleQuoted(str):
    pass

def single_quoted_presenter(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="'")

yaml.add_representer(SingleQuoted, single_quoted_presenter)

while True:
    lang = input("請選擇語言\nPlease select a language\n(1) zh_tw(繁體中文)\n(2) en_us(美式英語)\n>>> ")

    #中文系統
    if lang == "1":

        #選擇怪物或是物品
        while True:
            user_input = input("請問要製作哪一個項目\n可以輸入以下選項\n括號內的選一個輸入即可\n怪物: (1、怪物、m、mobs)\n物品: (2、物品、i、items)\n取消: (-)\n>>> ")
            if user_input == "-":
                print("3秒後自動停止程式.")
                time.sleep(1)
                print("2秒後自動停止程式..")
                time.sleep(1)
                print("1秒後自動停止程式...")
                time.sleep(1)
                sys.exit()
            elif user_input.lower() in ["1","怪物","m", "mobs","2", "物品","i", "items"]:
                break
            else:
                print("請輸入正確的選項")

        #輸入&輸出
        if user_input.lower() in ["1", "怪物", "m", "mobs"]:
            input("使用說明(格式):\n\n怪物ID:\n  Display: '怪物顯示名稱'\n  Type: 怪物類型\n  Health: 怪物生命值\n  Damage:  怪物攻擊力\n  Armor:  怪物防禦值\n\n(最終檔案格式會依照英文字母順序自動排列)\n\n按Enter鍵繼續...")
            monster_name = input("請輸入怪物ID\n>>> ")
            display_name = input("請輸入怪物顯示名稱\n可以輸入16進制色碼或是顏色代號\n例如: <#FF00FF>怪物測試 or &d怪物測試\n>>> ")
            monster_type = input("請輸入怪物類型\n例如: ZOMBIE(殭屍)\n>>> ")
            monster_health = input("請輸入怪物生命值\n請輸入數字\n>>> ")
            monster_damage = input("請輸入怪物攻擊力\n請輸入數字\n>>> ")
            monster_armor = input("請輸入怪物防禦值\n請輸入數字\n>>> ")
            if display_name != "-":
                display_name = SingleQuoted(display_name)
            zh_tw_data[str(monster_name)] = {"Type": str(zhconv.convert(monster_type, 'en-us')), 
                                "Display": display_name, 
                                "Health": int(zhconv.convert(monster_health, 'en-us')), 
                                "Damage": int(zhconv.convert(monster_damage, 'en-us')),
                                "Armor": int(zhconv.convert(monster_armor, 'en-us'))}

        elif user_input.lower() in ["2", "物品","i", "items"]:
            input("使用說明(格式):\n\n物品ID:\n  Display: '物品顯示名稱'\n  Model: Model值 \n  Type: 物品類型\n  Health: 物品生命值\n  Damage:  物品攻擊力\n\n(最終檔案格式會依照英文字母順序自動排列)\n\n按Enter鍵繼續...")
            item_name = input("請輸入物品id\n>>> ")
            display_name = input("請輸入物品顯示名稱\n可以輸入16進制色碼\n例如: <#FF00FF>物品測試\n>>> ")
            model_value = input("請輸入Model值\n請輸入數字\n>>> ")
            item_type = input("請輸入物品類型\n>>> ")
            item_health = input("請輸入物品生命值\n請輸入數字\n>>> ")
            item_damage = input("請輸入物品攻擊力\n請輸入數字\n>>> ")
            if display_name != "-":
                display_name = SingleQuoted(display_name)
            zh_tw_data[str(item_name)] = {"Type": str(zhconv.convert(item_type, 'zh-tw')), 
                            "Display": display_name, 
                            "Model": int(zhconv.convert(model_value, 'zh-tw')), 
                            "Health": int(zhconv.convert(item_health, 'zh-tw')), 
                            "Damage": int(zhconv.convert(item_damage, 'zh-tw'))}

        #最確認並打包成yml檔進行輸出
        while True:
            output = yaml.dump(zh_tw_data, allow_unicode=True)
            Confirmation = input("——————————\n" + output + "——————————\n確認以上資料確認是否要輸出檔案\n輸入(y)將會進行下一步\n輸入(n)將會自動刪除紀錄並停止程序\n>>> ")
            if Confirmation.lower() == "y":
                file_name = input("請輸入檔案名稱：\n不須輸入副檔名(.yml)\n>>> ")
                with open(f"{file_name}.yml", "w", encoding="utf-8") as f:
                    yaml.dump(zh_tw_data, f, allow_unicode=True)
                
                while True:
                    usage = input("檔案已成功生成! (" + file_name + ".yml)\n若需要查閱使用方式請輸入(y)\n若不需要查閱請輸入(n)\n>>> ")
                    if usage.lower() == "y" and user_input.lower() in ["1", "怪物", "m", "mobs"]:
                        print("使用方式:\n\n1. 將生成出來的檔案放進'Plugins/MythicMobs/Mobs'\n2. 在控制台輸入'/mm reload'\n3. 進入遊戲後輸入'/mm egg get " + monster_name + "'\n即可獲取你所製作的怪物蛋\n")
                        input("點擊Entar鍵關閉視窗...")
                        sys.exit()

                    elif usage.lower() == "y" and user_input.lower() in ["2", "物品","i", "items"]:
                        print("使用方式:\n\n1. 將生成出來的檔案放進'Plugins/MythicMobs/Items'\n2. 在控制台輸入'/mm reload'\n3. 進入遊戲後輸入'/mm item get " + item_name + "'\n即可獲取你所製作的物品\n")
                        input("點擊Entar鍵關閉視窗...")
                        sys.exit()

                    elif usage.lower() == "n":
                        sys.exit()

                    else:
                        print("請輸入y或是n")

            elif Confirmation.lower() == "n" and user_input.lower() in ["1", "怪物", "m", "mobs"]:
                print("即將關閉程式，並生成日誌 (auto_mythic.log)")
                logging.debug('\n\n以下是你所設定的所有資料\n\n怪物的ID: ' + monster_name + '\n怪物名字: ' + display_name)
                time.sleep(3)
                sys.exit()

            elif Confirmation.lower() == "n" and user_input.lower() in ["2", "物品","i", "items"]:
                print("即將關閉程式，並生成日誌 (auto_mythic.log)")
                logging.debug('\n\n以下是你所設定的所有資料\n\n物品的ID: ' + monster_name + '\n物品名字: ' + display_name)
                time.sleep(3)
                sys.exit()

            else:
                print("請輸入y或是n")

    #英文系統
    elif lang == "2":
        #選擇怪物或是物品
        print("123")
    #過濾垃圾訊息
    else:
        print("請選擇正確的語言\nPlease select the correct language")
import yaml
import zhconv
import sys
import time

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
            input("使用說明(格式):\n\n怪物ID:\n  Display: '怪物顯示名稱'\n  Type: 怪物類型\n  Health: 怪物生命值\n  Damage:  怪物攻擊力\n\n(最終檔案格式會依照英文字母順序自動排列)\n\n按Enter鍵繼續...")
            monster_name = input("請輸入怪物ID\n>>> ")
            display_name = input("請輸入怪物顯示名稱\n可以輸入16進制色碼或是顏色代號\n例如: <#FF00FF>怪物測試 or &d怪物測試\n>>> ")
            monster_type = input("請輸入怪物類型\n例如: ZOMBIE(殭屍)\n>>> ")
            monster_health = input("請輸入怪物生命值\n請輸入數字\n>>> ")
            monster_damage = input("請輸入怪物攻擊力\n請輸入數字\n>>> ")
            if display_name != "-":
                display_name = SingleQuoted(display_name)
            zh_tw_data[str(monster_name)] = {"Type": str(zhconv.convert(monster_type, 'zh-tw')), 
                                "Display": display_name, 
                                "Health": int(zhconv.convert(monster_health, 'zh-tw')), 
                                "Damage": int(zhconv.convert(monster_damage, 'zh-tw'))}
        elif user_input.lower() in ["2", "物品","i", "items"]:
            item_name = input("請輸入物品id\n>>> ")
            display_name = input("請輸入物品顯示名稱\n可以輸入16進制色碼\n例如: <#FF00FF>物品測試\n>>> ")
            model_value = input("請輸入Model值\n>>> ")
            item_type = input("請輸入物品類型\n>>> ")
            item_health = input("請輸入物品生命值\n>>> ")
            item_damage = input("請輸入物品攻擊力\n>>> ")
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
                    usage = input("檔案已成功生成! " + file_name + "\n若需要查閱使用方式請輸入(y)\n若不需要查閱請輸入(n)\n>>> ")
                    if usage.lower() == "y" and user_input.lower() in ["1", "怪物", "m", "mobs"]:
                        print("使用方式:\n\n請將生成出來的檔案放進'Plugins/MythicMobs/Mobs'\n在控制台輸入'/mm reload'\n進入遊戲後輸入'/mm egg get " + monster_name + "'\n即可獲取你所製作的怪物蛋\n")
                        input("點擊Entar鍵關閉視窗...")
                        sys.exit()

                    elif usage.lower() == "y" and user_input.lower() in ["2", "物品","i", "items"]:
                        print("使用方式:\n\n請將生成出來的檔案放進'Plugins/MythicMobs/Items'\n在控制台輸入'/mm reload'\n進入遊戲後輸入'/mm item get " + monster_name + "'\n即可獲取你所製作的物品\n")
                        input("點擊Entar鍵關閉視窗...")
                        sys.exit()

                    elif usage.lower() == "n":
                        sys.exit()

                    else:
                        print("請輸入y或是n")

            elif Confirmation.lower() == "n":
                print("即將關閉程式")
                time.sleep(3)
                sys.exit()

            else:
                print("請輸入y或是n")

    #英文系統
    elif lang == "2":
        #選擇怪物或是物品
        while True:
            user_input = input("Which project do you want to produce?\nYou can enter the following options\nSelect one of the brackets to enter\nmobs: (1、m、mobs)\nitems: (2、i、items)\nCancellation: (-)\n>>> ")
            if user_input == "-":
                print("Auto-stop program after 3 seconds...")
                time.sleep(1)
                print("Auto-stop program after 2 seconds..")
                time.sleep(1)
                print("Auto-stop program after 1 seconds.")
                time.sleep(1)
                sys.exit()
            elif user_input.lower() in ["1","m", "mobs","2","i", "items"]:
                break
            else:
                print("Please enter the correct option")

        #輸入&輸出
        if user_input.lower() in ["1", "m", "mobs"]:
            monster_name = input("請輸入怪物ID\n>>> ")
            display_name = input("請輸入物品顯示名稱\n可以輸入16進制色碼或是顏色代號\n例如: <#FF00FF>物品測試 or &d物品測試\n>>> ")
            monster_type = input("請輸入怪物類型\n例如: ZOMBIE(殭屍)\n>>> ")
            monster_health = input("請輸入怪物生命值\n\n>>> ")
            monster_damage = input("請輸入怪物攻擊力\n>>> ")
            if display_name != "-":
                display_name = SingleQuoted(display_name)
            en_us_data[int(monster_name)] = {"Type": int(zhconv.convert(monster_type, 'zh-tw')), 
                                "Display": display_name, 
                                "Health": int(zhconv.convert(monster_health, 'zh-tw')), 
                                "Damage": int(zhconv.convert(monster_damage, 'zh-tw'))}
        elif user_input.lower() in ["2","i", "items"]:
            item_name = input("請輸入物品id\n>>> ")
            display_name = input("請輸入物品顯示名稱\n可以輸入16進制色碼\n例如: <#FF00FF>物品測試\n>>> ")
            model_value = input("請輸入Model值\n>>> ")
            item_type = input("請輸入物品類型\n>>> ")
            item_health = input("請輸入物品生命值\n>>> ")
            item_damage = input("請輸入物品攻擊力\n>>> ")
            if display_name != "-":
                display_name = SingleQuoted(display_name)
            en_us_data[int(item_name)] = {"Type": int(zhconv.convert(item_type, 'zh-tw')), 
                            "Display": display_name, 
                            "Model": int(zhconv.convert(model_value, 'zh-tw')), 
                            "Health": int(zhconv.convert(item_health, 'zh-tw')), 
                            "Damage": int(zhconv.convert(item_damage, 'zh-tw'))}

        # 修改 Display
        en_us_new_data = {}
        for k, v in en_us_data.items():
            new_v = {}
            for kk, vv in v.items():
                if kk == "Display":
                    new_v[kk] = vv
                else:
                    new_v[kk] = int(vv)
            en_us_new_data[k] = new_v

        #最確認並打包成yml檔進行輸出
        while True:
            output = yaml.dump(en_us_new_data, allow_unicode=True)
            Confirmation = input("——————————\n" + output + "——————————\nCheck the above information to confirm if you want to export the file\nEnter (y) will proceed to the next step\nEnter(n) will automatically delete the record and stop the program\n>>> ")
            if Confirmation.lower() == "y":
                file_name = input("Please enter the file name：\nNo need to enter a secondary file name(.yml)\n>>> ")
                with open(f"{file_name}.yml", "w", encoding="utf-8") as f:
                    yaml.dump(en_us_new_data, f, allow_unicode=True)
                sys.exit()

            elif Confirmation.lower() == "n":
                print("Will close the program")
                time.sleep(3)
                break

            else:
                print("Please enter y or n")

    #過濾垃圾訊息
    else:
        print("請選擇正確的語言\nPlease select the correct language")
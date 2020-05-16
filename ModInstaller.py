# import webbrowser as wb
# import os
# import time


# #https://aternos.org/addons/a/curseforge/bubble-column-elevator-backport
# #https://aternos.org/addons/list/1/Simple%20Void%20World
# #https://aternos.org/addons/a/curseforge/simple-void-world

# def main():
#     # return
#     direct = 'C:/Users/KOT32500/AppData/Roaming/.minecraft/Mods'
#     Mods = os.listdir(direct)
#     for Mod in Mods:
#         SplitSimvol = [".",",","/","-","_"]
#         ModSplit = Mod
#         for Simvol in SplitSimvol:
#             ModSplit = ModSplit.split(Simvol)[0]
#         Cannot = ["1",' ','[',']','[1']
#         if ModSplit not in Cannot:
#             #curseforge
#             ModSplitEpmpty = ModSplit
#             aternos = f"https://aternos.org/addons/list/1/{ModSplit}"
#             wb.register('Chrome', None, wb.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
#             wb.get('Chrome').open_new_tab(f'{aternos}')
#             time.sleep(20)
            



# if __name__ == "__main__":
#     main()
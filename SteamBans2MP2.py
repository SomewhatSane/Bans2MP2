import os

print('SteamBans2MP2 - by SomewhatSane\n')

bansConverted = 0
successOldLoad = True
while successOldLoad:
    bansFile = input('Please insert the file name of your old MP1 SteamIdBans.txt (include the file extension!): ')

    try:
        oldBans = open(bansFile, "r", encoding='cp850')
        successOldLoad = False

    except:
        print("I can't seem to be able to open " + bansFile + ". Please make sure it exists and you have permission to read this file!")

print('Load success. Will output new file as UserIDBans.txt')
newBans = open('UserIDBans.txt', "a", encoding='cp850')

oldBansArray = oldBans.readlines()

for ban in oldBansArray:
    ban = ban.strip('\n') #Remove \n!
    print('Converting ' + ban + ' to new format..')

    currentBan = []
    currentBan = ban.split(';')
    #SteamID is 2nd piece!

    currentBan[1] = currentBan[1] + '@steam'
    newBanLine = ""

    for data in currentBan:
        if data == currentBan[-1]:
            newBanLine = newBanLine + data
        else:
            newBanLine = newBanLine + data + ';'

    newBanLine = newBanLine + '\n'
    try:
        newBans.write(newBanLine)
        print('Success')
        bansConverted = bansConverted + 1
    except:
        print('Fail trying to write to new bans file. Program closing.')
        break


print('\nSuccess. Converted ' + str(bansConverted) + ' bans to MP2 format.')

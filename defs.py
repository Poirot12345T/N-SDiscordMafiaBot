import time

accuseMessageDict = {}
cycletime = 24 #time of cycle in hours
firstDay = True

admin_room = #id of admin room
accuse_board = #id of board
command_room = #id of command room

def addAccuseList(messageList): #messageList == message.content.split(" ")
    who = messageList[1]
    reason = ""
    for i in range(2,(len(messageList))):
        reason = reason + messageList[i] + " "
    reason = reason[:len(reason)-1]
    return [who, reason]
    #returns a list

def send_message(messageContent,where): #where is predefined or an ID of a channel we want to reach 
    global admin_room
    global command_room
    global accuse_board
    if where == "admin":
        id = getId(admin_room)
    elif where == "command":
        id = getId(command_room)
    elif where == "accuselist":
        id = getId(accuse_board)
    else:
        try:
            id = getId(int(where))
        except ValueError:
            raise TypeError("channel not recognised")
    message.channel.send(messageContent)
    #returns void

def publishAccusion(accuselist, offender): #accuselist is returned from addAccuseList, offender is message.user
    who = accuselist[0]
    reason = accuselist[1]
    global accuseMessageDict
    for key in accuseMessageDict:
        if key == who:
            send_message("Whoops, this person was already accused.","command")
            alreadyAccused = True
    if not alreadyAccused:
        send_message("New accusion occured!\n" + who + " was accused by " + offender + " with reason:\n" + reason,"accuselist")
        messageId = get_last_message_id()
        accuseMessageDict.add(who,messageId)
        add_reaction(messageId)
    #retuns void
    
def resolveDay():
    global cycletime
    global firstDay
    global accuseMessageDict
    highestReaction = 0
    firstRun = True
    if not firstDay:
        for who in accuseMessageDict.keys():
            messageId = accuseMessageDict.who.value()
            reactionCount = get_reaction_count(messageId)
            if reactionCount > highestReaction:
                winner = [who, reactionCount]
                highestReaction = winner[1]
        for who in accuseMessageDict.keys():
            messageId = accuseMessageDict.who.value()
            reactionCount = get_reaction_count(messageId)
            if reactionCount == highestReaction:
                if firstRun:
                    send_message("There is not only one person who get the same result of " + str(highestReaction) + " votes:","admin")
                    firstRun = False
                send_message(who, "admin")
                draw = True
        if not draw:
            send_message(winner[0] + " won the voting with " + str(winner[1]) + " votes.","admin")
        accuseMessageDict = {}
        send_message("Wakey wakey rise and shine, good morning everyone! It's time to do some new accusions! The old ones were closed, it's no longer possible to influence them. Wait for game master to get the result.","accuselist")
    firstDay = False
    time.sleep(cycletime*3600)
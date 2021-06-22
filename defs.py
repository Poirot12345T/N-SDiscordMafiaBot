import time

accuse_message_dict = {}
cycletime = 24  # time of cycle in hours
first_day = True
admin_room = None  # id of admin room
accuse_board = None  # id of board
command_room = None  # id of command room


def add_accuse_list(message_list) -> list:  # message_list == message.content.split(" ")
    who = message_list[1]
    reason = ""
    for i in range(2, (len(message_list))):
        reason = reason + message_list[i] + " "
    reason = reason[:len(reason) - 1]
    return [who, reason]


def send_message(message_content, where):  # where is predefined or an ID of a channel we want to reach
    global admin_room
    global command_room
    global accuse_board
    if where == "admin":
        id = get_id(admin_room)
    elif where == "command":
        id = get_id(command_room)
    elif where == "accuselist":
        id = get_id(accuse_board)
    else:
        try:
            id = get_id(int(where))
        except ValueError:
            raise TypeError("channel not recognised")
    message.channel.send(message_content)


def publish_accusion(accuselist, offender):  # accuselist is returned from add_accuse_list, offender is message.user
    who = accuselist[0]
    reason = accuselist[1]
    global accuse_message_dict
    already_accused = True
    for key in accuse_message_dict:
        if key == who:
            send_message("Whoops, this person was already accused.", "command")
            already_accused = True
    if not already_accused:
        send_message("New accusion occured!" + who + " was accused by " + offender + " with reason:" + reason,
                     "accuselist")
        message_id = get_last_message_id()
        accuse_message_dict.add(who, message_id)
        add_reaction(message_id)


def resolve_day():
    global cycletime
    global first_day
    global accuse_message_dict
    highest_reaction = 0
    first_run = True
    if not first_day:
        for who in accuse_message_dict.keys():
            message_id = accuse_message_dict.who.value()
            reaction_count = get_reaction_count(message_id)
            if reaction_count > highest_reaction:
                winner = [who, reaction_count]
                highest_reaction = winner[1]
        for who in accuse_message_dict.keys():
            message_id = accuse_message_dict.who.value()
            reaction_count = get_reaction_count(message_id)
            if reaction_count == highest_reaction:
                if first_run:
                    send_message(
                        "_there is not only one person who get the same result of " + str(highest_reaction) + " votes:",
                        "admin")
                    first_run = False
                send_message(who, "admin")
                draw = True
        if not draw:
            send_message(winner[0] + " won the voting with " + str(winner[1]) + " votes.", "admin")
        accuse_message_dict = {}
        send_message(
            "Wakey wakey rise and shine, good morning everyone! Itt's time to do some new accusions! The old ones were closed, it's no longer possible to influence them. Wait for game master to get the result.",
            "accuselist")
    first_day = False
    time.sleep(cycletime * 3600)

from willie import module

@module.rule("^.*(\*sigh\*).*$")
def stop_sighing(bot, trigger):
        bot.say("You sound depressed " + trigger.nick + ". No one will blame you for giving up. In fact, quitting at this point is a perfectly reasonable response.")


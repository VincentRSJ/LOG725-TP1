from commands.command import Command


class MoveUpCommand(Command):

    def execute(self, actor):
        actor.move_up()
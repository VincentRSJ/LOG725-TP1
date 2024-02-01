from commands.command import Command


class MoveDownCommand(Command):

    def execute(self, actor):
        actor.move_down()